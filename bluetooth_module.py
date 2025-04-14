import serial

class BluetoothReceiver:
    def __init__(self, port="COM5", baudrate=9600):  # Troque a COM5 pela sua porta Bluetooth!
        self.perimeter = []
        self.start_point = None
        self.ready = False
        self.ser = serial.Serial(port, baudrate, timeout=1)

    def receive_all(self):
        print("Aguardando dados Bluetooth do app...")

        while True:
            if self.ser.in_waiting:
                data = self.ser.readline().decode("utf-8").strip().lower()
                print(f"Recebido: {data}")

                if data == "fim":
                    print("Perímetro finalizado.")
                    continue

                elif data.startswith("start:"):
                    try:
                        lat, lon = map(float, data.replace("start:", "").split(","))
                        self.start_point = (lat, lon)
                        print("Ponto de início recebido.")
                    except:
                        print("Erro ao processar ponto de início.")

                elif data == "iniciar" or data == "start":
                    print("Confirmação recebida para iniciar.")
                    self.ready = True
                    break

                else:
                    try:
                        lat, lon = map(float, data.split(","))
                        self.perimeter.append((lat, lon))
                    except:
                        print("Dado inválido. Envie coordenadas como lat,lon")

        self.ser.close()
        return self.perimeter, self.start_point
