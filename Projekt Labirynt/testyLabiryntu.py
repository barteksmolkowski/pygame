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