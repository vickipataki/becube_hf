from spriteok.figura import Figura

class Lada(Figura):
    kep = "img/lada.png"

    def __init__(self, x, y, tartalom, nyitva):
        super().__init__(x, y)
        self.tartalom = tartalom
        self.nyitva = nyitva

    def tartalom_kiiras(self):
        if self.nyitva:
            if self.tartalom != []:
                print("A láda a következőket tartalmazza:")
                for elem in self.tartalom:
                    print("    - " + elem)
            else:
                print("A láda üres")
        else:
            print("A láda zárva van")

    def kifoszt(self, jatekos):
        if jatekos.leptem:
            jatekos.leptem = False
            self.tartalom_kiiras()
            if self.nyitva:
                for targy in self.tartalom:
                    jatekos.targyat_talal(targy)
                self.tartalom = []


if __name__ == "__main__":
    elso_lada = Lada(2, 5, ['balta', 'kard'], True)
    masodik_lada = Lada(3, 4, ['balta', 'páncél'], False)
    elso_lada.tartalom_kiiras()
    masodik_lada.tartalom_kiiras()