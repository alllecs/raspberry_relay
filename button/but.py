import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(16)
    if input_state == False:
        print('Button 1 Pressed')
    input_state = GPIO.input(20)
    if input_state == False:
        print('Button 2 Pressed')
    input_state = GPIO.input(21)
    if input_state == False:
        print('Button 3 Pressed')
        time.sleep(0.2)
