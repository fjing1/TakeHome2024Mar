class IntensityManager:
    def __init__(self):
        self.intensities = {}
        self.turning_point = set()

    def get_turning_point_intensities(self):
        turning_point_intensities = []
        prev_value = 0
        for k, value in self.intensities.items() :
            # If the key is in the turning_point set, add it to the turning_point_intensities list as a tuple
            if k in self.turning_point and value != prev_value:
                turning_point_intensities.append((k, value))
            prev_value = value

        return turning_point_intensities

    def add(self, start, end, amount):
        self.turning_point.add(start)
        self.turning_point.add(end)
        self._update(start, end, amount, lambda x, y: x + y)

    # Clarified with Tomoka Inoue, implemented with my assumptions
    # Set behave same as add, update the starting point, but end point is not included.
    def set(self, start, end, amount):
        self.turning_point.add(start)
        self.turning_point.add(end)
        self._update(start, end, amount, lambda x, y: y)

    def _update(self, start, end, amount, operation):
        start_intensity = self._get_intensity(start)
        end_intensity = self._get_intensity(end)
        for key in range(start, end):
            current_intensity = self._get_intensity(key)
            self.intensities[key] = operation(current_intensity, amount)
        self.intensities[end] = operation(end_intensity, 0)

    def _get_intensity(self, request_point):
        if request_point in self.intensities:
            return self.intensities[request_point]
        return 0

    def clear(self):
        self.intensities = {}
        self.turning_point = set()