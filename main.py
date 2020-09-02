#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import random

GPIO_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(GPIO_PIN, True)
        time.sleep(random.random() * 5.0)
        GPIO.output(GPIO_PIN, False)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
