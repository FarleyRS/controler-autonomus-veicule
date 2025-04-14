import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    def __init__(self, trig=23, echo=24):
        self.trig = trig
        self.echo = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trig, False)
        time.sleep(2)

    def get_distance(self):
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()

        duration = pulse_end - pulse_start
        distance = duration * 17150  # cm
        return round(distance, 2)

    def cleanup(self):
        GPIO.cleanup()
