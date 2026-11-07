import random

class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.pos[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos.pop(val)
        last = self.vals.pop()

        if last != val:
            self.vals[idx] = last
            self.pos[last] = idx

        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)