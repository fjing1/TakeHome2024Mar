from sortedcontainers import SortedDict

class IntensityDict:
    """Manage intensities within a range"""
    def __init__(self):
        self.intensities_dict = SortedDict() # Keys are always maintain sorted
        self.default_val = 0

    def add(self, start, end, amount):
        """Add amount to intensities within range, end is not inclusive"""
        self.intensities_dict[end] = self.intensities_dict.get(end, 0)
        self._update(start, end, amount)

    def get_intensities_dict(self):
        """Return the intensities as the requested format"""
        return [(key, value) for key, value in self.intensities_dict.items()]

    def set(self, start, end, amount):
        """Set the intensities within a range to target amount"""
        if start not in self.intensities_dict:
            self.intensities_dict[start] = self.default_val
        if end not in self.intensities_dict:
            self.intensities_dict[end] = self.default_val
        # Inclusive flag can be customized upon request, since this part wasnt clear in the requirement
        keys_in_range = list(self.intensities_dict.irange(start, end, inclusive=(True, False)))
        for key in keys_in_range:
            self.intensities_dict[key] = amount
        self._clean_up_dict()

    def _update(self, start, end, amount):
        if start in self.intensities_dict:
            self.intensities_dict[start] += amount
        else:
            prev_key_index = self.intensities_dict.bisect_right(start) - 1
            if prev_key_index >= 0:
                prev_key = self.intensities_dict.iloc[prev_key_index]
                self.intensities_dict[start] = self.intensities_dict[prev_key] + amount
            else:
                self.intensities_dict[start] = amount

        next_key_index = self.intensities_dict.bisect_right(start)
        if next_key_index < len(self.intensities_dict):
            next_key = self.intensities_dict.iloc[next_key_index]
        else:
            next_key = None
        if end in self.intensities_dict:
            for key in self.intensities_dict.irange(next_key, self.intensities_dict.iloc[self.intensities_dict.bisect_left(end) -1 ]):
                self.intensities_dict[key] += amount
        else:
            self.intensities_dict[end] = self.default_val
        self._clean_up_dict()

    def _clean_up_dict(self):
        prev_val = 0
        keys_to_rm = []
        for key, value in self.intensities_dict.items():
            if value == prev_val:
                keys_to_rm.append(key)
            else:
                prev_val = value

        for key in keys_to_rm:
            del self.intensities_dict[key]

    def clear(self):
        """Clear intensities"""
        self.intensities = {}