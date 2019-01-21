from spriteok.figura import Figura

class Erme(Figura):
    kep = "img/Coin1.png"
    szamlalo = 0

    def __init__(self, x, y, ertek):
        super().__init__(x, y)
        self.ertek = ertek
        Erme.szamlalo += 1