from spriteok.figura import Figura, MEZO_MERET
from jatek_fuggvenyek import Irany, aranyat_talaltal
import arcade

class Jatekos(Figura):
    kep = "img/lovag.png"

    def __init__(self, x, y, eletek):
        super().__init__(x, y)
        self.leptem = False
        self.eletek = eletek
        self.legutobbi_lepes = Irany.SEMERRE
        self.arany = 0
        self.tavolsag = 0
        self.targylista = []

    def balra_lep(self, fal_lista):
        eredeti_koordinata = self.center_x # "Elmentjuk" az eredeti helyet
        self.center_x -= MEZO_MERET # Ideiglenesen athelyezzuk
        if not self.falon_all(fal_lista): # Megnezzuk, hogy az uj hely fal-e
            self.legutobbi_lepes = Irany.BALRA # Ha nem, marad az ideiglenes hely
            self.leptem = True
        else:
            self.center_x = eredeti_koordinata # Ha falon all, marad a hely

    def jobbra_lep(self, fal_lista):
        eredeti_koordinata = self.center_x
        self.center_x += MEZO_MERET
        if not self.falon_all(fal_lista):
            self.legutobbi_lepes = Irany.JOBBRA
            self.leptem = True
        else:
            self.center_x = eredeti_koordinata

    def lefele_lep(self, fal_lista):
        eredeti_koordinata = self.center_y
        self.center_y -= MEZO_MERET
        if not self.falon_all(fal_lista):
            self.legutobbi_lepes = Irany.LE
            self.leptem = True
        else:
            self.center_y = eredeti_koordinata

    def felfele_lep(self, fal_lista):
        eredeti_koordinata = self.center_y
        self.center_y += MEZO_MERET
        if not self.falon_all(fal_lista):
            self.legutobbi_lepes = Irany.FEL
            self.leptem = True
        else:
            self.center_y = eredeti_koordinata

    def aranyat_talal(self, talalt_arany):
        self.arany = aranyat_talaltal(talalt_arany, self.arany)

    def targyat_talal(self, targy):
        print("Találtál egy " + targy + " tárgyat!")
        self.targylista.append(targy)

    def falon_all(self, fal_lista):
        return not arcade.check_for_collision_with_list(self, fal_lista) == []