from gps_module import GPSModule
from bluetooth_module import BluetoothReceiver
from ultrasonic_sensor import UltrasonicSensor
from path_planner import PathPlanner
from navigator import Navigator
from motor_driver import MotorDriver

if __name__ == "__main__":
    try:
        print("=== Iniciando sistema autônomo ===")

        gps = GPSModule()
        bluetooth = BluetoothReceiver()
        ultrasonic = UltrasonicSensor()
        motor = MotorDriver()

        print("Aguardando coordenadas, ponto inicial e confirmação do APP...")
        perimeter, start_point = bluetooth.receive_all()

        if not start_point:
            print("Erro: Ponto de início não recebido.")
            exit()

        planner = PathPlanner(perimeter)
        grid = planner.generate_grid()
        path = planner.zigzag_path(grid)

        # Reposicionamento: encontre o ponto mais próximo da partida
        if start_point:
            closest = min(path, key=lambda p: (p[0] - start_point[0])**2 + (p[1] - start_point[1])**2)
            start_index = path.index(closest)
            path = path[start_index:]  # Começa do ponto mais próximo

        navigator = Navigator(gps, ultrasonic, path, motor)
        navigator.navigate()

    except KeyboardInterrupt:
        print("\nEncerrando o sistema...")
    finally:
        ultrasonic.cleanup()
        motor.cleanup()
