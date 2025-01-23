from typing import Optional, Dict, List, Tuple
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
                 ekran,
                 nazwa="Labirynt APP",
                 wymiary=(1200, 700),
                 obiekty: Optional[List] = None,
                 częstotliwość=70,
                 kolor: Tuple[int, int, int] = (255, 255, 255)):
        if obiekty is None:
            obiekty = []
        self.ekran = ekran
        self.nazwa = nazwa
        self.x, self.y = wymiary
        self.obiekty = obiekty
        self.częstotliwość = częstotliwość
        self.kolor = kolor

    def edycja(self, 
               nazwa: Optional[str] = None, 
               x: int = None, 
               y: int = None, 
               kolor: Tuple[int, int, int] = None, 
               obiekty: List = None, 
               częstotliwość: int = None):
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
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return
                case pygame.KEYDOWN:
                    self.klawisze[pygame.key.name(event.key)] = "naciśnięty"
                    print(f"Klawisz {pygame.key.name(event.key)} został naciśnięty.")
                case pygame.KEYUP:
                    self.klawisze[pygame.key.name(event.key)] = "zwolniony"
                    print(f"Klawisz {pygame.key.name(event.key)} został zwolniony.")
                case pygame.MOUSEMOTION:
                    self.mysz["pozycja"] = event.pos
                    print(f"Mysz poruszyła się na pozycję {self.mysz['pozycja']}.")
                case pygame.MOUSEBUTTONDOWN:
                    self.mysz["przyciski"][event.button] = "naciśnięty"
                    print(f"Przycisk myszy {event.button} został naciśnięty na pozycji {self.mysz['pozycja']}.")
                case pygame.MOUSEBUTTONUP:
                    self.mysz["przyciski"][event.button] = "zwolniony"
                    print(f"Przycisk myszy {event.button} został zwolniony na pozycji {self.mysz['pozycja']}.")

class ElementInterfejsu:
    def __init__(self, 
                 ekran=None,
                 grupaObiektów: Optional[Dict[str, List]] = None,
                 nazwaObiektu: str = "podstawowy",
                 polozenie: Tuple[int, int] = (0, 0), 
                 wymiary: Tuple[int, int] = (100, 100),
                 rodzaj: str = "Przycisk",
                 widzialnosc: bool = True
                 ):
        self.ekran = ekran
        self.grupaObiektów = grupaObiektów if grupaObiektów is not None else {}
        self.nazwaObiektu = nazwaObiektu
        self.x, self.y = polozenie
        self.szerokość, self.wysokość = wymiary
        self.rodzaj = rodzaj
        self.widzialnosc = widzialnosc

    def dodajDoGrupy(self, nazwaObiektu: str, obiekt):
        """Dodaj obiekt do grupy obiektów o danej nazwie."""
        if nazwaObiektu not in self.grupaObiektów:
            self.grupaObiektów[nazwaObiektu] = []
        self.grupaObiektów[nazwaObiektu].append(obiekt)

    def usunZgrupy(self, nazwa: str):
        """Usuń grupę obiektów o podanej nazwie."""
        if nazwa in self.grupaObiektów:
            del self.grupaObiektów[nazwa]

    def rysuj_Ustawienia(self):
        0

    def rysuj(self, nazwaObiektu):
        """Logika wyboru co rysować na podstawie nazwy obiektu."""
        if not self.widzialnosc:
            return  # Obiekt ukryty, nic nie rysujemy
        
        match nazwaObiektu:
            case "przycisk":
                0
            case "ustawienia":
                0
            case "napis":
                0
            case "scroll":
                0

        if nazwaObiektu == "przycisk":
            print("Rysuję przycisk: Prostokąt z tekstem lub ikoną.")
            # Możesz oddelegować do innej metody np. `rysuj_przycisk()`

class Ustawienia(ElementInterfejsu):
    def __init__(self,
                ekran=None,
                grupaObiektów: Optional[list] = None,
                nazwa: str = "ustawienia",
                polozenie: Tuple[int, int] = (0, 0),
                wymiary:Tuple[int, int] = (500, 300),
                kolory={"tło": (255, 255, 255)},
                rodzaj="Funkcjonalne",
                widzialnosc=True,
                obiektyMenu: Optional[List[Dict[str, List]]] = None
                ):
        super().__init__(ekran, grupaObiektów, nazwa, wymiary, rodzaj, widzialnosc)
        self.kolory = kolory
        self.szerokość, self.wysokość = wymiary
        self.x, self.y = polozenie
        self.obiektyMenu = obiektyMenu

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

    def dodajDoGłównejGrupy(self, nazwa):
        warstwa = len(self.obiektyMenu)
        x, y = 100, 100 * (warstwa - 1) + 100 * warstwa
        self.obiektyMenu.append

    def dodajDoGłównejGrupy(self, nazwa: str):
        """Dodaje nowy obiekt do głównej grupy obiektów menu."""
        if self.obiektyMenu is None:
            self.obiektyMenu = []

        # Oblicz pozycję nowego obiektu w zależności od warstwy.
        warstwa = len(self.obiektyMenu)
        x = 100
        y = 100 * (warstwa - 1) + 100 * warstwa
        nowy_obiekt = {
            "nazwa": nazwa,
            "pozycja": (x, y),
            "warstwa": warstwa
        }

        # Dodaj obiekt do listy `obiektyMenu`.
        self.obiektyMenu.append(nowy_obiekt)

        print(f"Dodano obiekt '{nazwa}' do głównej grupy na pozycji: {x}, {y}.")

    def dodajDoGrupy(self, obiekt):
        ElementInterfejsu.dodajDoGrupy(obiekt)

    def stwórz():
        0
        #rysowanie


class Przycisk(ElementInterfejsu):
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
    def __init__(self, wymiaryKratkowe=(20, 20), obiekty=None):
        if obiekty is None:
            obiekty = {
                "ścieżki": [],
                "ściany": [],
                "bonusy": [],
            }
        szerokość, wysokość = wymiaryKratkowe
        self.szerokość, self.wysokość = szerokość * 2 + 1, wysokość * 2 + 1
        self.obiekty = obiekty
        self.labirynt = np.ones((self.wysokość, self.szerokość), dtype=int)

    def generuj(self):
        def dfs(x, y):
            kierunki = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(kierunki)
            for dx, dy in kierunki:
                nx, ny = x + dx, y + dy

                if 0 <= nx < (self.szerokość // 2) and 0 <= ny < (self.wysokość // 2) and self.labirynt[ny * 2 + 1][nx * 2 + 1] == 1:
                    self.labirynt[y * 2 + 1 + dy][x * 2 + 1 + dx] = 0
                    self.labirynt[ny * 2 + 1][nx * 2 + 1] = 0

                    self.obiekty["ścieżki"].append((ny, nx))

                    dfs(nx, ny)

        self.labirynt.fill(1)
        self.obiekty = {"ścieżki": [], "ściany": [], "bonusy": []}

        self.labirynt[1][1] = 0
        self.obiekty["ścieżki"].append((1, 1))
        self.labirynt[self.wysokość - 2][self.szerokość - 2] = 0
        self.obiekty["ścieżki"].append((self.wysokość - 2, self.szerokość - 2))

        dfs(0, 0)

        self.dodaj_bonusy()

        for i in range(self.wysokość):
            for j in range(self.szerokość):
                if self.labirynt[i][j] == 1:
                    self.obiekty["ściany"].append((i, j))

        PunktStart = (1, 1)
        self.labirynt[self.wysokość - 2, self.szerokość - 2] = 4
        self.labirynt[self.wysokość - 3, self.szerokość - 2] = 0

    def dodaj_bonusy(self, częstotliwość=0.07):
        wolne_punkty = [(i, j) for i in range(self.wysokość) for j in range(self.szerokość) if self.labirynt[i][j] == 0]
        liczba_bonusów = round(len(wolne_punkty) * częstotliwość)

        kordyBonusów = random.sample(wolne_punkty, liczba_bonusów)
        for x, y in kordyBonusów:
            self.labirynt[x][y] = 2
            self.obiekty["bonusy"].append((x, y))

        print(f"Dodano {liczba_bonusów} bonusów w miejscach: {kordyBonusów}")

    def SprawdzPrzejscie(mapa,
                        PunktStart: Tuple[int, int] = (1, 1),
                        PunktMeta: Optional[Tuple[int, int]] = None,
                        RodzajŚciany: Optional[str] = None,
                        RodzajTrasy: Optional[str] = None,
                        WymaganePunkty: List[Tuple[int, int]] = []
                        ) -> bool:
        
        def ZnajdzSasiadow(x: int, y: int, unikajPól: Optional[List[Tuple[int, int]]] = None) -> List[Tuple[int, int]]:
            if unikajPól is None:
                unikajPól = []
                
            kierunki = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            sasiedzi = []
            for a, b in kierunki:
                nx, ny = x + a, y + b
                if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]):
                    blok = mapa[nx][ny]
                    if blok == RodzajŚciany and (nx, ny) not in unikajPól:
                        sasiedzi.append((nx, ny))
            return sasiedzi

        def AlgorytmDfs(Trasy: Optional[List[List[Tuple[int, int]]]] = None) -> List[List[Tuple[int, int]]]:
            0

        def SprawdzCzyTrasaWymagaPunkty(trasa: List[Tuple[int, int]], wymaganePunkty: List[Tuple[int, int]]) -> bool:
            0# Przejdzie przez każdą trase i na początku weźmie te co przechodzą przez punkty
            0# a potem weźmie tą co jest najkrótsza


    def wypisz(self):
        for wiersz in self.labirynt:
            print("".join(str(rzad) for rzad in wiersz))

    def zwróć_labirynt(self):
        return self.labirynt
    
class Labirynt(ElementInterfejsu, GeneratorLabiryntu):
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
        ElementInterfejsu.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
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

class Gracz(ElementInterfejsu, Użytkownik):
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
    
        ElementInterfejsu.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
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

generator = GeneratorLabiryntu(wymiaryKratkowe=(10, 10))

generator.generuj()

generator.dodaj_bonusy()

labirynt = generator.zwróć_labirynt()
print("\nZwrócony labirynt:")
for wiersz in labirynt:
    print(wiersz)