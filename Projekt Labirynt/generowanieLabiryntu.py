from typing import List, Tuple
import numpy as np
import random as randint


def stwórzKratkę(szerokość: int, wysokość: int):
    if szerokość % 2 == 0:
        szerokość -= 1
    if wysokość % 2 == 0:
        wysokość -= 1

    labirynt = np.zeros((szerokość, wysokość))
    for i in range(len(labirynt)):
        for j in range(len(labirynt[i])):
            if i == 0 or i == len(labirynt) - 1 or j == 0 or j == len(labirynt[i]) - 1:
                labirynt[i][j] = 8
            elif i % 2 == 0 and j % 2 == 0:
                labirynt[i][j] = 8
            elif i % 2 != 0 and j % 2 != 0:
                labirynt[i][j] = 2

    labirynt[1][0] = 3
    labirynt[len(labirynt) - 2][len(labirynt[0]) - 1] = 4

    return labirynt

def SprawdzSasiadow(punkt: tuple[int, int], labirynt: np.ndarray) -> dict:
    x, y = punkt
    sasiedzi = {0: [], 8: [], 2: [], 3: [], 4: []}
    kierunki = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    
    for dx, dy in kierunki.values():
        Nx, Ny = x + dx, y + dy
        if 0 <= Nx < labirynt.shape[0] and 0 <= Ny < labirynt.shape[1]:
            wartosc = labirynt[Nx][Ny]
            sasiedzi[wartosc].append((Nx, Ny))
    
    return sasiedzi

def LiczbaŚcian(labirynt: np.ndarray) -> np.ndarray:
    liczba_ścian = np.zeros_like(labirynt)
    
    for i in range(labirynt.shape[0]):
        for j in range(labirynt.shape[1]):

            if labirynt[i][j] not in [3, 4, 8]:
                sasiedzi = SprawdzSasiadow((i, j), labirynt)
                liczba_ścian[i][j] = len(sasiedzi[8])
    
    return liczba_ścian

def WstawTab(tab1: List[List[int]], tab2: List[List[int]]) -> List[List[int]]:

    if len(tab1) != len(tab2) or len(tab1[0]) != len(tab2[0]):
        raise ValueError("Tablice mają różne wymiary!")
    
    for i in range(len(tab2)):
        for j in range(len(tab2[i])):
            if tab2[i][j] != 0:
                tab1[i][j] = tab2[i][j]
    
    return tab1

def bfs(zajętePola: List[Tuple[int, int]] = [], trasy: List[List[Tuple[int, int]]] = []):
    for trasa in trasy:
        continue
    #     pole = trasa[len(trasa) - 1]
    #     sasiedzi = SprawdzSasiadow(pole)
    #     sasiad = randint()
        # dla każdego sąsiada dodanie trasy poprzez losowość (to labirynt nie bfs)

labirynt = stwórzKratkę(11, 11)
ściany = LiczbaŚcian(labirynt)
labirynt = WstawTab(labirynt, ściany)

print(labirynt)