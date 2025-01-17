import pygame
import re
import json
import numpy as np
import pickle
import math
import random


class Ekran:
    def __init__(self,
                fps=60,
                ekran = None,
                nazwa="Labirynt APP",
                wymiary=(1215, 670),
                obiekty=None,
                częstotliwość=70,
                kolor=(255, 255, 255)
                ):
        if obiekty is None:
            obiekty = []
        self.ekran = ekran
        self.fps = fps
        self.nazwa = nazwa
        self.x, self.y = wymiary
        self.obiekty = obiekty
        self.częstotliwość = częstotliwość
        self.kolor = kolor

    def edycja(self, nazwa=None, fps=None, x=None, y=None, kolor=None, obiekty=None, częstotliwość=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if fps is not None:
            self.fps = fps
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
        self.ekran = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption(self.nazwa)
        self.częstotliwość = pygame.time.Clock()

    def odśwież(self):
        if self.ekran:
            pygame.display.flip()
            self.częstotliwość.tick(self.fps)

    def wyczyść(self):
        if self.ekran:
            self.ekran.fill(self.kolor)

    def dodajObiekty(self, wszystkObiekty):
        for i in range(len(wszystkObiekty)):
            self.obiekty.append(wszystkObiekty[i])

    def usunObiekty(self, wszystkObiekty):
        for i in range(len(wszystkObiekty), -1, -1):
            if wszystkObiekty[i] in self.obiekty:
                self.obiekty.pop()

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

ekran = Ekran()
ekran.stwórz()

running = True

while running:
    clicked_this_frame = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not clicked_this_frame:
            clicked_this_frame = True

    ekran.wyczyść()
    ekran.odśwież()
