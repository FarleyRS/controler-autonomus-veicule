import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)

    def frente(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def tras(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

    def parar(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)


# Configura o modo de numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Define motores
motor1 = Motor(24, 23)  # motor esquerdo
motor2 = Motor(27, 22)  # motor direito

def frente():
    motor1.frente()
    motor2.frente()

def tras():
    motor1.tras()
    motor2.tras()

def parar():
    motor1.parar()
    motor2.parar()


try:
    while True:
        comando = input("Digite 'f' para frente, 't' para tras, 'p' para parar ou 'q' para sair: ")

        if comando == 'f':
            frente()
            print("Movendo para frente...")

        elif comando == 't':
            tras()
            print("Movendo para tras...")

        elif comando == 'p':
            parar()
            print("Parado!!!")

        elif comando == 'q':
            parar()
            print("SAINDO...")
            break

        else:
            print("Comando invalido.")

        time.sleep(2)

finally:
    parar()
    GPIO.cleanup()
    print("GPIO liberado com sucesso.")
