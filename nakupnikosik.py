class NakupniKosik:
    def __init__(self):
        self.polozky_kosiku = []
        self.dostupne_nabidky = ["banán", "jablko", "pomeranč"]

    def pridat_polozku(self, index_polozky):
        if 0 <= index_polozky < len(self.dostupne_nabidky):
            polozka = self.dostupne_nabidky.pop(index_polozky)
            self.polozky_kosiku.append(polozka)
            print(f"{polozka.capitalize()} byl přidán do košíku.")
        else:
            print("Neplatný index položky.")

    def zobrazit_nabidky(self):
        print("Dostupné nabídky:")
        for index, polozka in enumerate(self.dostupne_nabidky):
            print(f"{index}: {polozka.capitalize()}")

    def zobrazit_kosik(self):
        if not self.polozky_kosiku:
            print("Váš košík je prázdný.")
        else:
            print("----Váš košík---:")
            for polozka in self.polozky_kosiku:
                print(f"- {polozka.capitalize()}")

    def zaplatit(self):
        print("Děkujeme za nákup!")



print("Vítejte v naší terminálové aplikaci pro nákupy!")
print("Přidávejte položky do košíku zadáním odpovídajícího čísla.")
print("Začněme!")


kosik = NakupniKosik()


while True:
    kosik.zobrazit_nabidky()

    if not kosik.dostupne_nabidky:
        print("Nabídka je prázdná.")
        break

    kosik.zobrazit_kosik()

    uzivatelsky_vstup = input("----Zadejte číslo položky k přidání do košíku (nebo 'q' pro ukončení)----: ")
    if uzivatelsky_vstup.lower() == 'q':
        break

    try:
        index_polozky = int(uzivatelsky_vstup)
        kosik.pridat_polozku(index_polozky)
    except ValueError:
        print("Neplatný vstup. Zadejte číslo položky.")

kosik.zaplatit()

