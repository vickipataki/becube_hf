from spriteok.figura import Figura

class Szorny(Figura):
    kep = None

    def __init__(self, x, y, eletero, sebzes):
        super().__init__(x, y)
        self.eletero = eletero
        self.sebzes = sebzes

    def megjelenit(self):
        print("Szörny: koordináták: (" + str(self.center_x) + ", " + str(self.center_y) + "), életerő: " + str(self.eletero) + ", sebzés: " + str(self.sebzes))