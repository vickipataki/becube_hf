from spriteok.szorny import Szorny

class Ork(Szorny):
    kep = "img/ork.png"

    def __init__(self, x, y):
        super().__init__(x, y, 2, 1)