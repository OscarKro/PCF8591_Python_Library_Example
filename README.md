# PCF8591_Python_Library_Example

![PCF](./images/pcf8591.jpg)
This small repo is created for the Minor ICT for NON-ICT'ers from the university of applied siences Utrecht by Oscar kromhout on 13-1-2021. 
The example has a PCF8591 class which contains some very basic code to read out (and optional write) data from the PCF8591 using Python. 
It is completely based on the library from Shudiamonds. See: https://github.com/ShuDiamonds/PCF8591. All credits for creating this code except for the example on the lower side of the document go to him/her. I only used his/her code to create a simple to use example and document for the minor students.
Because Shundiamonds had originally placed his library under the MIT license I decided to also add this license to this repo.

## Requirements

- Raspberry pi (i tested it on a 3b+)
- PCF8591
- wires (and breadboard)
- Python 3
- The Wiring pi library

## how to start

- Run "sudo raspi-config" in the terminal
- Go to interfaces and enable I2C
- Finish
- Run "pip3 install wiringpi" in the terminal
- Wire the PCF8591 as described in the chapter "wiring"
- Run "python3 PCF8591.py" in the terminal to confirm it working
- Copy the PCF8591 class to your own project and use it like the example

## extra data
If you want/need to know more in depth information on the chip see the datasheet.

https://www.nxp.com/docs/en/data-sheet/PCF8591.pdf


## how to wire
PCF / pi

gnd		->	gnd

vcc		->	5V

scl		->	scl

sda		->	sda

a0/a3in -> 	whatever you want to read
![pins](./images/pins.jpg)

### caveats
I only tested (and build) it in a very small amount of time on a late evening. As far as I could tell, everything worked just fine, but as with everything, on certain applications things may work different from what you've expected
or maybe an error occurs that I've overseen. I cannot be held responsible for it nor will I feel any responsibillity for your project not working/failing/exploding/dying/causing damages. In other words, USE AT YOUR OWN RISK!



