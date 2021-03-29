from abc import ABC, abstractmethod
from random import randrange


class Fighter(ABC):
    def __init__(self, name):
        self.name = name
        self._punch = randrange(11)
        self._resistance = randrange(5)

    @abstractmethod
    def train(self):
        print(f'{self.name} is training...')
        pass

    def fight_coef(self):
        return self._punch * self._resistance

    def fight(self, rival):
        if self.fight_coef() > rival.fight_coef():
            print(f'{self.name} wins the fight')
        elif self.fight_coef() == rival.fight_coef():
            print(f'Its a draw')
        else:
            print(f'{self.name} loses the fight')


