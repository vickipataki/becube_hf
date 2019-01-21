from spriteok.szorny import Szorny

class Demon(Szorny):
    kep = "img/demon.png"

    def __init__(self, x, y):
        super().__init__(x, y, 1, 2)