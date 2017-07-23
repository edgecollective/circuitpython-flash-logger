# circuitpython-flash-logger

Basic datalogging to SPI flash memory on CircuitPython Express board.  Only Feather M0 Express has been tested.

## Credits

Based off super-helpful suggestions by [tannewt2](https://forums.adafruit.com/memberlist.php?mode=viewprofile&u=342057) of Adafruit.


## Requirements

- **Hardware**.  This particular setup requires using a simple switch to toggle the state of an IO pin on the board.  A through-hole 10K resistor can be used for this purpose.

- **Software**.  This firmware requires that a recent version of the [circuitpython UF2 master branch](https://github.com/adafruit/circuitpython/commits/master), which allows for filesystem remount via [storage.remount()](https://circuitpython.readthedocs.io/en/latest/shared-bindings/storage/__init__.html), be installed.  Instructions below for how to do this for the Feather M0 Express board.


## Installation (Feather M0 Express)

(All code below comes from the "feather_m0_express" directory in this github repo.)

1. **Connect the microcontroller** to your laptop.

Plug the Feather M0 Express into a USB port.  A USB drive will appear as CIRCUITPY.  Ignore this for now. 

2. **Install the UF2**

- Double-press the reset button in order to enter into bootloader mode.  A USB drive will appear on your desktop as "FEATHERBOOT". 
- Copy the .uf2 file into FEATHERBOOT. 

3. **Install the firmware**

- Now single-press the reset button.  A USB drive will appear on your desktop as "CIRCUITPY".
- Copy "boot.py" and "code.py" into CIRCUITPY.

## Usage (Feather M0 Express)

- **Datalogging**.  Connect a 10K resistor between pin D6 and 3V (pulling D6 "high"), and single-press the RESET button in order to reset the board. The microcontroller will boot up in "datalogging mode", and write values to a file called "data.txt" on the on-board SPI flash chip at one second intervals, flashing the red on-board LED after each write.  In this mode, write access to the SPI Flash via USB is disabled -- i.e., CIRCUITPY mounts in "read-only" mode.  

- **Reprogramming**. When D6 is not pulled "high" (no connector / resistor between D6 and 3V), the microcontroller will simply flash the on-board LED at 0.2 second intervals, and CIRCUITPY mounts in "write-allowed" mode.  This allows for new boot.py and code.py code to be uploaded to the board via drag-drop.








