import arcade  # A jatek grafikáját oldja meg

MEZO_MERET = 32 # Ekkora egy "kocka"

class Figura(arcade.Sprite):
    kep = None

    def __init__(self, x, y):
        super().__init__(self.kep)
        self.center_x, self.center_y = self.koordinatak_szamolasa(x, y)

    def koordinatak_szamolasa(self, x_mezo, y_mezo):
        x_pixelben = MEZO_MERET * x_mezo + MEZO_MERET / 2
        y_pixelben = MEZO_MERET * y_mezo + MEZO_MERET / 2
        return x_pixelben, y_pixelben