import pygame
import math
import traceback

class Screen:
    def __init__(self, fps, width, height, color):
        self.fps = fps
        self.width = width
        self.height = height
        self.color = color
        self.screen = None
        self.clock = None

    def Create(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Calculator")
        self.clock = pygame.time.Clock()

    def Refresh(self):
        if self.screen:
            pygame.display.flip()
            self.clock.tick(self.fps)

    def Clear(self):
        if self.screen:
            self.screen.fill(self.color)

    def Edit(self, elements, new_elements):
        if len(elements) == len(new_elements):
            for i in range(len(elements)):
                match elements[i]:
                    case "fps": self.fps = new_elements[i]
                    case "width": self.width = new_elements[i]
                    case "height": self.height = new_elements[i]
                    case "color": self.color = new_elements[i]
                    case "screen": self.screen = new_elements[i]
                    case "clock": self.clock = new_elements[i]

class UserKeyboard:
    def __init__(self):
        self.keys = {}

    def Sensor(self, event):
        if event.type == pygame.KEYDOWN:
            self.keys[event.key] = "pressed"
        elif event.type == pygame.KEYUP:
            self.keys[event.key] = "released"

    def KeyState(self, key):
        return self.keys.get(key, None)

class Display:
    def __init__(self, position, size, text="", color=(0, 0, 0), 
                 border_color=(0, 0, 0), border_thickness=10, font_size=36, 
                 font_thickness=0, align="left"):
        self.position = position
        self.size = size
        self.text = text
        self.color = color
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.font_size = font_size
        self.font_thickness = font_thickness
        self.align = align

        self.x, self.y = self.position
        self.width, self.height = self.size

        # Zainicjuj czcionkę
        self.font = pygame.font.Font(None, font_size)

    def Draw(self, screen):
        # Narysuj granicę
        pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), self.border_thickness)

        # Renderowanie tekstu i obliczenie jego położenia
        text_surface = self.font.render(self.text, True, self.color)
        text_width, text_height = text_surface.get_size()

        # Wyrównanie
        if self.align == "left":
            text_x = self.x + 10 # Wypełnienie od lewej strony
        elif self.align == "center":
            text_x = self.x + (self.width - text_width) // 2 # Wypełnienie od środka
        elif self.align == "right":
            text_x = self.x + self.width - text_width - 10 # Wypełnienie od prawej strony

        # Wyśrodkuj tekst w pionie
        text_y = self.y + (self.height - text_height) // 2

        # Narysuj tekst
        screen.blit(text_surface, (text_x, text_y))

    def edit(self, text=None, color=None, border_color=None, font_size=None, align=None):
        if text is not None:
            try:
                text = float(text)
                if text - round(text) != 0:
                    self.text = str(text)
                else:
                    self.text = str(round(text))
            except ValueError:
                self.text = text
        if color is not None:
            self.color = color
        if border_color is not None:
            self.border_color = border_color
        if font_size is not None:
            self.font_size = font_size
            self.font = pygame.font.Font(None, font_size)
        if align is not None:
            self.align = align

class Button:
    def __init__(self, position, size, color, text="", action=None, text_thickness=1, hover_effect=True, hover_intensity=-0.1, border_width=1, border_color=(0, 0, 0), hover_effect_enabled=True, click_effect_enabled=True):
        self.x, self.y = position
        self.width, self.height = size
        self.color = color
        self.text = text
        self.action = action
        self.text_thickness = text_thickness
        self.hover_effect = hover_effect  # Czy efekt "hover" jest włączony
        self.hover_intensity = hover_intensity  # Intensywność ściemnienia/rozjaśnienia
        self.border_width = border_width  # Grubość ramki
        self.border_color = border_color  # Kolor ramki
        self.is_pressed = False  # Stan kliknięcia przycisku
        self.hover_effect_enabled = hover_effect_enabled  # Flaga włączająca/wyłączająca efekt hover
        self.click_effect_enabled = click_effect_enabled  # Flaga włączająca/wyłączająca efekt kliknięcia

    def Draw(self, screen, font=None):
        color = self.color

        # Obsługuje efekt hover, gdy kursor znajduje się nad przyciskiem
        if self.hover_effect and self.hover_effect_enabled:
            x, y = pygame.mouse.get_pos()
            if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
                # Rozjaśnia lub ściemnia w zależności od pozycji kursora
                color = (
                    int(color[0] * (1 + self.hover_intensity)),
                    int(color[1] * (1 + self.hover_intensity)),
                    int(color[2] * (1 + self.hover_intensity))
                )
                color = tuple(max(0, min(255, c)) for c in color)

        # Jeżeli przycisk jest wciśnięty i efekty kliknięcia są włączone, zmienia kolor
        if self.is_pressed and self.click_effect_enabled:
            color = (
                int(color[0] * (1 + (2 * self.hover_intensity))),
                int(color[1] * (1 + (2 * self.hover_intensity))),
                int(color[2] * (1 + (2 * self.hover_intensity)))
            )
            color = tuple(max(0, min(255, c)) for c in color)

        # Rysowanie przycisku z (ewentualnie zmienionym) kolorem
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        
        # Rysowanie ramki
        if self.border_width > 0:
            pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), self.border_width)

        # Rysowanie tekstu
        if self.text:
            if font is None:
                font = pygame.font.Font(None, 36)
            font.set_bold(self.text_thickness > 1)  # Pogrubienie tekstu
            text_surface = font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            screen.blit(text_surface, text_rect)

    def Click(self, event):
        # Kliknięcie myszką na przycisk
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
                self.is_pressed = True  # Przyciski są "wciśnięte"
                if self.action:
                    self.action()

        # Zwalnianie przycisku, powrót do stanu normalnego
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_pressed = False

    def collidepoint(self, pos):
        # Metoda sprawdzająca, czy punkt 'pos' znajduje się w obrębie przycisku.
        x, y = pos
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

class seven_segment():
    def __init__(self, screen, wiersz, polozenie, wymiary, typ_zmiennej="int", grubosc_ramki=0, kolor_ramki=(0, 0, 0), kolor_tla=(255, 255, 255), kolor_zero=(195, 195, 195), kolor_jeden=(255, 242, 0), grubosc_segmentu=5):
        self.screen = screen
        self.wiersz = wiersz
        self.x, self.y = polozenie
        self.szerokosc, self.wysokosc = wymiary
        self.typ_zmiennej = typ_zmiennej
        self.grubosc_ramki = grubosc_ramki
        self.kolor_ramki = kolor_ramki
        self.kolor_tla = kolor_tla
        self.kolor_zero = kolor_zero
        self.kolor_jeden = kolor_jeden
        self.grubosc_segmentu = grubosc_segmentu
        self.liczba = None
        self.segmenty = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0}
        
    def wyswietl(self):
        dane = [
            {"x": self.x + self.grubosc_segmentu, "y": self.y, "szerokosc": self.szerokosc - 2 * self.grubosc_segmentu, "wysokosc": self.grubosc_segmentu},  # Segment 1 (top)
            {"x": self.x + self.szerokosc - self.grubosc_segmentu, "y": self.y + self.grubosc_segmentu, "szerokosc": self.grubosc_segmentu, "wysokosc": (self.wysokosc // 2) - self.grubosc_segmentu},  # Segment 2 (top right)
            {"x": self.x + self.szerokosc - self.grubosc_segmentu, "y": self.y + (self.wysokosc // 2), "szerokosc": self.grubosc_segmentu, "wysokosc": (self.wysokosc // 2) - self.grubosc_segmentu},  # Segment 3 (bottom right)
            {"x": self.x + self.grubosc_segmentu, "y": self.y + self.wysokosc - self.grubosc_segmentu, "szerokosc": self.szerokosc - 2 * self.grubosc_segmentu, "wysokosc": self.grubosc_segmentu},  # Segment 4 (bottom)
            {"x": self.x, "y": self.y + (self.wysokosc // 2), "szerokosc": self.grubosc_segmentu, "wysokosc": (self.wysokosc // 2) - self.grubosc_segmentu},  # Segment 5 (bottom left)
            {"x": self.x, "y": self.y + self.grubosc_segmentu, "szerokosc": self.grubosc_segmentu, "wysokosc": (self.wysokosc // 2) - self.grubosc_segmentu},  # Segment 6 (top left)
            {"x": self.x + self.grubosc_segmentu, "y": self.y + (self.wysokosc // 2) - (self.grubosc_segmentu // 2), "szerokosc": self.szerokosc - 2 * self.grubosc_segmentu, "wysokosc": self.grubosc_segmentu}  # Segment 7 (middle)
        ]

        for i in range(7):
            color = self.kolor_jeden if self.segmenty[str(i + 1)] else self.kolor_zero
            pygame.draw.rect(self.screen, color, (dane[i]["x"], dane[i]["y"], dane[i]["szerokosc"], dane[i]["wysokosc"]))

    def edycja(self, wiersz=None, polozenie=None, wymiary=None, kolor_tla=None, kolor_zero=None, kolor_jeden=None, grubosc_segmentu=None):
        if wiersz is not None:
            self.wiersz = wiersz
        if polozenie is not None:
            self.polozenie = polozenie
        if wymiary is not None:
            self.wymiary = wymiary
        if kolor_tla is not None:
            self.kolor_tla = kolor_tla
        if kolor_zero is not None:
            self.kolor_zero = kolor_zero
        if kolor_jeden is not None:
            self.kolor_jeden = kolor_jeden
        if grubosc_segmentu is not None:
            self.grubosc_segmentu = grubosc_segmentu

    def aktualizuj(self, liczba):
        segment_map = {
            0: {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 0},
            1: {"1": 0, "2": 1, "3": 1, "4": 0, "5": 0, "6": 0, "7": 0},
            2: {"1": 1, "2": 1, "3": 0, "4": 1, "5": 1, "6": 0, "7": 1},
            3: {"1": 1, "2": 1, "3": 1, "4": 1, "5": 0, "6": 0, "7": 1},
            4: {"1": 0, "2": 1, "3": 1, "4": 0, "5": 0, "6": 1, "7": 1},
            5: {"1": 1, "2": 0, "3": 1, "4": 1, "5": 0, "6": 1, "7": 1},
            6: {"1": 1, "2": 0, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1},
            7: {"1": 1, "2": 1, "3": 1, "4": 0, "5": 0, "6": 0, "7": 0},
            8: {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1},
            9: {"1": 1, "2": 1, "3": 1, "4": 1, "5": 0, "6": 1, "7": 1}
        }
        self.segmenty = segment_map.get(liczba, {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0})

pygame.init()
screen = Screen(60, 322, 467, (245, 245, 245))  # x, y, width, height, color
screen.Create()
segmentowy7 = seven_segment(screen.screen, 1, (10, 75), (30, 55))
keyboard = UserKeyboard()
display = Display(
    (5, 70),               # Pozycja (x, y)
    (312, 65),             # Wymiary (szerokość, wysokość)
    "0",       # Tekst do wyświetlenia
    border_color=(0, 0, 0),# Kolor ramki (czarny)
    border_thickness=1,    # Grubość ramki
    align="right",         # Wyrównanie tekstu (poziome: "left", "center", "right")
    font_size=57,          # Rozmiar czcionki
    font_thickness=2       # Grubość czcionki
)
def MClearExplain():
    print("Clear the memory")

def MRecallExplain():
    print("Recall the value from memory")

def MAddExplain():
    print("Add the current value to memory")

def MSubExplain():
    print("Subtract the current value from memory")

def MStoreExplain():
    print("Store the current value in memory")

def MDisplayExplain():
    print("Display the current memory value")

def ifInteger(value):
    return isinstance(value, int)

aktualny_znak = ""

def set_current_character(znak):
    global aktualny_znak
    print(f"Kliknięto: {znak}")
    aktualny_znak = znak

def stworzenie_przyciskow():
    button_mapping = {
        "Add/Sub": Button((5, 413), (75, 46), (255, 255, 255), "+/-", action=lambda: set_current_character("+/-")),
        "Zero": Button((84, 413), (75, 46), (255, 255, 255), "0", action=lambda: set_current_character("0")),
        "Comma": Button((163, 413), (75, 46), (255, 255, 255), ",", action=lambda: set_current_character(",")),
        "Equals": Button((242, 413), (75, 46), (0, 110, 200), "=", action=lambda: set_current_character("="), hover_intensity=0.1),

        "One": Button((5, 363), (75, 46), (255, 255, 255), "1", action=lambda: set_current_character("1")),
        "Two": Button((84, 363), (75, 46), (255, 255, 255), "2", action=lambda: set_current_character("2")),
        "Three": Button((163, 363), (75, 46), (255, 255, 255), "3", action=lambda: set_current_character("3")),
        "Add": Button((242, 363), (75, 46), (255, 255, 255), "+", action=lambda: set_current_character("+")),

        "Four": Button((5, 313), (75, 46), (255, 255, 255), "4", action=lambda: set_current_character("4")),
        "Five": Button((84, 313), (75, 46), (255, 255, 255), "5", action=lambda: set_current_character("5")),
        "Six": Button((163, 313), (75, 46), (255, 255, 255), "6", action=lambda: set_current_character("6")),
        "Minus": Button((242, 313), (75, 46), (255, 255, 255), "-", action=lambda: set_current_character("-")),

        "Seven": Button((5, 263), (75, 46), (255, 255, 255), "7", action=lambda: set_current_character("7")),
        "Eight": Button((84, 263), (75, 46), (255, 255, 255), "8", action=lambda: set_current_character("8")),
        "Nine": Button((163, 263), (75, 46), (255, 255, 255), "9", action=lambda: set_current_character("9")),
        "Times": Button((242, 263), (75, 46), (255, 255, 255), "x", action=lambda: set_current_character("x")),

        "Reciprocal": Button((5, 213), (75, 46), (255, 255, 255), "1/x", action=lambda: set_current_character("1/x")),
        "Square": Button((84, 213), (75, 46), (255, 255, 255), "x^2", action=lambda: set_current_character("x^2")),
        "Str": Button((163, 213), (75, 46), (255, 255, 255), "str(x)", action=lambda: set_current_character("str(x)")),
        "Divide": Button((242, 213), (75, 46), (255, 255, 255), "/", action=lambda: set_current_character("/")),

        "Percent": Button((5, 163), (75, 46), (255, 255, 255), "%", action=lambda: set_current_character("%")),
        "CE": Button((84, 163), (75, 46), (255, 255, 255), "CE", action=lambda: set_current_character("CE")),
        "C": Button((163, 163), (75, 46), (255, 255, 255), "C", action=lambda: set_current_character("C")),
        "Del": Button((242, 163), (75, 46), (255, 255, 255), "DEL", action=lambda: set_current_character("DEL")),

        "MemoryClear": Button((15, 140), (37, 22), (245, 245, 245), "MC", action=lambda: (MClearExplain(), set_current_character("MC")), border_width=0, hover_effect=False, click_effect_enabled=False),
        "MemoryRecall": Button((66, 140), (37, 22), (245, 245, 245), "MR", action=lambda: (MRecallExplain(), set_current_character("MR")), border_width=0, hover_effect=False, click_effect_enabled=False),
        "MemoryAdd": Button((117, 140), (37, 22), (245, 245, 245), "M+", action=lambda: (MAddExplain(), set_current_character("M+")), border_width=0, hover_effect=False, click_effect_enabled=False),
        "MemorySub": Button((168, 140), (37, 22), (245, 245, 245), "M-", action=lambda: (MSubExplain(), set_current_character("M-")), border_width=0, hover_effect=False, click_effect_enabled=False),
        "MemoryStore": Button((219, 140), (37, 22), (245, 245, 245), "MS", action=lambda: (MStoreExplain(), set_current_character("MS")), border_width=0, hover_effect=False, click_effect_enabled=False),
        "MemoryDisplay": Button((270, 140), (37, 22), (245, 245, 245), "MD", action=lambda: (MDisplayExplain(), set_current_character("MD")), border_width=0, hover_effect=False, click_effect_enabled=False)
    }
    return button_mapping

button_mapping = stworzenie_przyciskow()
numer = 0
segments7 = []
for i in range(9):
    segments7.append(Button((10 + 34 * i, 75), (30, 55), (100, 100, 100)))

hist_klikniec = {"1znak": "0", "2znak": "0", "dzialanie": "", "memory": 0}
aktualna_funkcja = "1znak"
wpisana_liczba = ""  # Będzie przechowywać aktualnie wpisywaną liczbę jako tekst (np. 95.123)

def obsluga_znakow(aktualny_znak):
    global hist_klikniec, aktualna_funkcja, wpisana_liczba  # Declare global variables

    if aktualny_znak.isdigit():
        if hist_klikniec[aktualna_funkcja] == "0":
            hist_klikniec[aktualna_funkcja] = aktualny_znak
        else:
            if len(hist_klikniec[aktualna_funkcja]) < 9:
                hist_klikniec[aktualna_funkcja] += aktualny_znak

        display.edit(text=hist_klikniec[aktualna_funkcja])

    match aktualny_znak:
        case "+" | "-" | "x" | "/" | "%":
            hist_klikniec["dzialanie"] = aktualny_znak
            aktualna_funkcja = "2znak"
            hist_klikniec["2znak"] = "0"
        case "=":
            liczba1 = float(hist_klikniec["1znak"])
            liczba2 = float(hist_klikniec["2znak"])

            try:
                match hist_klikniec["dzialanie"]:
                    case "+":
                        wynik = liczba1 + liczba2
                    case "-":
                        wynik = liczba1 - liczba2
                    case "x":
                        wynik = liczba1 * liczba2
                    case "/":
                        if liczba2 == 0:
                            raise ZeroDivisionError
                        wynik = liczba1 / liczba2
                    case "%":
                        if liczba2 == 0:
                            raise ZeroDivisionError
                        wynik = liczba1 % liczba2

                wynik_zaokraglony = round(wynik, 8)  # Round to 8 decimal places
                wpisana_liczba = str(wynik_zaokraglony)[:9]  # Limit to 9 characters

                if len(wpisana_liczba) <= 9:
                    display.edit(text=wpisana_liczba)
                    hist_klikniec["1znak"] = str(wynik_zaokraglony)
                    aktualna_funkcja = "1znak"
                else:
                    display.edit(text="Error wynik")
            except ZeroDivisionError:
                display.edit(text="Error /0")
                hist_klikniec["1znak"] = "0"
                hist_klikniec["2znak"] = "0"
                hist_klikniec["dzialanie"] = ""
                aktualna_funkcja = "1znak"

        case "C":
            hist_klikniec = {"1znak": "0", "2znak": "0", "dzialanie": "", "memory": 0}
            aktualna_funkcja = "1znak"
            display.edit(text="0")
        case "CE":
            hist_klikniec[aktualna_funkcja] = "0"
            display.edit(text="0")
        case "DEL":
            hist_klikniec[aktualna_funkcja] = hist_klikniec[aktualna_funkcja][:-1]
            if hist_klikniec[aktualna_funkcja] == "" or hist_klikniec[aktualna_funkcja] == "-":
                hist_klikniec[aktualna_funkcja] = "0"
            else:
                try:
                    # Format the number to a maximum of 9 characters
                    formatted_number = float(hist_klikniec[aktualna_funkcja])
                    hist_klikniec[aktualna_funkcja] = str(formatted_number)[:9]
                except ValueError:
                    hist_klikniec[aktualna_funkcja] = "0"
            display.edit(text=hist_klikniec[aktualna_funkcja])
        case "+/-":
            if hist_klikniec[aktualna_funkcja]:
                hist_klikniec[aktualna_funkcja] = str(-float(hist_klikniec[aktualna_funkcja]))
                display.edit(text=hist_klikniec[aktualna_funkcja])
        case "x^2":
            try:
                liczba = float(hist_klikniec[aktualna_funkcja])
                wynik = liczba ** 2
                wynik_zaokraglony = round(wynik, 8)  # Round to 8 decimal places
                wpisana_liczba = str(wynik_zaokraglony)[:9]  # Limit to 9 characters

                if len(wpisana_liczba) <= 9:
                    display.edit(text=wpisana_liczba)
                    hist_klikniec[aktualna_funkcja] = str(wynik_zaokraglony)
                    print(f"Pełny wynik: {wynik}, Wynik zaokrąglony: {wynik_zaokraglony}")
                else:
                    display.edit(text="Error x^2(.1)")
            except ValueError:
                display.edit(text="Error x^2(.2)")
        case "1/x":
            try:
                liczba = float(hist_klikniec[aktualna_funkcja])
                if liczba != 0:
                    wynik = 1 / liczba
                    wynik_zaokraglony = round(wynik, 8)  # Round to 8 decimal places
                    wpisana_liczba = str(wynik_zaokraglony)[:9]  # Limit to 9 characters
                    display.edit(text=wpisana_liczba)
                    hist_klikniec[aktualna_funkcja] = str(wynik_zaokraglony)
                    print(f"Pełny wynik: {wynik}, Wynik zaokrąglony: {wynik_zaokraglony}")
                else:
                    display.edit(text="Error 1/x (.2)")
            except ValueError:
                display.edit(text="Error 1/x (.3)")
        case "str(x)":
            try:
                liczba = float(hist_klikniec[aktualna_funkcja])
                if liczba >= 0:
                    wynik = math.sqrt(liczba)
                    wynik_zaokraglony = round(wynik, 8)  # Round to 8 decimal places
                    wpisana_liczba = str(wynik_zaokraglony)[:9]  # Limit to 9 characters
                    display.edit(text=wpisana_liczba)
                    hist_klikniec[aktualna_funkcja] = str(wynik_zaokraglony)
                    print(f"Pełny wynik: {wynik}, Wynik zaokrąglony: {wynik_zaokraglony}")
                else:
                    display.edit(text="Error str (.1)")
            except ValueError:
                display.edit(text="Error str (.2)")
        case ",":
            if "." not in hist_klikniec[aktualna_funkcja]:  # Sprawdź, czy przecinek już istnieje
                hist_klikniec[aktualna_funkcja] += "."  # Dodaj przecinek do istniejącej liczby
                display.edit(text=hist_klikniec[aktualna_funkcja])  # Zaktualizuj wyświetlacz
        case "M+" | "M-" | "MR" | "MC":
            def aktualizuj_pamiec(operacja, wartosc):
                try:
                    match operacja:
                        case "dodaj":
                            hist_klikniec["memory"] += float(wartosc)
                        case "odejmij":
                            hist_klikniec["memory"] -= float(wartosc)
                        case "odczytaj":
                            wynik_zaokraglony = round(hist_klikniec["memory"], 8)  # Round to 8 decimal places
                            display.edit(text=str(wynik_zaokraglony)[:9])  # Limit to 9 characters
                    print(hist_klikniec)  # Wyświetl aktualny stan hist_klikniec
                except ValueError:
                    display.edit(text=f"Error {operacja}")
                    print(f"Błąd podczas operacji {operacja} na pamięci")
            match aktualny_znak:
                case "M+":
                    aktualizuj_pamiec("dodaj", hist_klikniec[aktualna_funkcja])
                case "M-":
                    aktualizuj_pamiec("odejmij", hist_klikniec[aktualna_funkcja])
                case "MR":
                    aktualizuj_pamiec("odczytaj", None)
                    # Update the current value with the memory value
                    if hist_klikniec["dzialanie"]:
                        hist_klikniec["2znak"] = str(hist_klikniec["memory"])[:9]
                        display.edit(text=hist_klikniec["2znak"])
                    else:
                        hist_klikniec[aktualna_funkcja] = str(hist_klikniec["memory"])[:9]
                        display.edit(text=hist_klikniec[aktualna_funkcja])
running = True
while running:
    clicked_this_frame = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in button_mapping.values():
            button.Click(event)

        if event.type == pygame.MOUSEBUTTONDOWN and not clicked_this_frame:
            clicked_this_frame = True

            for button in button_mapping.values():
                if button.collidepoint(event.pos):
                    button.action()
                    print(hist_klikniec)
                    try:
                        obsluga_znakow(aktualny_znak)
                    except ValueError:
                        traceback.print_exc()
                        print("Błąd podczas przetwarzania znaku:", aktualny_znak)

    screen.Clear()
    for button in button_mapping.values():
        button.Draw(screen.screen)
    for segment in segments7:
        segment.Draw(screen.screen)
    segmentowy7.aktualizuj(numer)
    segmentowy7.wyswietl()

    display.Draw(screen.screen)
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()