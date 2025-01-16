import pygame
import re
import json
import numpy
import pickle
import math
import random

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

    def edycja(self, nazwa=None, wymiary=None, kolor=None, obiekty=None, częstotliwość=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if wymiary is not None:
            self.wymiary = wymiary
        if kolor is not None:
            self.kolor = kolor
        if obiekty is not None:
            self.obiekty = obiekty
        if częstotliwość is not None:
            self.częstotliwość = częstotliwość

    def stwórz():
        0

    def dodajObiekty():
        0

    def usunObiekty():
        0

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
        super().__init__(ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
        self.kolory = kolory

    def edycja(self, nazwa=None, polozenie=None, wymiary=None, kolory=None, rodzaj=None, widzialnosc=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if polozenie is not None:
            self.polozenie = polozenie
        if wymiary is not None:
            self.wymiary = wymiary
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

    def edycja(self, nazwa=None, polozenie=None, wymiary=None, kolor=None, rodzaj=None, widzialnosc=None, CzyKliknięty=None, Jasność=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if polozenie is not None:
            self.polozenie = polozenie
        if wymiary is not None:
            self.wymiary = wymiary
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

class Napis(Obiekt, Przycisk):
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
        Obiekt.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
        Przycisk.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, kolor, rodzaj, widzialnosc, CzyKliknięty, Jasność)
        self.kolorNapisu = kolorNapisu

    def edycja(self, nazwa=None, polozenie=None, wymiary=None, kolorNapisu=None, kolor=None, rodzaj=None, widzialnosc=None, CzyKliknięty=None, Jasność=None):
        
        if nazwa is not None:
            self.nazwa = nazwa
        if polozenie is not None:
            self.polozenie = polozenie
        if wymiary is not None:
            self.wymiary = wymiary
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

        self.wymiaryScrolla = wymiaryScrolla
        self.wymiaryPrzycisku = wymiaryPrzycisku
        self.kolory = kolory
        self.max_scroll = max_scroll
        self.obecna_pozycja = 0

    def edycja(self, nazwa=None, polozenie=None, wymiaryScrolla=None, wymiaryPrzycisku=None, kolory=None, max_scroll=None, widzialnosc=None):

        if nazwa is not None:
            self.nazwa = nazwa
        if polozenie is not None:
            self.polozenie = polozenie
        if wymiaryScrolla is not None:
            self.wymiaryScrolla = wymiaryScrolla
        if wymiaryPrzycisku is not None:
            self.wymiaryPrzycisku = wymiaryPrzycisku
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

    def edycja(self, wymiary=None, obiekty=None):
        if wymiary is not None:
            self.wymiary = wymiary
        
        if obiekty is not None:
            self.obiekty = obiekty

    def generuj():
        0

    def dodajDoGrupy():
        0

    def stwórz():
        0

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

    def edycja(self, nazwa=None, polozenie=None, wymiary=None, rodzaj=None, widzialnosc=None, wymiary_labiryntu=None, obiekty_labiryntu=None):

        if nazwa is not None:
            self.nazwa = nazwa
        if polozenie is not None:
            self.polozenie = polozenie
        if wymiary is not None:
            self.wymiary = wymiary
        if rodzaj is not None:
            self.rodzaj = rodzaj
        if widzialnosc is not None:
            self.widzialnosc = widzialnosc

        if wymiary_labiryntu is not None:
            self.wymiary = wymiary_labiryntu
        if obiekty_labiryntu is not None:
            self.obiekty = obiekty_labiryntu

    def dodajDoGrupy():
        0

    def stwórz():
        0

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

    def pobierz():
        0

    def usuń():
        0

    def reset():
        0

class Użytkownik(Pamięć):
    def __init__(self,
                 pliki=None,
                 dane=None
                 ):

        super().__init__(pliki, dane)

    def edycja(self, pliki=None, dane=None):
        super().edycja(pliki, dane)

    def stwórz():
        0

    def zaloguj():
        0

    def wyloguj():
        0

class Gracz(Obiekt, Użytkownik, Labirynt):
    def __init__(self,
                ekran=None,
                grupaObiektów=None,
                nazwa="podstawowy",
                polozenie=(0, 0),
                wymiary=(100, 100),
                kolory={
                    "niebieski": (0, 0, 255),
                    "czerwony": (255, 0, 0)
                },
                rodzaj="Przycisk",
                widzialnosc=True,
                pliki=None,
                dane=None,
                wymiary_labiryntu=(20, 20),
                obiekty_labiryntu=None
                ):

        Obiekt.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc)
        Użytkownik.__init__(self, pliki, dane)
        Labirynt.__init__(self, ekran, grupaObiektów, nazwa, polozenie, wymiary, rodzaj, widzialnosc, wymiary_labiryntu, obiekty_labiryntu)

    def edycja(self, nazwa=None, polozenie=None, wymiary=None, kolory=None, pliki=None, dane=None, wymiary_labiryntu=None, obiekty_labiryntu=None):

        if nazwa is not None:
            self.nazwa = nazwa
        if polozenie is not None:
            self.polozenie = polozenie
        if wymiary is not None:
            self.wymiary = wymiary
        if kolory is not None:
            self.kolory = kolory

        if pliki is not None:
            self.pliki = pliki
        if dane is not None:
            self.dane = dane

        if wymiary_labiryntu is not None:
            self.wymiary_labiryntu = wymiary_labiryntu
        if obiekty_labiryntu is not None:
            self.obiekty_labiryntu = obiekty_labiryntu

    def dodajDoGrupy():
        0

    def usunZgrupy():
        0

    def stwórz():
        0

    def ruch():
        0
