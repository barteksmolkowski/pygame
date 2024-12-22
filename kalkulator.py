import pygame
import math

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

class Button:
    def __init__(self, position, size, color, text="", action=None, text_thickness=1, hover_effect=True, hover_intensity=-0.1, border_width=1, border_color=(0, 0, 0)):
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

    def Draw(self, screen, font=None):
        # Jeśli efekt hover jest włączony, sprawdzamy, czy kursor jest nad przyciskiem
        if self.hover_effect:
            x, y = pygame.mouse.get_pos()
            # Stosujemy efekt hover
            if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
                # Dopasowujemy intensywność, która może być dodatnia lub ujemna
                color = (
                    int(self.color[0] * (1 + self.hover_intensity)),
                    int(self.color[1] * (1 + self.hover_intensity)),
                    int(self.color[2] * (1 + self.hover_intensity))
                )
                # Zapewniamy, że wartości kolorów mieszczą się w przedziale od 0 do 255
                color = tuple(max(0, min(255, c)) for c in color)
            else:
                color = self.color
        else:
            color = self.color

        # Rysujemy przycisk z (ewentualnie zmienionym) kolorem
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        
        # Rysowanie ramki wokół przycisku, jeśli border_width(szerokość_obramowania) > 0
        if self.border_width > 0:
            pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), self.border_width)

        # Rysowanie tekstu
        if self.text:
            if font is None:
                font = pygame.font.Font(None, 36)
            font.set_bold(self.text_thickness > 1)  # Ustawienie pogrubienia na podstawie grubości tekstu
            text_surface = font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            screen.blit(text_surface, text_rect)

    def Click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
                if self.action:
                    self.action()

    def collidepoint(self, pos):
        #Metoda, która sprawdza, czy punkt 'pos' znajduje się w obrębie przycisku.
        x, y = pos
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

class CalculatorDisplay():
    def __init__(self, display):
        self.display = display
        self.text = ""
        self.letters = []
        self.operation = ""
        self.result = 0

    def calculate(self, number1, operation, number2 = 0):
        result = 0
        match operation:
            case "+":
                result + number1 + number2
            case "-":
                result = number1 - number2
            case "*":
                result = number1 * number2
            case "/":
                if number2 != 0:
                    result = round(number1 / number2)
                else:
                    result = "Error"
            case "1/x":
                if number1 != 0:
                    result = 1 / number1
                else:
                    result = "Error"
            case "x^2":
                result = number1 ** 2
            case "sqrt(x)":
                if number1 >= 0:
                    result = math.sqrt(number1)
                else:
                    result = "Error"
            case "%":
                result = number1 % number2
        
        return 0 if len(result) > 13 else result
        
    def SendToDisplay(self, text):
        0

    def TextUpdate(self, NewLetter):
        if len(self.letters) not in [3, 7, 11] and len(self.letters) <= 13:
            try:
                self.letters.append(int(NewLetter))
            except ValueError:
                if self.operation == "":
                    self.operation = NewLetter
                else:
                    # podaje wynik i automatycznie ustawia pierwszą liczbę na wynik
                    pass

# Pygame Initialization
pygame.init()

# Tworzymy obiekt ekranu
screen = Screen(60, 322, 467, (245, 245, 245))  # x, y, width, height, color
screen.Create()

# Tworzymy nowy obiekt klasy UserKeyboard, który obsługuje interakcje z klawiaturą
keyboard = UserKeyboard()


# Zainicjuj obiekt wyświetlacz
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

# Funkcje objaśniające operacje na pamięci (używając symboli zastępczych dla rzeczywistej funkcjonalności)
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

# Zmienna globalna dla bieżącego symbolu do wyświetlenia (np. aktualnie wybrana liczba lub operacja)
aktualny_znak = ""

# Zaktualizuj bieżący symbol za pomocą wybranego znaku
def set_current_character(znak):
    global aktualny_znak
    aktualny_znak = znak

# TWORZENIE PRZYCISKÓW (słownik wraz z  funkcjonalnością)
button_mapping = {
    # (Poz, Rozmiar,Kolor,Etykieta,Akcja oraz wszelkie dodatkowe właściwości)
    "Add/Sub": Button((5, 413), (75, 46), (255, 255, 255), "+/-", action=lambda: (print("Click +/-"), set_current_character("+/-"))),
    "Zero": Button((84, 413), (75, 46), (255, 255, 255), "0", action=lambda: (print("Click 0"), set_current_character("0"))),
    "Comma": Button((163, 413), (75, 46), (255, 255, 255), ",", action=lambda: (print("Click ,"), set_current_character(","))),
    "Equals": Button((242, 413), (75, 46), (0, 110, 200), "=", action=lambda: (print("Click ="), set_current_character("=")), hover_intensity=0.1),

    "One": Button((5, 363), (75, 46), (255, 255, 255), "1", action=lambda: (print("Click 1"), set_current_character("1"))),
    "Two": Button((84, 363), (75, 46), (255, 255, 255), "2", action=lambda: (print("Click 2"), set_current_character("2"))),
    "Three": Button((163, 363), (75, 46), (255, 255, 255), "3", action=lambda: (print("Click 3"), set_current_character("3"))),
    "Add": Button((242, 363), (75, 46), (255, 255, 255), "+", action=lambda: (print("Click +"), set_current_character("+"))),

    "Four": Button((5, 313), (75, 46), (255, 255, 255), "4", action=lambda: (print("Click 4"), set_current_character("4"))),
    "Five": Button((84, 313), (75, 46), (255, 255, 255), "5", action=lambda: (print("Click 5"), set_current_character("5"))),
    "Six": Button((163, 313), (75, 46), (255, 255, 255), "6", action=lambda: (print("Click 6"), set_current_character("6"))),
    "Minus": Button((242, 313), (75, 46), (255, 255, 255), "-", action=lambda: (print("Click -"), set_current_character("-"))),

    "Seven": Button((5, 263), (75, 46), (255, 255, 255), "7", action=lambda: (print("Click 7"), set_current_character("7"))),
    "Eight": Button((84, 263), (75, 46), (255, 255, 255), "8", action=lambda: (print("Click 8"), set_current_character("8"))),
    "Nine": Button((163, 263), (75, 46), (255, 255, 255), "9", action=lambda: (print("Click 9"), set_current_character("9"))),
    "Times": Button((242, 263), (75, 46), (255, 255, 255), "x", action=lambda: (print("Click x"), set_current_character("x"))),

    "Reciprocal": Button((5, 213), (75, 46), (255, 255, 255), "1/x", action=lambda: (print("Click 1/x"), set_current_character("1/x"))),
    "Square": Button((84, 213), (75, 46), (255, 255, 255), "x^2", action=lambda: (print("Click x^2"), set_current_character("x^2"))),
    "Str": Button((163, 213), (75, 46), (255, 255, 255), "str(x)", action=lambda: (print("Click str(x)"), set_current_character("str(x)"))),
    "Divide": Button((242, 213), (75, 46), (255, 255, 255), "/", action=lambda: (print("Click /"), set_current_character("/"))),

    "Percent": Button((5, 163), (75, 46), (255, 255, 255), "%", action=lambda: (print("Click %"), set_current_character("%"))),
    "CE": Button((84, 163), (75, 46), (255, 255, 255), "CE", action=lambda: (print("Click CE"), set_current_character("CE"))),
    "C": Button((163, 163), (75, 46), (255, 255, 255), "C", action=lambda: (print("Click C"), set_current_character("C"))),
    "Del": Button((242, 163), (75, 46), (255, 255, 255), "DEL", action=lambda: (print("Click DEL"), set_current_character("DEL"))),

    "MemoryClear": Button((15, 140), (37, 22), (245, 245, 245), "MC", action=lambda: (MClearExplain(), print("Click Memory Clear"), set_current_character("MC")), border_width=0, hover_effect=False),
    "MemoryRecall": Button((66, 140), (37, 22), (245, 245, 245), "MR", action=lambda: (MRecallExplain(), print("Click Memory Recall"), set_current_character("MR")), border_width=0, hover_effect=False),
    "MemoryAdd": Button((117, 140), (37, 22), (245, 245, 245), "M+", action=lambda: (MAddExplain(), print("Click Memory Add"), set_current_character("M+")), border_width=0, hover_effect=False),
    "MemorySub": Button((168, 140), (37, 22), (245, 245, 245), "M-", action=lambda: (MSubExplain(), print("Click Memory Subtract"), set_current_character("M-")), border_width=0, hover_effect=False),
    "MemoryStore": Button((219, 140), (37, 22), (245, 245, 245), "MS", action=lambda: (MStoreExplain(), print("Click Memory Store"), set_current_character("MS")), border_width=0, hover_effect=False),
    "MemoryDisplay": Button((270, 140), (37, 22), (245, 245, 245), "MD", action=lambda: (MDisplayExplain(), print("Click Memory Display"), set_current_character("MD")), border_width=0, hover_effect=False)
}

# Pętla główna
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Obsługuje kliknięcia
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in button_mapping.values():
                if button.collidepoint(event.pos):  # Zatrzymajmy się w przycisku, jeśli kliknięto
                    button.action()

    screen.Clear()  # Wyczyszcz ekran
    for button in button_mapping.values():
        button.Draw(screen.screen)  # Rysujemy przyciski na powierzchni ekranu
    
    display.Draw(screen.screen)
    
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Ograniczamy liczbę klatek do 30

pygame.quit()