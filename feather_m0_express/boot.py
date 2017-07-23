import digitalio
import board
import storage

switch=digitalio.DigitalInOut(board.D6)
switch.switch_to_input()

storage.remount("/",not switch.value) # switch.value==False means datalogging mode:  allow circuitpython code to write to flash, while making USB read-only.  So: pull D6 high for datalogging, leave D6 at ground for USB write access (reprogramming).
