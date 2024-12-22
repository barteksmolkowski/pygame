import pygame

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

        # Initialize font
        self.font = pygame.font.Font(None, font_size)

    def Draw(self, screen):
        # Draw the border
        pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), self.border_thickness)

        # Render the text and calculate its position
        text_surface = self.font.render(self.text, True, self.color)
        text_width, text_height = text_surface.get_size()

        # Handle alignment
        if self.align == "left":
            text_x = self.x + 10  # Padding from the left
        elif self.align == "center":
            text_x = self.x + (self.width - text_width) // 2
        elif self.align == "right":
            text_x = self.x + self.width - text_width - 10  # Padding from the right

        # Vertically center the text
        text_y = self.y + (self.height - text_height) // 2

        # Draw the text
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
        
        # Rysowanie ramki wokół przycisku, jeśli border_width > 0
        if self.border_width > 0:
            pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), self.border_width)

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

# Pygame Initialization
pygame.init()
screen = Screen(60, 322, 467, (245, 245, 245))
screen.Create()
keyboard = UserKeyboard()

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

if True == True: # ADD BUTTONS
    buttonAddSub = Button((5, 413), (75, 46), (255, 255, 255), "+/-", action=lambda: print("Click +/-"))
    buttonZero = Button((84, 413), (75, 46), (255, 255, 255), "0", action=lambda: print("Click 0"))
    buttonComma = Button((163, 413), (75, 46), (255, 255, 255), ",", action=lambda: print("Click ,"))
    buttonEquals = Button((242, 413), (75, 46), (0, 110, 200), "=", action=lambda: print("Click ="), hover_intensity=0.1)

    buttonOne = Button((5, 363), (75, 46), (255, 255, 255), "1", action=lambda: print("Click 1"))
    buttonTwo = Button((84, 363), (75, 46), (255, 255, 255), "2", action=lambda: print("Click 2"))
    buttonThree = Button((163, 363), (75, 46), (255, 255, 255), "3", action=lambda: print("Click 3"))
    buttonAdd = Button((242, 363), (75, 46), (255, 255, 255), "+", action=lambda: print("Click +"))

    buttonFour = Button((5, 313), (75, 46), (255, 255, 255), "4", action=lambda: print("Click 4"))
    buttonFive = Button((84, 313), (75, 46), (255, 255, 255), "5", action=lambda: print("Click 5"))
    buttonSix = Button((163, 313), (75, 46), (255, 255, 255), "6", action=lambda: print("Click 6"))
    buttonMinus = Button((242, 313), (75, 46), (255, 255, 255), "-", action=lambda: print("Click -"))

    buttonSeven = Button((5, 263), (75, 46), (255, 255, 255), "7", action=lambda: print("Click 7"))
    buttonEight = Button((84, 263), (75, 46), (255, 255, 255), "8", action=lambda: print("Click 8"))
    buttonNine = Button((163, 263), (75, 46), (255, 255, 255), "9", action=lambda: print("Click 9"))
    buttonTimes = Button((242, 263), (75, 46), (255, 255, 255), "x", action=lambda: print("Click x"))

    buttonReciprocal = Button((5, 213), (75, 46), (255, 255, 255), "1/x", action=lambda: print("Click 1/x"))
    buttonSquare = Button((84, 213), (75, 46), (255, 255, 255), "x^2", action=lambda: print("Click x^2"))
    buttonStr = Button((163, 213), (75, 46), (255, 255, 255), "str(x)", action=lambda: print("Click str(x)"))
    buttonDivide = Button((242, 213), (75, 46), (255, 255, 255), "/", action=lambda: print("Click /"))

    buttonPercent = Button((5, 163), (75, 46), (255, 255, 255), "%", action=lambda: print("Click %"))
    buttonCE = Button((84, 163), (75, 46), (255, 255, 255), "CE", action=lambda: print("Click CE"))
    buttonC = Button((163, 163), (75, 46), (255, 255, 255), "C", action=lambda: print("Click C"))
    buttonDel = Button((242, 163), (75, 46), (255, 255, 255), "DEL", action=lambda: print("Click DEL"))

    buttonMemoryClear = Button((15, 140), (37, 22), (245, 245, 245), "MC", action=lambda: (MClearExplain(), print("Click Memory Clear")), border_width=0, hover_effect=False)
    buttonMemoryRecall = Button((66, 140), (37, 22), (245, 245, 245), "MR", action=lambda: (MRecallExplain(), print("Click Memory Recall")), border_width=0, hover_effect=False)
    buttonMemoryAdd = Button((117, 140), (37, 22), (245, 245, 245), "M+", action=lambda: (MAddExplain(), print("Click Memory Add")), border_width=0, hover_effect=False)
    buttonMemorySub = Button((168, 140), (37, 22), (245, 245, 245), "M-", action=lambda: (MSubExplain(), print("Click Memory Subtract")), border_width=0, hover_effect=False)
    buttonMemoryStore = Button((219, 140), (37, 22), (245, 245, 245), "MS", action=lambda: (MStoreExplain(), print("Click Memory Store")), border_width=0, hover_effect=False)
    buttonMemoryDisplay = Button((270, 140), (37, 22), (245, 245, 245), "MD", action=lambda: (MDisplayExplain(), print("Click Memory Display")), border_width=0, hover_effect=False)

display = Display(
    (5, 70),               # Pozycja (x, y)
    (312, 65),             # Wymiary (szerokość, wysokość)
    "9 999 999 999",       # Tekst do wyświetlenia
    border_color=(0, 0, 0),# Kolor ramki (czarny)
    border_thickness=1,    # Grubość ramki
    align="right",         # Wyrównanie tekstu (poziome: "left", "center", "right")
    font_size=57,          # Rozmiar czcionki
    font_thickness=2      # Grubość czcionki
)
# Main program loop
running = True
current_button = None  # Zmienna do przechowywania aktualnie klikniętego przycisku

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keyboard.Sensor(event)

        button_mapping = {
            buttonAddSub: "Add/Sub",
            buttonZero: "0",
            buttonComma: ",",
            buttonEquals: "=",
            buttonOne: "1",
            buttonTwo: "2",
            buttonThree: "3",
            buttonAdd: "+",
            buttonFour: "4",
            buttonFive: "5",
            buttonSix: "6",
            buttonMinus: "-",
            buttonSeven: "7",
            buttonEight: "8",
            buttonNine: "9",
            buttonTimes: "*",
            buttonReciprocal: "Reciprocal",
            buttonSquare: "Square",
            buttonStr: "Str",
            buttonDivide: "/",
            buttonPercent: "%",
            buttonCE: "CE",
            buttonC: "C",
            buttonDel: "Del",
            buttonMemoryClear: "Memory Clear",
            buttonMemoryRecall: "Memory Recall",
            buttonMemoryAdd: "Memory Add",
            buttonMemorySub: "Memory Sub",
            buttonMemoryStore: "Memory Store",
            buttonMemoryDisplay: "Memory Display"
        }

        # BUTTONS EVENTS
        for button, button_name in button_mapping.items():
            if button.Click(event):
                current_button = button_name

    # Printing the current button in the console (or use it wherever necessary)
    if current_button:
        print(f"Last clicked button: {current_button}")

    # Keyboard handling
    if keyboard.KeyState(pygame.K_ESCAPE) == "pressed":
        running = False  # Exit the program when ESC is pressed

    # Clearing the screen
    screen.Clear()

    if True == True:  # BUTTONS DRAW
        buttonAddSub.Draw(screen.screen)
        buttonZero.Draw(screen.screen)
        buttonComma.Draw(screen.screen)
        buttonEquals.Draw(screen.screen)

        buttonOne.Draw(screen.screen)
        buttonTwo.Draw(screen.screen)
        buttonThree.Draw(screen.screen)
        buttonAdd.Draw(screen.screen)

        buttonFour.Draw(screen.screen)
        buttonFive.Draw(screen.screen)
        buttonSix.Draw(screen.screen)
        buttonMinus.Draw(screen.screen)

        buttonSeven.Draw(screen.screen)
        buttonEight.Draw(screen.screen)
        buttonNine.Draw(screen.screen)
        buttonTimes.Draw(screen.screen)

        buttonReciprocal.Draw(screen.screen)
        buttonSquare.Draw(screen.screen)
        buttonStr.Draw(screen.screen)
        buttonDivide.Draw(screen.screen)

        buttonPercent.Draw(screen.screen)
        buttonCE.Draw(screen.screen)
        buttonC.Draw(screen.screen)
        buttonDel.Draw(screen.screen)

        buttonMemoryClear.Draw(screen.screen)
        buttonMemoryRecall.Draw(screen.screen)
        buttonMemoryAdd.Draw(screen.screen)
        buttonMemorySub.Draw(screen.screen)
        buttonMemoryStore.Draw(screen.screen)
        buttonMemoryDisplay.Draw(screen.screen)

    display.Draw(screen.screen)

    # Updating the screen
    screen.Refresh()

pygame.quit()








#ZADANIA na tydzień

# zrobić adventocode 23,24,25,26,27,28

# dokończyć górę menu kalkulatora i dla memory jak się najedzie to wyjaśnienia

# dokończyć logike z wpisywaniem w wyświetlacz

# skończyć logike działań

# zrobić menu z opcjami (typy kalkulatorów)jak się najedzie na przycisk w lewym górnym rogu

# zrobić możliwość ustawiania wielkości okienka
    # na początku że będzie można ustawić szerokość i wysokość jako xy
    # a przyciski wtedy będą się odpowiednio edytować
    # potem dać możliwość użytkownikowi poprostu poruszać okienkiem i myszką zmieniać wielkość okna

# w tym menu z opcjami dać: kalkulator_naukowy, ustawienia, autor (to wiadomo po co:)

# schemat działania kalkulatora naukowego to taki sam jak w aplikacji windowsa