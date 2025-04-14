import RPi.GPIO as GPIO
import time

class MotorDriver:
    def __init__(self, in1=17, in2=18, in3=27, in4=22, ena=23, enb=24):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.ena = ena
        self.enb = enb

        GPIO.setmode(GPIO.BCM)
        GPIO.setup([in1, in2, in3, in4, ena, enb], GPIO.OUT)

        self.pwmA = GPIO.PWM(ena, 1000)
        self.pwmB = GPIO.PWM(enb, 1000)
        self.pwmA.start(0)
        self.pwmB.start(0)

    def move_forward(self, speed=60):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        self.pwmA.ChangeDutyCycle(speed)
        self.pwmB.ChangeDutyCycle(speed)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)

    def turn_left(self, speed=50):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        self.pwmA.ChangeDutyCycle(speed)
        self.pwmB.ChangeDutyCycle(speed)

    def turn_right(self, speed=50):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)
        self.pwmA.ChangeDutyCycle(speed)
        self.pwmB.ChangeDutyCycle(speed)

    def cleanup(self):
        self.stop()
        GPIO.cleanup()
