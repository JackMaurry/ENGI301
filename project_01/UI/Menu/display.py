"""
--------------------------------------------------------------------------
Display And Menu
--------------------------------------------------------------------------
License:   
Copyright 2023 <Jack Maurry>

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use the HT16K33 Display and a button to create a digital people counter

Requirements:
  - Increment the counter by one each time the button is pressed
  - If button is held for more than 2s, reset the counter

Uses:
  - HT16K33 display library developed in class

"""
import time

import Adafruit_BBIO.GPIO as GPIO

import ht16k33 as HT16K33
import button as BUTTON

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Display():
    select_time = None
    button     = None
    display    = None
    
    # vars to be outputted to ShuffleOrder
    Shuffle_Choice = None
    Players = None
    SBP = None
    HandSelected = None
    
    def __init__(self, select_time=1.0, button="P2_2", i2c_bus=1, i2c_address=0x70):
        """ Initialize variables and set up display """
        self.select_time = select_time
        self.button     = BUTTON.Button(button)
        self.display    = HT16K33.HT16K33(i2c_bus, i2c_address)
    
    # End def

    # Takes User Input on whether to do a randomized shuffle or user-modified shuffle
    def ShuffleMethod(self):
        
        self.Shuffle_Choice          = 0        # Shuffle method chosen
        button_press_time            = 0.0      # Time button was pressed (in seconds)
        
        self.display.text("SHUF")
        self.button.wait_for_press()
        button_press_time = self.button.get_last_press_duration()
        if (button_press_time < self.select_time):
                self.display.text("RAND")

    
        while(button_press_time < 1.0):
            
            # Wait for button press / release
            self.button.wait_for_press()
            # Get the press time
            button_press_time = self.button.get_last_press_duration()

            #MOVE 1 UP IN MENU SLOT
            if (self.button.is_pressed and button_press_time < 1.0):
            
                if (self.Shuffle_Choice == 0):
                    self.display.text("INPT")
                    self.Shuffle_Choice = 1
                
                else:
                    self.display.text("RAND")
                    self.Shuffle_Choice = 0
        
        print('Shuffle Method Chosen: ' + str(self.Shuffle_Choice))
        

        if (self.Shuffle_Choice == 1):
            self.SmallBlindPosition()
        
    # End def
    
    # Takes User Input on where small blind position is located 
    def SmallBlindPosition(self):
        
        self.Shuffle_Choice          = 0        # Shuffle method chosen
        button_press_time            = 0.0      # Time button was pressed (in seconds)
        
        self.display.text("SHUF")
        self.button.wait_for_press()
        button_press_time = self.button.get_last_press_duration()
        if (button_press_time < self.select_time):
                self.display.text("RAND")

    
        while(button_press_time < 1.0):
            
            # Wait for button press / release
            self.button.wait_for_press()
            # Get the press time
            button_press_time = self.button.get_last_press_duration()

            #MOVE 1 UP IN MENU SLOT
            if (self.button.is_pressed and button_press_time < 1.0):
            
                if (self.Shuffle_Choice == 0):
                    self.display.text("INPT")
                    self.Shuffle_Choice = 1
                
                else:
                    self.display.text("RAND")
                    self.Shuffle_Choice = 0
        
        print('Shuffle Method Chosen: ' + str(self.Shuffle_Choice))
    """    
    def PlayersInHand(self):
    
    def HandSelection(self):
        
    def Start(self):
    """

    def cleanup(self):
        """Cleanup the hardware components."""
        # Set Display to something unique to show program is complete
        self.display.text("ERR")
    # End def

# End class

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the display 
    Player_Menu = Display()
    try:
        # Run the display
        Player_Menu.ShuffleMethod()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        Player_Menu.cleanup()

    print("Program Complete")

