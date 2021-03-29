from Fighter import Fighter


class Taekwondoist(Fighter):

    def __init__(self, name):
        super().__init__(name)

    def train(self):
        Fighter.train(self)
        self._punch += 2
        self._resistance += 1/2
