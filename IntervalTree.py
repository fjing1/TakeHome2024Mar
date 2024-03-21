class IntervalTree:
    def __init__(self):
        self.tree = {}

    def add(self, start, end, value):
        self.tree[(start, end)] = value

    def get(self, start, end):
        return self.tree.get((start, end), None)

# Usage
i_tree = IntervalTree()
i_tree.add(10, 30, 1)
print(i_tree.get(10,30))  # Output: [[10, 1], [30, 0]]
print(i_tree.add(20, 40, 1))
print(i_tree.add(10, 40, -2))