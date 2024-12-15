import pygame
import random

# Inicjalizacja Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Pozycja gracza (zielony kwadrat)
gracz_x = screen.get_width() / 2
gracz_y = screen.get_height() / 2
rozmiar_gracza = 40
predkosc = 300

# Pozycja czerwonego kwadratu
kwadrat_x = random.randint(0, screen.get_width() - rozmiar_gracza)
kwadrat_y = random.randint(0, screen.get_height() - rozmiar_gracza)
rozmiar_kwadratu = 40

# Licznik punktów
punkty = 0
win_punkty = 10

# Funkcja kolizji
def czujnik(gracz, kwadrat):
    return (gracz[0] < kwadrat[0] + kwadrat[2] and
            gracz[0] + gracz[2] > kwadrat[0] and
            gracz[1] < kwadrat[1] + kwadrat[3] and
            gracz[1] + gracz[3] > kwadrat[1])

# Funkcja wyświetlająca tekst
def rysuj_tekst(ekran, tekst, rozmiar_czcionki, kolor, pozycja, nazwa_czcionki=None):
    czcionka = pygame.font.Font(nazwa_czcionki, rozmiar_czcionki)
    powierzchnia_tekstu = czcionka.render(tekst, True, kolor)
    ekran.blit(powierzchnia_tekstu, pozycja)

# Główna pętla gry
running = True
system = "game"  # Zmienna określająca stan gry

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Wyjście z gry
                running = False

    # Ruch gracza i logika gry tylko w trybie "game"
    if system == "game":
        # Ruch gracza za pomocą strzałek i WASD
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Góra
            gracz_y -= predkosc * clock.get_time() / 1000
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Dół
            gracz_y += predkosc * clock.get_time() / 1000
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Lewo
            gracz_x -= predkosc * clock.get_time() / 1000
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Prawo
            gracz_x += predkosc * clock.get_time() / 1000

        # Ograniczenie ruchu gracza do granic mapy
        gracz_x = max(0, min(gracz_x, screen.get_width() - rozmiar_gracza))
        gracz_y = max(0, min(gracz_y, screen.get_height() - rozmiar_gracza))

        # Sprawdzanie kolizji gracza z czerwonym kwadratem
        gracz = (gracz_x, gracz_y, rozmiar_gracza, rozmiar_gracza)
        kwadrat = (kwadrat_x, kwadrat_y, rozmiar_kwadratu, rozmiar_kwadratu)

        if czujnik(gracz, kwadrat):
            punkty += 1
            kwadrat_x = random.randint(0, screen.get_width() - rozmiar_kwadratu)
            kwadrat_y = random.randint(0, screen.get_height() - rozmiar_kwadratu)

        if punkty == win_punkty:
            system = "end"  # Przejście do ekranu końcowego

    # Rysowanie elementów na ekranie
    screen.fill((255, 255, 255))  # Tło

    if system == "game":
        # Gracz
        pygame.draw.rect(screen, "green", (gracz_x, gracz_y, rozmiar_gracza, rozmiar_gracza))
        # Czerwony kwadrat
        pygame.draw.rect(screen, "red", (kwadrat_x, kwadrat_y, rozmiar_kwadratu, rozmiar_kwadratu))
        # Wyświetlanie punktów
        rysuj_tekst(screen, f"Punkty: {punkty}", 30, (0, 0, 0), (10, 10))

    if system == "end":
        # Niebieskie okno wygranej
        x_srodek = screen.get_width() // 2
        y_srodek = screen.get_height() // 2
        pygame.draw.rect(screen, "blue", (x_srodek - 100, y_srodek - 50, 200, 100))
        # Tekst "Wygrana"
        rysuj_tekst(screen, "Wygrana!", 50, (255, 255, 255), (x_srodek - 70, y_srodek - 25))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
