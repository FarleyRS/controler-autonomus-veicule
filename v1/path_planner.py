import numpy as np

class PathPlanner:
    def __init__(self, perimeter, cell_size=0.00003):
        self.perimeter = perimeter
        self.cell_size = cell_size

    def is_inside_polygon(self, point):
        x, y = point
        vertices = self.perimeter
        inside = False
        n = len(vertices)
        p1x, p1y = vertices[0]

        for i in range(n + 1):
            p2x, p2y = vertices[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def generate_grid(self):
        min_lat = min(p[0] for p in self.perimeter)
        max_lat = max(p[0] for p in self.perimeter)
        min_lon = min(p[1] for p in self.perimeter)
        max_lon = max(p[1] for p in self.perimeter)

        lat_range = np.arange(min_lat, max_lat, self.cell_size)
        lon_range = np.arange(min_lon, max_lon, self.cell_size)

        grid = []
        for lat in lat_range:
            for lon in lon_range:
                center = (lat + self.cell_size/2, lon + self.cell_size/2)
                if self.is_inside_polygon(center):
                    grid.append(center)
        return grid

    def zigzag_path(self, grid):
        path = []
        rows = sorted(set(p[0] for p in grid))
        cols = sorted(set(p[1] for p in grid))

        for i, row in enumerate(rows):
            col_range = cols if i % 2 == 0 else reversed(cols)
            for col in col_range:
                pt = (row, col)
                if pt in grid:
                    path.append(pt)
        return path
