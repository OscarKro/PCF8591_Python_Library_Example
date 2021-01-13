###### pin assign
# This document is created for the Minor ICT for non ICT'ers by Oscar Kromhout 13-1-2021.
# It is very heavily based on the library designed by ShuDiamonds. https://github.com/ShuDiamonds/PCF8591
# It uses almost all code from ShuDiamonds and all credits for creating this go to him/her. See his/her Github for further instructions! 

# Below is a while loop containing a very basic example on how to read out all the analog pins.
######



import wiringpi
import time

class PCF8591:
	def __init__(self, addr):
		wiringpi.wiringPiSetup() #setup wiringpi

		self.i2c = wiringpi.I2C() #get I2C
		self.dev = self.i2c.setup(addr) #setup I2C device

	def LED_ON(self):
		self.i2c.writeReg8(self.dev, 0x40, 0xFF)
		
	def LED_OFF(self):
		self.i2c.writeReg8(self.dev, 0x40, 0x00)
		
	def DAoutput(self,value):
		self.i2c.writeReg8(self.dev, 0x40, value)
		
	def analogRead0(self):
		self.i2c.writeReg8(self.dev, 0x48,0x40)
		self.i2c.readReg8(self.dev,0x48)	#Read first(former) byte. p8 datasheet
		return self.i2c.readReg8(self.dev,0x48)
		
	def analogRead1(self):
		self.i2c.writeReg8(self.dev, 0x48,0x41)
		self.i2c.readReg8(self.dev,0x48)	#Read first(former) byte. p8 datasheet
		return self.i2c.readReg8(self.dev,0x48)
		
	def analogRead2(self):
		self.i2c.writeReg8(self.dev, 0x48,0x42)
		self.i2c.readReg8(self.dev,0x48)	#Read first(former) byte. p8 datasheet
		return self.i2c.readReg8(self.dev,0x48)
	def analogRead3(self):
		self.i2c.writeReg8(self.dev, 0x48,0x43)
		self.i2c.readReg8(self.dev,0x48)	#Read first(former) byte. p8 datasheet
		return self.i2c.readReg8(self.dev,0x48)
	def analogRead(self,pin):
		self.i2c.writeReg8(self.dev, 0x48,0x40+pin)
		self.i2c.readReg8(self.dev,0x48)	#Read first(former) byte. p8 datasheet
		return self.i2c.readReg8(self.dev,0x48)


pcf8591 = PCF8591(0x48) 			# Create the PCF8581 object. Google object Orientated programming for more information on this.
while True: 						# Create a never ending while loop
	value0=pcf8591.analogRead0()	# Read Pin 0 and place the data in the variable value0
	time.sleep(0.1)					# Sleep a short while to give the chip some time to adjust (Maybe not necessary?, use trial and error to find out)
	value1=pcf8591.analogRead1()	# same as line 56
	time.sleep(0.1)					# same as line 57
	value2=pcf8591.analogRead2()	# etc
	time.sleep(0.1)					# etc
	value3=pcf8591.analogRead3()	# etc
	time.sleep(0.1)					# etc
	print("value0: " + str(value0) + " value1: " + str(value1) + " value2: " + str(value2) + " value3: " + str(value3)) # print all the outcomes

	

