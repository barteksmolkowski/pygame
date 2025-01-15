class Ekran:
    def __init__(self,
                nazwa="Labirynt APP",
                wymiary=(1200, 700),
                obiekty=None,
                częstotliwość=70,
                kolor=(255, 255, 255)
                ):
        if obiekty is None:
            obiekty = []
        self.nazwa = nazwa
        self.wymiary = wymiary
        self.obiekty = obiekty
        self.częstotliwość = częstotliwość
        self.kolor = kolor


class Obiekt:
    def __init__(self, 
                ekran=None,
                grupaObiektów=None,
                nazwa="podstawowy",
                polozenie=(0, 0), 
                wymiary=(100, 100),
                rodzaj="Przycisk",
                widzialnosc=True
                ):
        self.ekran = ekran
        self.grupaObiektów = grupaObiektów
        self.nazwa = nazwa
        self.polozenie = polozenie
        self.wymiary = wymiary
        self.rodzaj = rodzaj
        self.widzialnosc = widzialnosc


class Ustawienia(Obiekt):
    def __init__(self,
                ekran=None,
                grupaObiektów=None,
                nazwa="ustawienia",
                polozenie=(0, 0),
                wymiary=(500, 300),
                rodzaj="Funkcjonalne",
                widzialnosc=True
                ):
        super().__init__(ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)


class Przycisk(Obiekt):
    def __init__(self,
                ekran=None,
                grupaObiektów=None,
                nazwa="podstawowy",
                polozenie=(0, 0),
                wymiary=(100, 100), 
                rodzaj="Przycisk",
                widzialnosc=True,
                CzyKliknięty=False,
                Jasność=0
                ):
        super().__init__(ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
        self.CzyKliknięty = CzyKliknięty
        self.Jasność = Jasność


class GeneratorLabiryntu:
    def __init__(self, 
                wymiary=(20, 20), 
                obiekty=None
                ):
        if obiekty is None:
            obiekty = {
                "ścieżki": [],
                "ściany": [],
                "bonusy": [],
            }
        self.wymiary = wymiary
        self.obiekty = obiekty


class Labirynt(Obiekt, GeneratorLabiryntu):
    def __init__(self,
                ekran,
                grupaObiektów,
                nazwa="podstawowy",
                polozenie=(0, 0),
                wymiary=(100, 100),
                rodzaj="Przycisk",
                widzialnosc=True,
                wymiary_labiryntu=(20, 20),
                obiekty_labiryntu=None
                ):
        Obiekt.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
        GeneratorLabiryntu.__init__(self, wymiary_labiryntu, obiekty_labiryntu)


class Pamięć:
    def __init__(self,
                 pliki=None,
                 dane=None
                 ):
        if pliki is None:
            pliki = {"txt": None, "json": None}
        if dane is None:
            dane = {
                "Ustawienia": {
                    "Gracz": [], 
                    "Labirynt": [], 
                    "PoziomTrudności": 0
                },
                "Labirynt": 0,
                "Level": 0
            }
        self.pliki = pliki
        self.dane = dane


class Użytkownik(Pamięć):
    def __init__(self,
                pliki=None,
                dane=None
                ):
        super().__init__(pliki, dane)


class Gracz(Obiekt, Użytkownik, Labirynt):
    def __init__(self,
                ekran=None,
                grupaObiektów=None,
                nazwa="podstawowy",
                polozenie=(0, 0),
                wymiary=(100, 100),
                rodzaj="Przycisk",
                widzialnosc=True,
                pliki=None,
                dane=None,
                wymiary_labiryntu=(20, 20),
                obiekty_labiryntu=None
                ):
        Użytkownik.__init__(self, pliki, dane)
        Labirynt.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc, wymiary_labiryntu, obiekty_labiryntu)
        Obiekt.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
