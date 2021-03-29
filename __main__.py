from Karateka import Karateka
from Taekwondoist import Taekwondoist


def main():
    Jin = Karateka('Jin Kazama')
    Hwoarang = Taekwondoist('Hwoarang')
    Jin.fight(Hwoarang)
    Hwoarang.train()
    Jin.fight(Hwoarang)

main()