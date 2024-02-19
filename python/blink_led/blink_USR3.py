# USR3 LED Blinking Code




import Adafruit_BBIO.GPIO as GPIO
import time

leds = ['USR0', 'USR1', 'USR2', 'USR3']
i = 0;
delay = 0.1;

print('hit ^C to stop')
print('toggling LEDs:')

for x in leds:
    GPIO.setup(x,GPIO.OUT)
    print("0", end='')
    
def n(i):
    if i >= len(leds) :
        return 2*len(leds)-i-2
    else:
        return i 
        
# section to cause blinking of USR3 LED
while True:

# Causes 0.1 second blink of USR3 LED
    GPIO.output(leds[3],GPIO.HIGH)
    time.sleep(0.1)
   
# Causes 0.1 second pause/deactivation of USR3 LED
    GPIO.output(leds[3],GPIO.LOW)
    time.sleep(0.1)   

while True:
    print("\x1b[" + str(n(i)+1) + "G1", end='', flush=True)
    GPIO.output(leds[n(i)],GPIO.HIGH)
    time.sleep(delay)
    
    print("\x1b[" + str(n(i)+1) + "G0", end='', flush=True)
    GPIO.output(leds[n(i)],GPIO.LOW)
    i = i + 1
    if i >= 2*len(leds)-2:
        i = 0
        
        