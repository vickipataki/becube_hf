# Importok

from jatek_fuggvenyek import *
import arcade  # A jatek grafikáját oldja meg
from jatek_fuggvenyek import Irany
from spriteok.erme import Erme
from spriteok.kard import Kard
from spriteok.lada import Lada
from spriteok.ork import Ork
from spriteok.demon import Demon
from spriteok.jatekos import Jatekos
from spriteok.fal import Fal

# --- Konstansok ---

KEP_SZELESSEG = 640
KEP_MAGASSAG = 480

MEZO_MERET = 32 # Ekkora egy "kocka"
BAL_HATAR = 48 # Eddig mehet a játékos (képének középpontja) balra
JOBB_HATAR = 592 # Eddig mehet a játékos (képének középpontja) jobbra
FELSO_HATAR = 432 # Eddig mehet a játékos (képének középpontja) felfele
ALSO_HATAR = 48 # Eddig mehet a játékos (képének középpontja) lefele


class LovagJatek(arcade.Window):

    def __init__(self):
        super().__init__(KEP_SZELESSEG, KEP_MAGASSAG, "Lovagjáték")

        # Ezek a valtozok tartalmazzak a sprite listakat
        self.jatekos_lista = None
        self.eletero_lista = None
        self.erme_jelzo_lista = None
        self.erme_lista = None
        self.kard_lista = None
        self.szorny_lista = None
        self.lada_lista = None
        self.fal_lista = None

        # A jatekos_1 sprite-ja
        self.jatekos_sprite = None

        self.jatekos_1 = Jatekos(13, 9, 5)
        self.jatekos_2 = Jatekos(8, 7, 5)

    def on_key_press(self, megnyomott_gomb, modositok):
        """
        Ez a függvény tartalmazza azt, hogy mit kell gombnyomáskor csinálni.

        Automatikusan meghívódik minden gombnyomáskor. Ezt az úgynevezett
        eseményekkel (event) oldjuk majd meg: az 'on_key_press' esemény mindig megtörténik ('elsül'), ha valaki megnyom egy gombot,
        bármelyiket. Ez a függvény az 'on_key_press' esemény kezelő függvénye (event handler).

        A 'megnyomott_gomb' paraméter tartalmazza majd a megnyomott gomb kódját, így el tudjuk dönteni, hogy melyik gombot
        nyomták meg.

        A 'modositok' paramétert is megkapjuk, de nem használjuk. Ezzel lehetne vizsgálni a shift, alt, ctrl, stb. gombok
        lenyomását az eredetielg lenyomott gombbal együtt. Nem használjuk, de az esemény szerkezete miatt meg kell adni.
        """

        # A gombnyomásnak megfelelően odéb tesszük a játékost
        self.mozgasd_a_jatekost(megnyomott_gomb)

        # Ha elfogynak az életeink, a 'kesz' változót igazra állítjuk, vége a játéknak.
        # Később más feltételekt is megadhatunk: lejárhat az idő, vagy éppen nyerhet a játékos
        if self.jatekos_1.eletek == 0:
            self.kesz = True

        # Ha kész, bezárjuk az ablakot. Azért van külön lépésben
        if self.kesz:
            self.close()

    def on_draw(self):
        """
        Ez a függvény is automatikusan hívódik meg. A játék bizonyos időközönként kirajzolja a képernyőt.
        Ide kell befoglalni mindent, amit meg szeretnénk jelentíteni.
        Mindig az arcade.start_render-rel kell kezdeni.
        """
        arcade.start_render()
        self.jelenitsd_meg_a_hatteret()

        self.jatekos_lista.draw()
        self.erme_jelzo_lista.draw()
        self.jelenitsd_meg_az_aranymennyiseget()
        self.eletero_lista.draw()
        self.erme_lista.draw()
        self.kard_lista.draw()
        self.szorny_lista.draw()
        self.lada_lista.draw()
        self.fal_lista.draw()

    def inditas(self):
        self.grafika_init()

        self.eletek_kezdeti_kirajzolasa()

        self.kesz = False  # Ha igaz, vége lesz a játéknak

        # Kezdeti üzenetek kiírása
        udvozlet()

        # Fixen 5 aranyat találunk a játék elején
        self.jatekos_1.aranyat_talal(5)

        # Valójában itt indul el az ismétlődő ciklus
        arcade.run()

        # Ha vége a játéknak
        viszlat(self.jatekos_1.tavolsag, self.jatekos_1.arany)
        kiir_fejlett(self.jatekos_1.targylista)

    def grafika_init(self):

        # Hatter poziciojanak beallitasa
        self.hatter_pozicio_x, self.hatter_pozicio_y = KEP_SZELESSEG / 2, KEP_MAGASSAG / 2
        self.hatter_kep = arcade.load_texture("img/palya.png")

        self.jatekos_sprite_init()

        # Eletero jelzo betoltese
        self.eletero_lista = arcade.SpriteList()

        self.erme_jelzo_init()
        self.erme_sprite_init()
        self.kard_sprite_init()
        self.szorny_sprite_init()
        self.lada_sprite_init()
        self.fal_sprite_init()


    def jatekos_sprite_init(self):
        # Jatekos betoltese
        self.jatekos_lista = arcade.SpriteList()
        self.jatekos_lista.append(self.jatekos_1)
        self.jatekos_lista.append(self.jatekos_2)


    def erme_jelzo_init(self):
        # Erme az erme jelzohoz
        self.erme_jelzo_sprite = arcade.Sprite("img/Coin1.png")
        self.erme_jelzo_sprite.center_x = MEZO_MERET / 2
        self.erme_jelzo_sprite.center_y = KEP_MAGASSAG - 1.5 * MEZO_MERET
        self.erme_jelzo_lista = arcade.SpriteList()
        self.erme_jelzo_lista.append(self.erme_jelzo_sprite)


    def erme_sprite_init(self):
        # Felveheto erme Spriteok
        self.erme_lista = arcade.SpriteList()
        self.erme_lista.append(Erme(3, 5, 2))
        self.erme_lista.append(Erme(12, 7, 7))
        self.erme_lista.append(Erme(13, 2, 13))
        self.erme_lista.append(Erme(7, 8, 5))


    def kard_sprite_init(self):
        # Kard Spriteok
        self.kard_lista = arcade.SpriteList()
        self.kard_lista.append(Kard(12, 5))
        self.kard_lista.append(Kard(3, 7))


    def szorny_sprite_init(self):
        self.szorny_lista = arcade.SpriteList()
        self.szorny_lista.append(Ork(2, 5))
        self.szorny_lista.append(Demon(7, 2))


    def lada_sprite_init(self):
        self.lada_lista = arcade.SpriteList()
        self.lada_lista.append(Lada(4, 5,['balta', 'kard'], True))
        self.lada_lista.append(Lada(11, 7, ['balta', 'páncél'], False))


    def fal_sprite_init(self):
        self.fal_lista = arcade.SpriteList()
        for i in range(4, 15):
            self.fal_lista.append(Fal(i, 11))
            self.fal_lista.append(Fal(i, 3))


    def koordinatak_szamolasa(self, x_mezo, y_mezo):
        x_pixelben = MEZO_MERET * x_mezo + MEZO_MERET / 2
        y_pixelben = MEZO_MERET * y_mezo + MEZO_MERET / 2
        return x_pixelben, y_pixelben

    def mozgasd_a_jatekost(self, megnyomott_gomb):

        # If-elif szerkezettel megvizsgáljuk, hogy a megnyomott gomb valamelyik nyíl-e a négy nyíl közül

        # Ha a lenyomott gomb a balra gomb
        if megnyomott_gomb == arcade.key.LEFT:

            # Ha a jatekos_1 x pozicioja nagyobb, mint a bal határ, vagyis nem a kepernyő bal szélén van
            if self.jatekos_1.center_x > BAL_HATAR:

                # Akkor egy "kockányival" balrább toljuk
                self.jatekos_1.balra_lep(self.fal_lista)

        # Es hasonloan a tobbi nyilra
        elif megnyomott_gomb == arcade.key.RIGHT:
            if self.jatekos_1.center_x < JOBB_HATAR:
                self.jatekos_1.jobbra_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.UP:
            if self.jatekos_1.center_y < FELSO_HATAR:
                self.jatekos_1.felfele_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.DOWN:
            if self.jatekos_1.center_y > ALSO_HATAR:
                self.jatekos_1.lefele_lep(self.fal_lista)

        if megnyomott_gomb == arcade.key.A:
            if self.jatekos_2.center_x > BAL_HATAR:
                self.jatekos_2.balra_lep(self.fal_lista)

        # Es hasonloan a tobbi nyilra
        elif megnyomott_gomb == arcade.key.D:
            if self.jatekos_2.center_x < JOBB_HATAR:
                self.jatekos_2.jobbra_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.W:
            if self.jatekos_2.center_y < FELSO_HATAR:
                self.jatekos_2.felfele_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.S:
            if self.jatekos_2.center_y > ALSO_HATAR:
                self.jatekos_2.lefele_lep(self.fal_lista)

    def update(self, delta_time):
        """ A jatek logikaja jon ide """

        # Legeneraljuk azoknak az ermeknek a listajat, amikre a jatekos_1 ralepett
        # Miert lista, miert nem csak egy erme? Mert lehetne több erme is egy helyen
        for jatekos in self.jatekos_lista:
            erintett_ermek = arcade.check_for_collision_with_list(
                jatekos,
                self.erme_lista)

            # Vegigmegyunk az erintett ermeken, levesszuk oket es megnoveljuk az aranykeszletet
            for erme in erintett_ermek:
                erme.kill()
                Erme.szamlalo -= 1
                jatekos.aranyat_talal(erme.ertek)

            # Ugyanezt megtesszuk a kardokkal
            erintett_kardok = arcade.check_for_collision_with_list(
                jatekos,
                self.kard_lista
            )

            for kard in erintett_kardok:
                jatekos.targyat_talal("kard")
                kard.kill()

            erintett_ladak = arcade.check_for_collision_with_list(
                jatekos,
                self.lada_lista
            )

            for lada in erintett_ladak:
                lada.kifoszt(jatekos)

            jatekos.update()

        if Erme.szamlalo == 0:
            self.kesz = True

    def jelenitsd_meg_a_hatteret(self):
        arcade.draw_texture_rectangle(
            self.hatter_pozicio_x,
            self.hatter_pozicio_y,
            self.hatter_kep.width,
            self.hatter_kep.height,
            self.hatter_kep)

    def jelenitsd_meg_az_aranymennyiseget(self):
        arcade.draw_text(
            str(self.jatekos_1.arany),
            MEZO_MERET,
            KEP_MAGASSAG - 2 * MEZO_MERET,
            arcade.color.WHITE,
            30)

    def eletek_kezdeti_kirajzolasa(self):
        for i in range(self.jatekos_1.eletek):
            uj_elet_sprite = arcade.Sprite("img/heart.png")
            uj_elet_sprite.center_x = i * MEZO_MERET + MEZO_MERET / 2
            uj_elet_sprite.center_y = KEP_MAGASSAG - MEZO_MERET / 2
            self.eletero_lista.append(uj_elet_sprite)

    def uj_elet(self, jatekos):
        uj_elet_sprite = arcade.Sprite("img/heart.png")
        uj_elet_sprite.center_x = self.jatekos_1.eletek * MEZO_MERET + MEZO_MERET / 2
        uj_elet_sprite.center_y = KEP_MAGASSAG - MEZO_MERET / 2
        self.eletero_lista.append(uj_elet_sprite)
        jatekos.eletek += 1

    def veszits_eletet(self):
        utolso_elet = self.eletero_lista[self.eletek - 1]
        utolso_elet.kill()
        self.jatekos_1.eletek -= 1


if __name__ == "__main__":
    jatek = LovagJatek()
    jatek.inditas()
