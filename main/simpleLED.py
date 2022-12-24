'''
This code creates a simple blinking LED light from single GPIO pin
'''
import RPi.GPIO as GPIO
import time

#number of GPIO pin
LED_PIN = 17

#use the GPIO numbers instead of the “standard” pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    #reset all states and modes for all GPIOs, 
    #which can prevent you from having errors in future programs.
    GPIO.cleanup()