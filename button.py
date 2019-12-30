import RPi.GPIO as GPIO
from time import sleep
from subprocess import call
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Give the pin a physical position
#Set up the Lights
GPIO.setup(29, GPIO.OUT, initial = 1) #Red Turn pin 29 to high
GPIO.setup(31, GPIO.OUT, initial = 1) #Blue Turn pin 31 to high
GPIO.setup(33, GPIO.OUT, initial = 1) #White Turn pin 7 to high
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Red Make pin 13 a button, set to high
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Blue Make pin 15 a button, set to high
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) #White Make pin 18 a button, set to high

try: 
  while True:
    input_state11 = GPIO.input(11) #set input_state13 to high
    input_state13 = GPIO.input(13) #set input_state15 to high
    input_state15 = GPIO.input(15) #set input_state18 to high
    if input_state11 == False: #if button is pressed, pin 13 is low
      GPIO.output(29, 0) #light goes off
      #GPIO.output(31, 0)
      #GPIO.output(33, 0)
      print('Red button pressed')
      sleep(0.2) #wait
      GPIO.output(29, 1) #light goes on
      os.system('pkill arecord')
      #call(['python','play_audio.py'])
      #GPIO.output(31, 1)
      #GPIO.output(33, 1)
    if input_state13 == False: #initiates recording
      GPIO.output(31, 0) #light goes off
      os.system('arecord -D hw:1,0 -f cd test.wav -c 1 &')
      print('Blue button pressed')
      sleep(0.2) #wait
      GPIO.output(31, 1) #light goes on
    if input_state15 == False:
      GPIO.output(33, 0) #light goes off
      print('White button pressed')
      os.system('aplay test.wav')
      sleep(0.2) #wait
      GPIO.output(33, 1) #light goes on 
except KeyboardInterrupt:
  GPIO.output(29, 0)
  GPIO.output(31, 0)
  GPIO.output(33, 0)


