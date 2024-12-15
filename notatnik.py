import pygame  

# System zarządzający ekranami
class System:
    def __init__(self):
        self.ekrany = []
        self.aktywny_ekran = None

    def dodaj_ekran(self, ekran):
        self.ekrany.append(ekran)
        if not self.aktywny_ekran:
            self.aktywny_ekran = ekran  # Domyślnie ustaw pierwszy ekran jako aktywny

    def ustaw_aktywny_ekran(self, ekran):
        self.aktywny_ekran = ekran

    def renderuj(self):
        if self.aktywny_ekran:
            self.aktywny_ekran.stworz_ekran()

# Klasa opisująca pojedynczy ekran
class Ekran:
    def __init__(
        self,
        nazwa,
        klatki,
        szerokosc,
        wysokosc,
        kolor_tla=(0, 0, 0)
    ):
        self.nazwa = nazwa
        self.klatki = klatki
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.kolor_tla = kolor_tla
        self.przyciski = []

    def stworz_ekran(
        self
    ):
        self.nazwa.fill(self.kolor_tla)

        for przycisk in self.przyciski:
            przycisk.stworz()

    def dodaj_przycisk(
        self,
        przycisk
    ):
        self.przyciski.append(przycisk)

# Klasa zarządzania grupami przycisków
class KlasaPrzyciskow:
    def __init__(
        self,
        nazwa
    ):
        self.nazwa = nazwa
        self.przyciski = []

    def dodaj_przycisk(
        self,
        przycisk
    ):
        self.przyciski.append(przycisk)

    def ustaw_kolor(
        self,
        kolor
    ):
        for przycisk in self.przyciski:
            przycisk.kolor = kolor

    def ukryj(
        self
    ):
        for przycisk in self.przyciski:
            przycisk.ukryty = True

    def pokaz(
        self
    ):
        for przycisk in self.przyciski:
            przycisk.ukryty = False

# Klasa przycisku
class Przycisk:
    def __init__(
        self,
        ekran,
        x,
        y,
        szerokosc,
        wysokosc,
        kolor,
        tekst=None,
        kolor_tekstu=(0, 0, 0),
        rozmiar_czcionki=20,
        nazwa_czcionki=None,
        akcja=None,
        kolor_ramki=(0, 0, 0),
        klasa=None
    ):
        self.ekran = ekran
        self.x = x
        self.y = y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.kolor = kolor
        self.kolor_ramki = kolor_ramki
        self.tekst = tekst
        self.kolor_tekstu = kolor_tekstu
        self.rozmiar_czcionki = rozmiar_czcionki
        self.nazwa_czcionki = nazwa_czcionki
        self.akcja = akcja
        self.klasa = klasa
        self.ukryty = False

        ekran.dodaj_przycisk(self)
        if klasa:
            klasa.dodaj_przycisk(self)

    def stworz(
        self
    ):
        if self.ukryty:
            return

        pygame.draw.rect(self.ekran.nazwa, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))

        pygame.draw.rect(self.ekran.nazwa, self.kolor_ramki, (self.x, self.y, self.szerokosc, self.wysokosc), 3)

        if self.tekst:
            czcionka = pygame.font.Font(self.nazwa_czcionki, self.rozmiar_czcionki)
            powierzchnia_tekstu = czcionka.render(self.tekst, True, self.kolor_tekstu)
            tekst_rect = powierzchnia_tekstu.get_rect(center=(self.x + self.szerokosc // 2, self.y + self.wysokosc // 2))
            self.ekran.nazwa.blit(powierzchnia_tekstu, tekst_rect)

    def czy_klikniety(
        self,
        pozycja_myszy
    ):
        return self.x <= pozycja_myszy[0] <= self.x + self.szerokosc and self.y <= pozycja_myszy[1] <= self.y + self.wysokosc

    def kliknij(
        self
    ):
        if self.akcja:
            self.akcja()

class Tekst:
    def __init__(
        self,
        ekran,
        tekst,
        rozmiar_czcionki,
        kolor,
        pozycja,
        nazwa_czcionki=None
    ):
        self.ekran = ekran
        self.tekst = tekst
        self.rozmiar_czcionki = rozmiar_czcionki
        self.kolor = kolor
        self.x, self.y = pozycja
        self.nazwa_czcionki = nazwa_czcionki

    def stworz(
        self
    ):
        czcionka = pygame.font.Font(self.nazwa_czcionki, self.rozmiar_czcionki)
        powierzchnia_tekstu = czcionka.render(self.tekst, True, self.kolor)
        self.ekran.blit(powierzchnia_tekstu, (self.x, self.y))

    def edycja(
        self,
        rodzaj, #lista
        zmiana
    ):  
        def jedna_zmiana(
            rodzaj
        ):
            match rodzaj:
                case "tekst":
                    self.tekst = zmiana
                case "rozmiar_czcionki":
                    self.rozmiar_czcionki = zmiana  # Poprawiono z self.rodzaj na self.rozmiar_czcionki
                case "kolor":
                    self.kolor = zmiana
                case "pozycja":
                    self.x, self.y = zmiana  # Zmieniamy pozycję na nową (x, y)
                case "nazwa_czcionki":
                    self.nazwa_czcionki = zmiana

        if type(rodzaj) == list:
            
            for i in range(len(rodzaj)):
                jedna_zmiana(rodzaj[i])

        else:
            jedna_zmiana(rodzaj)

class Wyswietlacz:
    def __init__(
        self,
        ekran,
        x,
        y,
        szerokosc,
        wysokosc,
        rozmiar_czcionki,
        lZnakowWwierszu,
        tekst="",
        kolor=(255, 255, 255),
        kolor_czcionki=(0, 0, 0),
        nazwa_czcionki=None,
        interlinia=5,
        wyrownanie="lewo",
        kolor_ramki=None,
        grubosc_ramki=0,
        aktywny=True,
        podziel_tekst=True,
    ):
        self.ekran = ekran
        self.x = x
        self.y = y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.rozmiar_czcionki = rozmiar_czcionki
        self.lZnakowWwierszu = lZnakowWwierszu
        self.tekst = tekst
        self.kolor = kolor
        self.kolor_czcionki = kolor_czcionki
        self.nazwa_czcionki = nazwa_czcionki
        self.interlinia = interlinia
        self.wyrownanie = wyrownanie
        self.kolor_ramki = kolor_ramki
        self.grubosc_ramki = grubosc_ramki
        self.aktywny = aktywny
        self.podziel_tekst = podziel_tekst

    def zawijanie_tekstu(self, tekst, font):
        """Podział tekstu na linie zgodnie z szerokością pola."""
        wiersze = []
        slowa = tekst.split(" ")
        wiersz = ""

        for slowo in slowa:
            if font.size(wiersz + slowo)[0] <= self.szerokosc:
                wiersz += slowo + " "
            else:
                wiersze.append(wiersz.strip())
                wiersz = slowo + " "

        wiersze.append(wiersz.strip())
        return wiersze

    def rysuj_ramke(self):
        """Rysuje tło oraz ramkę wyświetlacza."""
        if self.kolor:
            pygame.draw.rect(self.ekran, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))
        if self.kolor_ramki and self.grubosc_ramki > 0:
            pygame.draw.rect(self.ekran, self.kolor_ramki, (self.x, self.y, self.szerokosc, self.wysokosc), self.grubosc_ramki)

    def rysuj_tekst(self, linia_od=0, linia_do=None):
        """Rysuje tekst na wyświetlaczu w wybranych liniach."""
        if not self.aktywny or not self.tekst:
            return

        # Tworzenie obiektu czcionki
        font = pygame.font.Font(self.nazwa_czcionki, self.rozmiar_czcionki)

        # Dzielimy tekst na linie
        tekst_podzielony = self.zawijanie_tekstu(self.tekst, font)

        # Wyliczamy maksymalną ilość linii, która zmieści się w wyświetlaczu
        linia_do = linia_do or len(tekst_podzielony)
        tekst_podzielony = tekst_podzielony[linia_od:linia_do]

        # Rysowanie każdego wiersza
        y_offset = self.y
        for wiersz in tekst_podzielony:
            tekst_raster = font.render(wiersz, True, self.kolor_czcionki)
            if self.wyrownanie == "lewo":
                self.ekran.blit(tekst_raster, (self.x, y_offset))
            elif self.wyrownanie == "srodek":
                tekst_x = self.x + (self.szerokosc - tekst_raster.get_width()) // 2
                self.ekran.blit(tekst_raster, (tekst_x, y_offset))
            elif self.wyrownanie == "prawo":
                tekst_x = self.x + self.szerokosc - tekst_raster.get_width()
                self.ekran.blit(tekst_raster, (tekst_x, y_offset))

            y_offset += tekst_raster.get_height() + self.interlinia

    def rysuj(self, linia_od=0, linia_do=None):
        """Rysuje ramkę i tekst na ekranie."""
        if not self.aktywny:
            return
        self.rysuj_ramke()
        self.rysuj_tekst(linia_od, linia_do)

    def edycja(self, rodzaj, zmiana):
        """Zmienia właściwości wyświetlacza."""
        def jedna_zmiana(rodzaj):
            match rodzaj:
                case "tekst":
                    self.tekst = zmiana
                case "rozmiar_czcionki":
                    self.rozmiar_czcionki = zmiana
                case "kolor":
                    self.kolor = zmiana
                case "pozycja":
                    self.x, self.y = zmiana
                case "nazwa_czcionki":
                    self.nazwa_czcionki = zmiana

        if type(rodzaj) == list:
            for i in range(len(rodzaj)):
                jedna_zmiana(rodzaj[i])
        else:
            jedna_zmiana(rodzaj)
pygame.init()
szerokosc, wysokosc = 800, 600
# Parametry ekranu
x = szerokosc // 24  # Jednostka szerokości (37,5 px)
y = wysokosc // 16  # Jednostka wysokości (37,5 px)

# Parametry przycisków
szerokosc_przyciskow = 7 * x  # 7 jednostek, czyli 7 * 37,5 px = 262,5 px
wysokosc_przyciskow = 2 * y  # 2 jednostki, czyli 2 * 37,5 px = 75 px

# Odstęp między przyciskami
odstep = y  # 37,5 px

# Tworzenie systemu ekranów i ekranu
system = System()
ekran = pygame.display.set_mode((szerokosc, wysokosc))
ekran1 = Ekran(ekran, None, szerokosc, wysokosc, kolor_tla=(255, 255, 255))
system.dodaj_ekran(ekran1)

# Tworzenie klasy przycisków
klasa_przyciskow = KlasaPrzyciskow("grupa_przyciskow")

# Tworzenie przycisków i przypisywanie ich do klasy
przycisk1 = Przycisk(
    ekran1, x, y, szerokosc_przyciskow, wysokosc_przyciskow, (169, 169, 169),
    tekst="Przycisk 1", kolor_tekstu=(0, 0, 0), rozmiar_czcionki=35,
    akcja=lambda: print("Kliknięto przycisk 1"),
    kolor_ramki=(0, 0, 0), klasa=klasa_przyciskow
)
przycisk2 = Przycisk(
    ekran1, x, y * 4, szerokosc_przyciskow, wysokosc_przyciskow, (169, 169, 169),
    tekst="Przycisk 2", kolor_tekstu=(0, 0, 0), rozmiar_czcionki=35,
    akcja=lambda: print("Kliknięto przycisk 2"),
    kolor_ramki=(0, 0, 0), klasa=klasa_przyciskow
)
przycisk3 = Przycisk(
    ekran1, x, y * 7, szerokosc_przyciskow, wysokosc_przyciskow, (169, 169, 169),
    tekst="Przycisk 3", kolor_tekstu=(0, 0, 0), rozmiar_czcionki=35,
    akcja=lambda: print("Kliknięto przycisk 3"),
    kolor_ramki=(0, 0, 0), klasa=klasa_przyciskow
)
przycisk4 = Przycisk(
    ekran1, x, y * 10, szerokosc_przyciskow, wysokosc_przyciskow, (169, 169, 169),
    tekst="Przycisk 4", kolor_tekstu=(0, 0, 0), rozmiar_czcionki=35,
    akcja=lambda: print("Kliknięto przycisk 4"),
    kolor_ramki=(0, 0, 0), klasa=klasa_przyciskow
)
przycisk5 = Przycisk(
    ekran1, x, y * 13, szerokosc_przyciskow, wysokosc_przyciskow, (169, 169, 169),
    tekst="Przycisk 5", kolor_tekstu=(0, 0, 0), rozmiar_czcionki=35,
    akcja=lambda: print("Kliknięto przycisk 5"),
    kolor_ramki=(0, 0, 0), klasa=klasa_przyciskow
)

# Tworzenie wyświetlacza
wyswietlacz = Wyswietlacz(
    ekran1,  # Ekran na którym się wyświetli
    x,  # Pozycja na osi X
    y + 3 * odstep,  # Pozycja na osi Y (z uwzględnieniem odstępu między przyciskami)
    7 * x,  # Szerokość wyświetlacza
    4 * y,  # Wysokość wyświetlacza
    30,  # Rozmiar czcionki
    30,  # Liczba znaków w wierszu
    tekst="Witaj na ekranie!",  # Przykładowy tekst
    kolor=(200, 200, 255),  # Kolor tła wyświetlacza
    kolor_czcionki=(0, 0, 0),  # Kolor czcionki
)

# W celu wyświetlenia na ekranie musimy ją rysować w funkcji renderującą ekran:
system.renderuj()  # Ta linia zaktualizuje aktywny ekran, rysując wszystkie elementy

# Pętla główna (gdzie sprawdzane są zdarzenia i renderowanie)
running = True
while running:
    ekran1.nazwa.fill((255, 255, 255))  # Tło ekranu
    wyswietlacz.rysuj()  # Rysowanie wyświetlacza
    pygame.display.flip()  # Aktualizacja okna

    # Sprawdzanie zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Dodaj obsługę innych zdarzeń, np. kliknięcie przycisku
pygame.quit()

