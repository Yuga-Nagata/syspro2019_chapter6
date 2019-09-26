#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import cgi
import cgitb

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('<input type="number" name="angle">')
print('<input type="submit" value="submit">')
print('</form>')

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

def setservo(arg):
        duty = ( (2.4-0.5)*(arg+90)/180 + 0.5 ) / 20 * 100
        servo.ChangeDutyCycle(duty)
        time.sleep(0.5)

form = cgi.FieldStorage()
value = form.getvalue("angle")

setservo(float(value))
print(float(value))
GPIO.cleanup()
