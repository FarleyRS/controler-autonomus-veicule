from math import radians, cos, sin, asin, sqrt
from motor_driver import MotorDriver

import time

class Navigator:
    def __init__(self, gps, ultrasonic, path, motor, tolerance=3.0, avoid_distance=50.0):
        self.gps = gps
        self.ultrasonic = ultrasonic
        self.motor = motor
        self.path = path
        self.tolerance = tolerance
        self.avoid_distance = avoid_distance

    def haversine(self, lat1, lon1, lat2, lon2):
        R = 6371000
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        return R * 2 * asin(sqrt(a))

    def find_closest_waypoint(self, current):
        closest = None
        min_dist = float("inf")
        for wp in self.path:
            dist = self.haversine(current[0], current[1], wp[0], wp[1])
            if dist < min_dist:
                min_dist = dist
                closest = wp
        return closest

    def navigate(self):
        index = 0
        while index < len(self.path):
            waypoint = self.path[index]
            current = self.gps.get_position()
            dist = self.haversine(current[0], current[1], waypoint[0], waypoint[1])

            if self.find_closest_waypoint(current) != waypoint:
                print("Recalculando rota...")
                index = self.path.index(self.find_closest_waypoint(current))
                continue

            if self.ultrasonic.get_distance() < self.avoid_distance:
                print("Obstáculo à frente! Parando e desviando...")
                self.motor.stop()
                time.sleep(1)
                self.motor.turn_right()
                time.sleep(1)
                self.motor.move_forward()
                time.sleep(1)
                continue

            print(f"Indo para {index+1}/{len(self.path)} | Distância: {dist:.1f}m")
            self.motor.move_forward()

            if dist <= self.tolerance:
                print("Waypoint alcançado!\n")
                self.motor.stop()
                index += 1

            time.sleep(1)

