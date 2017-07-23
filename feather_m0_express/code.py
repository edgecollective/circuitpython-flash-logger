import digitalio
import board
import time

switch=digitalio.DigitalInOut(board.D6)
switch.switch_to_input()

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

if switch.value==True: # if pin D6 is pulled high, then datalog mode -- no USB write allowed
    for i in range(10): # keep number of writes low for testing
        f=open('data.txt','a')
        f.write('{:03d}\n'.format(i))
        f.close()
        led.value = not led.value # blink to indicate successful write
        time.sleep(1)
        
else:
    while True:
        led.value = not led.value #faster blink to indicate in USB read-write mode
        time.sleep(.2)
