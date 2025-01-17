import pygame
import re
import json
import numpy as np
import pickle
import math
import random
import time

class Ekran:
    def __init__(self,
                 ekran=None,
                 nazwa="Labirynt APP",
                 wymiary=(1200, 700),
                 obiekty=None,
                 częstotliwość=70,
                 kolor=(255, 255, 255)):
        if obiekty is None:
            obiekty = []
        self.ekran = ekran
        self.nazwa = nazwa
        self.x, self.y = wymiary
        self.obiekty = obiekty
        self.częstotliwość = częstotliwość
        self.kolor = kolor

    def edycja(self, nazwa=None, x=None, y=None, kolor=None, obiekty=None, częstotliwość=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if kolor is not None:
            self.kolor = kolor
        if obiekty is not None:
            self.obiekty = obiekty
        if częstotliwość is not None:
            self.częstotliwość = częstotliwość

    def stwórz(self):
        pygame.init()
        self.ekran = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption(self.nazwa)
        self.ekran.fill(self.kolor)
        pygame.display.update()

        uruchomiony = True
        while uruchomiony:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    uruchomiony = False

        pygame.quit()

    def dodajObiekty(self, obiekt):
        self.obiekty.append(obiekt)
        print(f"Obiekt {obiekt} dodany do ekranu.")

    def usunObiekty(self, obiekt):
        if obiekt in self.obiekty:
            self.obiekty.remove(obiekt)
            print(f"Obiekt {obiekt} usunięty z ekranu.")
        else:
            print(f"Obiekt {obiekt} nie znajduje się na ekranie.")

    def przechwyc_klawisze_i_mysz(self):
        self.klawisze = {}
        self.mysz = {"pozycja": (0, 0), "przyciski": {}}
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    self.klawisze[pygame.key.name(event.key)] = "naciśnięty"
                    print(f"Klawisz {pygame.key.name(event.key)} został naciśnięty.")
                elif event.type == pygame.KEYUP:
                    self.klawisze[pygame.key.name(event.key)] = "zwolniony"
                    print(f"Klawisz {pygame.key.name(event.key)} został zwolniony.")
                elif event.type == pygame.MOUSEMOTION:
                    self.mysz["pozycja"] = event.pos
                    print(f"Mysz poruszyła się na pozycję {self.mysz['pozycja']}.")
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mysz["przyciski"][event.button] = "naciśnięty"
                    print(f"Przycisk myszy {event.button} został naciśnięty na pozycji {self.mysz['pozycja']}.")
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mysz["przyciski"][event.button] = "zwolniony"
                    print(f"Przycisk myszy {event.button} został zwolniony na pozycji {self.mysz['pozycja']}.")

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
        self.szerokość, self.wysokość = polozenie
        self.x, self.y = wymiary
        self.rodzaj = rodzaj
        self.widzialnosc = widzialnosc

    def dodajDoGrupy():
        0

    def usunZgrupy():
        0

class Ustawienia(Obiekt):
    def __init__(self,
                ekran=None,
                grupaObiektów=None,
                nazwa="ustawienia",
                polozenie=(0, 0),
                wymiary=(500, 300),
                kolory={"tło": (255, 255, 255)},
                rodzaj="Funkcjonalne",
                widzialnosc=True
                ):
        super().__init__(ekran, grupaObiektów, nazwa, wymiary, rodzaj, widzialnosc)
        self.kolory = kolory
        self.szerokość, self.wysokość = wymiary
        self.x, self.y = polozenie

    def edycja(self, nazwa=None, x=None, y=None, szerokość=None, wysokość=None, kolory=None, rodzaj=None, widzialnosc=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if szerokość is not None:
            self.szerokość = szerokość
        if wysokość is not None:
            self.wysokość = wysokość
        if kolory is not None:
            self.kolory = kolory
        if rodzaj is not None:
            self.rodzaj = rodzaj
        if widzialnosc is not None:
            self.widzialnosc = widzialnosc

    def dodajDoGrupy():
        0

    def stwórz():
        0

class Przycisk(Obiekt):
    def __init__(self,
                ekran=None,
                grupaObiektów=None,
                nazwa="podstawowy",
                polozenie=(0, 0),
                wymiary=(100, 100),
                kolor=(),
                rodzaj="Przycisk",
                widzialnosc=True,
                CzyKliknięty=False,
                Jasność=0
                ):
        super().__init__(ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
        self.CzyKliknięty = CzyKliknięty
        self.Jasność = Jasność
        self.kolor = kolor
        self.x, self.y = polozenie
        self.szerokość, self.wysokość = wymiary

    def edycja(self, nazwa=None, x=None, y=None, szerokość=None, wysokość=None, kolor=None, rodzaj=None, widzialnosc=None, CzyKliknięty=None, Jasność=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if szerokość is not None:
            self.szerokość = szerokość
        if wysokość is not None:
            self.wysokość = wysokość
        if kolor is not None:
            self.kolor = kolor
        if rodzaj is not None:
            self.rodzaj = rodzaj
        if widzialnosc is not None:
            self.widzialnosc = widzialnosc
        if CzyKliknięty is not None:
            self.CzyKliknięty = CzyKliknięty
        if Jasność is not None:
            self.Jasność = Jasność

    def dodajDoGrupy():
        0

    def stwórz():
        0

    def JakKliknięty():
        0

class Napis(Przycisk):
    def __init__(self,
                ekran=None,
                grupaObiektów=None,
                nazwa="podstawowy",
                polozenie=(0, 0),
                wymiary=(100, 100),
                kolorNapisu=(0, 0, 0),
                kolor=(255, 255, 255),
                rodzaj="Przycisk",
                widzialnosc=True,
                CzyKliknięty=False,
                Jasność=0
                ):

        Przycisk.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, kolor, rodzaj, widzialnosc, CzyKliknięty, Jasność)
        self.kolorNapisu = kolorNapisu
        self.x, self.y = polozenie
        self.szerokość, self.wysokość = wymiary

    def edycja(self, nazwa=None, x=None, y=None, szerokość=None, wysokość=None, kolorNapisu=None, kolor=None, rodzaj=None, widzialnosc=None, CzyKliknięty=None, Jasność=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if szerokość is not None:
            self.szerokość = szerokość
        if wysokość is not None:
            self.wysokość = wysokość
        if rodzaj is not None:
            self.rodzaj = rodzaj
        if widzialnosc is not None:
            self.widzialnosc = widzialnosc

        if kolor is not None:
            self.kolor = kolor
        if CzyKliknięty is not None:
            self.CzyKliknięty = CzyKliknięty
        if Jasność is not None:
            self.Jasność = Jasność
        
        if kolorNapisu is not None:
            self.kolorNapisu = kolorNapisu

    def dodajDoGrupy():
        0

    def stwórz():
        0

    def JakKliknięty():
        0

class Scroll(Przycisk):
    def __init__(self, 
                 ekran=None, 
                 grupaObiektów=None, 
                 nazwa="Scroll", 
                 polozenie=(0, 0), 
                 wymiaryScrolla=(10, 250),
                 wymiaryPrzycisku=(5, 5),
                 kolory=None,
                 rodzaj="Przycisk", 
                 widzialnosc=True,
                 max_scroll=200
                 ):

        if kolory is None:
            kolory = {
                "scroll": (0, 0, 0),
                "tło": (0, 0, 0)
            }

        super().__init__(ekran, grupaObiektów, nazwa, polozenie, wymiaryScrolla, rodzaj, widzialnosc)
        self.x, self.y = polozenie
        self.szerScrolla, self.wysScrolla = wymiaryScrolla
        self.szerPrzycisku, self.wysPrzycisku = wymiaryPrzycisku

        self.kolory = kolory
        self.max_scroll = max_scroll
        self.obecna_pozycja = 0

    def edycja(self,
               nazwa=None,
               x=None,
               y=None,
               szerScrolla=None,
               wysScrolla=None,
               szerPrzycisku=None,
               wysPrzycisku=None,
               kolory=None,
               max_scroll=None,
               widzialnosc=None
               ):

        if nazwa is not None:
            self.nazwa = nazwa
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if szerScrolla is not None:
            self.szerScrolla = szerScrolla
        if wysScrolla is not None:
            self.wysScrolla = wysScrolla
        if szerPrzycisku is not None:
            self.szerPrzycisku = szerPrzycisku
        if wysPrzycisku is not None:
            self.wysPrzycisku = wysPrzycisku
        if kolory is not None:
            self.kolory = kolory
        if max_scroll is not None:
            self.max_scroll = max_scroll
        if widzialnosc is not None:
            self.widzialnosc = widzialnosc

    def dodajDoGrupy():
        0

    def stwórz():
        0

    def JakKliknięty():
        0

    def ruch():
        0
    
class GeneratorLabiryntu:
    def __init__(self, 
                wymiaryKratkowe=(20, 20), 
                obiekty=None,
                labirynt=None
                ):
        if obiekty is None:
            obiekty = {
                "ścieżki": [],
                "ściany": [],
                "bonusy": [],
            }
        if labirynt is None:
            labirynt = []
        self.szerokość, self.wysokość = wymiaryKratkowe
        self.obiekty = obiekty
        self.labirynt = labirynt

    def edycja(self, szerokość=None, wysokość=None, obiekty=None, labirynt=None):
        if szerokość is not None:
            self.szerokość = szerokość
        if wysokość is not None:
            self.wysokość = wysokość
        if obiekty is not None:
            self.obiekty = obiekty
        if labirynt is not None:
            self.labirynt = labirynt

    def generuj(self):
        self.labirynt = np.zeros(((self.szerokość * 2 + 1), (self.wysokość * 2 + 1)))
        print(self.labirynt)

    def dodajDoGrupy(self):
        pass

    def stwórz(self):
        pass
    #   #####
    #   s @ #
    #   #@#@#
    #   # @ m
    #   #####  (0, "#"), (1, " "), (2, "@"), (3, "s"), (4, "m")

class Labirynt(Obiekt, GeneratorLabiryntu):
    def __init__(self,
                ekran,
                grupaObiektów,
                nazwa="podstawowy",
                polozenie=(0, 0),
                wymiary=(100, 100),
                rodzaj="Przycisk",
                widzialnosc=True,
                wymiaryKratkowe=(20, 20),
                obiekty_labiryntu=None
                ):
        Obiekt.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
        GeneratorLabiryntu.__init__(self, wymiaryKratkowe, obiekty_labiryntu)
        self.x, self.y = polozenie
        self.szerokość, self.wysokość = wymiary
        self.szerLabiryntKrat, self.wysLabiryntKrat = wymiaryKratkowe

    def edycja(self,
               nazwa=None,
               x=None,
               y=None,
               szerokość=None,
               wysokość=None,
               rodzaj=None,
               widzialnosc=None,
               szerLabiryntKrat=None,
               wysLabiryntKrat=None,
               obiekty_labiryntu=None
               ):
        if nazwa is not None:
            self.nazwa = nazwa
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if szerokość is not None:
            self.szerokość = szerokość
        if wysokość is not None:
            self.wysokość = wysokość
        if rodzaj is not None:
            self.rodzaj = rodzaj
        if widzialnosc is not None:
            self.widzialnosc = widzialnosc
        if szerLabiryntKrat is not None:
            self.szerLabiryntKrat = szerLabiryntKrat
        if wysLabiryntKrat is not None:
            self.wysLabiryntKrat = wysLabiryntKrat
        if obiekty_labiryntu is not None:
            self.obiekty = obiekty_labiryntu

    def dodajDoGrupy(self):
        pass

    def stwórz(self):
        pass

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

    def edycja(self, pliki=None, dane=None):
        if pliki is not None:
            self.pliki.update(pliki)
        if dane is not None:
            self.dane.update(dane)

    def pobierz(self):
        pass

    def usuń(self):
        pass

    def reset(self):
        pass

class Użytkownik(Pamięć):
    def __init__(self, pliki=None, dane=None):
        super().__init__(pliki, dane)

    def edycja(self, pliki=None, dane=None):
        if pliki is None:
            pliki = {"txt": None, "json": None}
        if dane is None:
            dane = {}
        super().edycja(pliki, dane)

    def stwórz(self):
        pass

    def zaloguj(self):
        pass

    def wyloguj(self):
        pass

class Gracz(Obiekt, Użytkownik):
    def __init__(self,
                ekran=None,
                grupaObiektów=None,
                nazwa="podstawowy",
                polozenie=(0, 0),
                wymiary=(100, 100),
                kolorObramowanie=(255, 0, 0),
                kolorŚrodek=(0, 0, 255),
                obramowaniePx=3,
                rodzaj="Przycisk",
                widzialnosc=True,
                pliki=None,
                dane=None,
                wymiary_labiryntu=(20, 20),
                obiekty_labiryntu=None
                ):
    
        Obiekt.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
        Użytkownik.__init__(self, pliki, dane)

        self.x, self.y = polozenie
        self.szerokość, self.wysokość = wymiary

        self.szerLabiryntKrat, self.wysLabiryntKrat = wymiary_labiryntu
        self.obiekty_labiryntu = obiekty_labiryntu
        self.labirynt = None

        self.generator_labiryntu = GeneratorLabiryntu(
            wymiaryKratkowe=wymiary_labiryntu,
            obiekty=obiekty_labiryntu
        )
        self.kolorObramowanie = kolorObramowanie
        self.kolorŚrodek = kolorŚrodek
        self.obramowaniePx = obramowaniePx
    
    def generuj_labirynt(self):
        self.labirynt = self.generator_labiryntu.generuj()

    def edycja(self,
               nazwa=None,
               x=None,
               y=None,
               szerokość=None,
               wysokość=None,
               kolorObramowanie=None,
               kolorŚrodek=None,
               pliki=None,
               dane=None,
               szerLabiryntKrat=None,
               wysLabiryntKrat=None,
               obiekty_labiryntu=None):

        if nazwa is not None:
            self.nazwa = nazwa
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if szerokość is not None:
            self.szerokość = szerokość
        if wysokość is not None:
            self.wysokość = wysokość
        if kolorObramowanie is not None:
            self.kolorObramowanie = kolorObramowanie
        if kolorŚrodek is not None:
            self.kolorŚrodek = kolorŚrodek
        if pliki is not None:
            self.pliki = pliki
        if dane is not None:
            self.dane = dane
        if szerLabiryntKrat is not None:
            self.szerLabiryntKrat = szerLabiryntKrat
        if wysLabiryntKrat is not None:
            self.wysLabiryntKrat = wysLabiryntKrat
        if obiekty_labiryntu is not None:
            self.obiekty_labiryntu = obiekty_labiryntu
        if szerLabiryntKrat is not None:
            self.szerLabiryntKrat = szerLabiryntKrat
        if wysLabiryntKrat is not None:
            self.wysLabiryntKrat = wysLabiryntKrat
        if obiekty_labiryntu is not None:
            self.obiekty_labiryntu = obiekty_labiryntu
    def dodajDoGrupy(self, grupa):
        if grupa and self not in grupa:
            grupa.add(self)

    def usunZgrupy(self, grupa):
        if grupa and self in grupa:
            grupa.remove(self)

    def stwórz(self):
        print(f"Tworzenie gracza {self.nazwa} na pozycji ({self.x}, {self.y}) z wymiarami {self.szerokość}x{self.wysokość}")

    def ruch(self, kierunek):
        if kierunek == "góra":
            self.y -= 1
        elif kierunek == "dół":
            self.y += 1
        elif kierunek == "lewo":
            self.x -= 1
        elif kierunek == "prawo":
            self.x += 1
        print(f"Gracz {self.nazwa} przesunął się na ({self.x}, {self.y})")

def test_gracz():
    gracz = Gracz(
        nazwa="Testowy Gracz",
        polozenie=(2, 3),
        wymiary=(50, 50),
        wymiary_labiryntu=(10, 10),
        obiekty_labiryntu={"ścieżki": [(1, 1)], "ściany": [(0, 0)], "bonusy": [(2, 2)]},
    )

    print("Stan początkowy gracza:")
    print(f"Nazwa: {gracz.nazwa}")
    print(f"Położenie: ({gracz.x}, {gracz.y})")
    print(f"Wymiary: ({gracz.szerokość}, {gracz.wysokość})")
    print(f"Wymiary labiryntu: ({gracz.szerLabiryntKrat}x{gracz.wysLabiryntKrat})")
    print(f"Obiekty labiryntu: {gracz.obiekty_labiryntu}")

    print("\nGenerowanie labiryntu:")
    gracz.generuj_labirynt()
    print("Wygenerowany labirynt:")
    print(gracz.labirynt)

    print("\nEdycja gracza:")
    gracz.edycja(nazwa="Nowy Gracz", x=5, y=5, szerokość=60, wysokość=60)
    print("Po edycji:")
    print(f"Nazwa: {gracz.nazwa}")
    print(f"Położenie: ({gracz.x}, {gracz.y})")
    print(f"Wymiary: ({gracz.szerokość}, {gracz.wysokość})")

    print("\nRuch gracza:")
    gracz.ruch("prawo")
    gracz.ruch("dół")
    print(f"Po ruchach: ({gracz.x}, {gracz.y})")

test_gracz()

def test_uzytkownik():
    # Tworzymy obiekt Użytkownik z początkowymi wartościami
    uzytkownik = Użytkownik(pliki={"txt": "plik1.txt", "json": "plik2.json"}, dane={"nazwa": "Janek", "wiek": 25})
    
    # Wypisanie początkowego stanu
    print(f"Stan początkowy użytkownika:")
    print(f"Pliki: {uzytkownik.pliki}")
    print(f"Dane: {uzytkownik.dane}")
    
    # Edycja danych użytkownika
    print("\nEdycja danych użytkownika:")
    uzytkownik.edycja(pliki={"txt": "plik3.txt", "json": "plik4.txt"}, dane={"nazwa": "Marek", "wiek": 30})
    print(f"Po edycji:")
    print(f"Pliki: {uzytkownik.pliki}")
    print(f"Dane: {uzytkownik.dane}")

test_uzytkownik()

def test_pamiec():
    pamiec = Pamięć()

    print("Stan początkowy pamięci:")
    print(f"Pliki: {pamiec.pliki}")
    print(f"Dane: {pamiec.dane}")

    print("\nEdycja danych w pamięci:")
    pamiec.edycja(
        pliki={"txt": "dokument1.txt", "json": "config.json"},
        dane={
            "Ustawienia": {"Gracz": ["Janek"], "Labirynt": ["Level1"], "PoziomTrudności": 2},
            "Labirynt": 1,
            "Level": 1
        }
    )
    print("Po edycji:")
    print(f"Pliki: {pamiec.pliki}")
    print(f"Dane: {pamiec.dane}")

    print("\nTestowanie metody pobierz():")
    pamiec.pobierz()

    print("\nTestowanie metody usuń():")
    pamiec.usuń()

    print("\nTestowanie metody reset():")
    pamiec.reset()

test_pamiec()

def test_labirynt():
    ekran = None
    grupaObiektów = None

    labirynt = Labirynt(ekran, grupaObiektów, nazwa="Labirynt Testowy", polozenie=(5, 5), wymiary=(200, 200))

    print("Stan początkowy labiryntu:")
    print(f"Nazwa: {labirynt.nazwa}")
    print(f"Polożenie: ({labirynt.x}, {labirynt.y})")
    print(f"Wymiary: ({labirynt.szerokość}, {labirynt.wysokość})")
    print(f"Wymiary kratkowe: ({labirynt.szerLabiryntKrat}, {labirynt.wysLabiryntKrat})")

    print("\nEdycja labiryntu:")
    labirynt.edycja(
        nazwa="Nowy Labirynt",
        x=10,
        y=10,
        szerokość=300,
        wysokość=300,
        szerLabiryntKrat=30,
        wysLabiryntKrat=30
    )
    print("Po edycji:")
    print(f"Nazwa: {labirynt.nazwa}")
    print(f"Polożenie: ({labirynt.x}, {labirynt.y})")
    print(f"Wymiary: ({labirynt.szerokość}, {labirynt.wysokość})")
    print(f"Wymiary kratkowe: ({labirynt.szerLabiryntKrat}, {labirynt.wysLabiryntKrat})")

    print("\nTestowanie metody dodajDoGrupy():")
    labirynt.dodajDoGrupy()

    print("\nTestowanie metody stwórz():")
    labirynt.stwórz()

test_labirynt()

def test_generator_labiryntu():
    generator = GeneratorLabiryntu(wymiaryKratkowe=(10, 10), obiekty={"ścieżki": [(1, 1)], "ściany": [(0, 0)], "bonusy": [(2, 2)]})

    print("Stan początkowy generatora labiryntu:")
    print(f"Wymiary kratkowe: ({generator.szerokość}, {generator.wysokość})")
    print(f"Obiekty: {generator.obiekty}")
    print(f"Labirynt: {generator.labirynt}")

    print("\nEdycja generatora labiryntu:")
    generator.edycja(
        szerokość=15,
        wysokość=15,
        obiekty={"ścieżki": [(3, 3)], "ściany": [(1, 1)], "bonusy": [(4, 4)]},
        labirynt=[[1, 1], [0, 1]]
    )

    print("Po edycji generatora:")
    print(f"Wymiary kratkowe: ({generator.szerokość}, {generator.wysokość})")
    print(f"Obiekty: {generator.obiekty}")
    print(f"Labirynt: {generator.labirynt}")

    print("\nTestowanie metody generuj():")
    generator.generuj()

    print("\nTestowanie metody dodajDoGrupy():")
    generator.dodajDoGrupy()

    print("\nTestowanie metody stwórz():")
    generator.stwórz()

test_generator_labiryntu()