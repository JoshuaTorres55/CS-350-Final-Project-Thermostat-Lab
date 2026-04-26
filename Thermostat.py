from gpiozero import Button, PWMLED
import time
import board
import busio
import adafruit_ahtx0
import serial

# LEDs
red = PWMLED(17)
blue = PWMLED(27)

# Buttons
mode_button = Button(5)
up_button = Button(25)
down_button = Button(12)

# I2C sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

# UART
ser = None

state = "off"
set_temp = 72
