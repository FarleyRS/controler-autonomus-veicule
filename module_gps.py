import serial

class GPSModule:
    def __init__(self, port="/dev/serial0", baudrate=9600):
        self.gps = serial.Serial(port, baudrate, timeout=1)

    def get_position(self):
        while True:
            line = self.gps.readline().decode("utf-8", errors="ignore")
            if "$GPGGA" in line:
                try:
                    data = line.split(",")
                    if data[2] and data[4]:
                        lat = self._convert(data[2], data[3])
                        lon = self._convert(data[4], data[5])
                        return lat, lon
                except:
                    continue

    def _convert(self, coord, direction):
        degrees = float(coord[:2])
        minutes = float(coord[2:])
        decimal = degrees + (minutes / 60)
        if direction in ['S', 'W']:
            decimal *= -1
        return decimal
