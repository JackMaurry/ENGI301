"""
MIT License

Copyright (c) 2019 DDeGonge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__version__ = '0.1.0'

import sys
import time
import os
import cv2
import scipy.misc
import numpy as np

class Train_Obj(object):
    """ Stores training image and name for either rank or suit set """
    def __init__(self, img = [], name = None):
        self.img = img
        self.name = name

class Camera(object):
    TRAIN_PATH = 'helpers/Card_Images'
    def __init__(self, resolution=cfg.IMAGE_RESOLUTION):
        self.camera = None
        self.resolution = resolution
        self.train_ranks = self.load_calibration_set(self.TRAIN_PATH, ALLRANKS)
        self.train_suits = self.load_calibration_set(self.TRAIN_PATH, ALLSUITS)
        self.white_offset_img = self.load_offset_image(self.TRAIN_PATH, 'cal.jpg')

    def read_card(self, enable_and_disable: bool = False):
        image = self._capture_image(enable_and_disable)
        processed_img = self.preprocess_image(image)
        return self.match_card(processed_img)

    def exposure_sweep(self, exposures):
        img = self._capture_image(enable_and_disable=True)
        return [self.preprocess_image(img, int(exp)) for exp in exposures]

    def _capture_image(self, enable_and_disable):
        if enable_and_disable:
            self.start_camera()
        rawCapture = PiRGBArray(self.camera)
        self.camera.capture(rawCapture, format="bgr")
        if enable_and_disable:
            self.stop_camera()
        return rawCapture.array

    @staticmethod
    def _display_image(img):
        cv2.imshow("Image", img)
        cv2.waitKey(0)

    @staticmethod
    def _save_image(img, path):
        scipy.misc.toimage(img, cmin=0.0, cmax=...).save('path')

    def start_camera(self):
        self.camera = PiCamera()
        self.configure_camera()

    def configure_camera(self):
        self.camera.rotation = cfg.IMAGE_ROTATION_DEGS
        self.camera.resolution = self.resolution
        self.camera.exposure_mode = 'off'

    def stop_camera(self):
        self.camera.close()

    """ Image recognition functions """

    def preprocess_image(self, img, exp_threshold = None):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        blur_crop = blur[cfg.H_MIN:cfg.H_MAX, cfg.W_MIN:cfg.W_MAX]
        if cfg.USE_CAL_IMAGE:
            # Subtract from background white cal image before thresholding
            blur_crop = self.white_offset_img - blur_crop
            blur_crop[blur_crop > 200] = 0
            if cfg.DEBUG_MODE:
                debug_save_img(blur_crop, 'offset_greyscale.jpg')
                debug_save_img(blur, 'greyscale.jpg')
            
        if exp_threshold is None:
            exp_threshold = cfg.BW_THRESH
        _, proc_img = cv2.threshold(blur_crop, exp_threshold, 255, cv2.THRESH_BINARY)

        if not cfg.USE_CAL_IMAGE:
            proc_img = cv2.bitwise_not(processed_image)

        if cfg.DEBUG_MODE:
            debug_save_img(proc_img, 'thresholded.jpg')

        return proc_img

    def match_card(self, processed_image):
        """ Finds best rank and suit matches for the query card. Differences
        the query card rank and suit images with the train rank and suit images.
        The best match is the rank or suit image that has the least difference."""

        qCard = Card()

        # Invert image and find contours
        _, contours, _ = cv2.findContours(processed_image, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        # Trim smallest contours if too many found
        if len(contours) > cfg.MAX_CONTOURS_TO_CHECK:
            contours = contours[:cfg.MAX_CONTOURS_TO_CHECK]

        # Crop contour regions and save as image array to card
        def contour_to_bb(contour):
            x,y,w,h = cv2.boundingRect(contour)
            return processed_image[y:y+h, x:x+w]
        qCard.test_imgs = [contour_to_bb(contour) for contour in contours]

        best_rank_match_diff = 10000
        best_suit_match_diff = 10000

        # Must find at least 2 to find both rank and suit
        if len(qCard.test_imgs) < 2:
            return qCard

        for i, test_img in enumerate(qCard.test_imgs):
            # Find best rank match
            rank_img = cv2.resize(test_img, (cfg.RANK_WIDTH, cfg.RANK_HEIGHT), interpolation=cv2.INTER_CUBIC)
            for Trank in self.train_ranks:
                diff_img = cv2.absdiff(rank_img, Trank.img)
                rank_diff = int(np.sum(diff_img)/255)
                
                if rank_diff < min(best_rank_match_diff, cfg.RANK_DIFF_MAX):
                    best_rank_match_diff = rank_diff
                    qCard.rank = Trank.name

            # Same process with suit images
            suit_img = cv2.resize(test_img, (cfg.SUIT_WIDTH, cfg.SUIT_HEIGHT), interpolation=cv2.INTER_CUBIC)
            for Tsuit in self.train_suits:
                diff_img = cv2.absdiff(suit_img, Tsuit.img)
                suit_diff = int(np.sum(diff_img)/255)
                
                if suit_diff < min(best_suit_match_diff, cfg.SUIT_DIFF_MAX):
                    best_suit_match_diff = suit_diff
                    qCard.suit = Tsuit.name

            if cfg.DEBUG_MODE:
                print('rank:', qCard.rank, best_rank_match_diff)
                print('suit:', qCard.suit, best_suit_match_diff)
                debug_save_img(rank_img, 'rank{}.jpg'.format(i))
                debug_save_img(suit_img, 'suit{}.jpg'.format(i))

            if i >= 2 and qCard.rank is not None and qCard.suit is not None:
                break

        return qCard

    @staticmethod
    def load_calibration_set(filepath, set_names):
        """ Loads calibration rank or suit images to create calibration set. """
        def gen_obj(i):
            img = cv2.imread(os.path.join(filepath, i + '.jpg'), cv2.IMREAD_GRAYSCALE)
            return Train_Obj(img=img, name=i)

        return [gen_obj(i) for i in set_names]

    @staticmethod
    def load_offset_image(filepath, filename):
        import_img = cv2.imread(os.path.join(filepath, filename))
        return cv2.cvtColor(import_img,cv2.COLOR_BGR2GRAY)


if __name__=='__main__':
    c = Camera()
    card = c.read_card(enable_and_disable=True)
    print(card.rank, card.suit)


def debug_save_img(img, imgname):
    im = Image.fromarray(img)
    im.save(os.path.join('/home/pi/', imgname))