import RPi.GPIO as GPIO          
from time import sleep
import time

class Motor:
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2

motor1 = Motor(24, 23)
motor1.in1 = 24
motor1.in2 = 23

motor2 = Motor(27, 22)
motor2.in1 = 27
motor2.in2 = 22

GPIO.setmode(GPIO.BCM)

# moto 1
GPIO.setup(in1, GPIO.OUT)  # IN1
GPIO.setup(in2, GPIO.OUT)  # IN2

# moto 2
GPIO.setup(in3, GPIO.OUT)  # IN3
GPIO.setup(in4, GPIO.OUT)  # IN4


# FunÃ§Ã£o para girar o motor para frente
def frente():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    

# FunÃ§Ã£o para girar o motor para trÃ¡s
def tras():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)

# FunÃ§Ã£o para parar o motor
def parar():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

while(1):

    comando = input("Digite 'f' para frente ou 't' para tras: ")
    
    if comando == 'f':
        frente()
        print("Movendo para frente...")
        
    elif comando == 't':
        tras()
        print("Movendo para tras...")
        
    elif comando == 'p':
        parar()
        print("parado!!!")
        
    elif comando == 'q':
        parar()
        print("SAINDO")
        exit()
        
    else:
        print("Comando invalido.")
        
    time.sleep(2)