from Fighter import Fighter


class Karateka(Fighter):

    def __init__(self, name):
        super().__init__(name)

    def train(self):
        Fighter.train()
        self._punch += 1
        self._resistance += 2