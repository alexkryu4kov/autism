from random import choice


class Experiment:
    def __init__(self, size=8):
        self.size = size

    def generate_data(self):
        return {i: list(range(self.size)) for i in range(self.size)}

    def choose_elem(self):
        return choice(self.generate_data()[0])
