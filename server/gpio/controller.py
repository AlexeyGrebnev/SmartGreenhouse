import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RELAY_PINS = {
    "fan": 17,
    "lamp": 27,
    "pump": 22
}

for pin in RELAY_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def control_device(device, state):
    pin = RELAY_PINS.get(device)
    if pin is None:
        return False
    GPIO.output(pin, GPIO.LOW if state == "on" else GPIO.HIGH)
    return True

def cleanup():
    GPIO.cleanup()