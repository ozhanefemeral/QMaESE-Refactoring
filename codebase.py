import math

class Figura2D:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def oblicz_pole(self):
        raise NotImplementedError("Metoda abstrakcyjna")

    def check_collision(self, other_shape):
        return False

class Ksztalt2D(Figura2D):
    def __init__(self, nazwa, x, y, dlugosc, szerokosc):
        super().__init__(nazwa)
        self.x = x
        self.y = y
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    @property
    def center(self):
        return self.x + self.dlugosc / 2, self.y + self.szerokosc / 2

    def check_collision(self, other_shape):
        if not isinstance(other_shape, Ksztalt2D):
            raise TypeError("other_shape must be an instance of Ksztalt2D")

        # Check if the shapes overlap in x and y directions
        if self.x < other_shape.x + other_shape.dlugosc and self.x + self.dlugosc > other_shape.x:
            if self.y < other_shape.y + other_shape.szerokosc and self.y + self.szerokosc > other_shape.y:
                return True

        return False

class Ksztalt3D(Figura2D):
    def __init__(self, nazwa, x, y, z, dlugosc, szerokosc, wysokosc):
        super().__init__(nazwa)
        self.x = x
        self.y = y
        self.z = z
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    @property
    def center(self):
        return self.x + self.dlugosc / 2, self.y + self.szerokosc / 2, self.z + self.wysokosc / 2

    def carpisma_kontrolu(self, diger_sekil):
        if not isinstance(diger_sekil, Ksztalt3D):
            raise TypeError("diger_sekil musi być instancją klasy Ksztalt3D")

        # Check if the shapes have the same center
        if self.center != diger_sekil.center:
            return False

        # Check if the shapes overlap in x, y, and z directions
        if self.x < diger_sekil.x + diger_sekil.dlugosc and self.x + self.dlugosc > diger_sekil.x:
            if self.y < diger_sekil.y + diger_sekil.szerokosc and self.y + self.szerokosc > diger_sekil.y:
                if self.z < diger_sekil.z + diger_sekil.wysokosc and self.z + self.wysokosc > diger_sekil.z:
                    return True

        return False

class Kula(Ksztalt3D):
    def __init__(self, nazwa, x, y, z, promien):
        super().__init__(nazwa, x, y, z, 0, 0, 0)
        self.promien = promien

    def oblicz_objetosc(self):
        return (4 * math.pi * self.promien ** 3) / 3

class Szescian(Ksztalt3D):
    def __init__(self, nazwa, x, y, z, krawedz):
        super().__init__(nazwa, x, y, z, 0, 0, 0)
        self.krawedz = krawedz

    def oblicz_objetosc(self):
        return self.krawedz ** 3

class Kwadrat(Figura2D):
    def __init__(self, nazwa, dlugosc, szerokosc):
        super().__init__(nazwa)
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def oblicz_pole(self):
        return self.dlugosc * self.szerokosc

    def check_collision(self, other_shape):
        if not isinstance(other_shape, Figura2D):
            raise TypeError("other_shape must be an instance of Figura2D")

        # Check if the shapes have the same center
        if self.center != other_shape.center:
            return False

        # Check if the shapes overlap in x and y directions
        if self.x < other_shape.x + other_shape.dlugosc and self.x + self.dlugosc > other_shape.x:
            if self.y < other_shape.y + other_shape.szerokosc and self.y + self.szerokosc > other_shape.y:
                return True

        return False

class Trojkat(Figura2D):
    def __init__(self, nazwa, podstawa, wysokosc):
        super().__init__(nazwa)
        self.podstawa = podstawa
        self.wysokosc = wysokosc

    def oblicz_pole(self):
        return 0.5 * self.podstawa * self.wysokosc

    def sprawdz_kolizje(self, druga_figura):
        if not isinstance(druga_figura, Figura2D):
            raise TypeError("druga_figura musi być instancją klasy Figura2D")

        # Get the bounding box coordinates for the first triangle
        x1 = min(0, self.podstawa, self.podstawa / 2)
        y1 = min(0, 0, self.wysokosc)

        x2 = max(0, self.podstawa, self.podstawa / 2)
        y2 = max(0, 0, self.wysokosc)

        # Get the bounding box coordinates for the second triangle
        x3 = min(0, druga_figura.podstawa, druga_figura.podstawa / 2)
        y3 = min(0, 0, druga_figura.wysokosc)

        x4 = max(0, druga_figura.podstawa, druga_figura.podstawa / 2)
        y4 = max(0, 0, druga_figura.wysokosc)

        # Check if the bounding boxes overlap
        if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
            return False
        else:
            return True

def main():
    # Figury 2D
    prostokat = Kwadrat("prostokat", 10, 5)
    print("Pole prostokąta:", prostokat.oblicz_pole())

    trojkat = Trojkat("trójkąt", 10, 12)
    print("Pole trójkąta:", trojkat.oblicz_pole())

    # Figury 3D
    szescian = Szescian("sześcian", 0, 0, 0, 6)
    print("Objętość sześcianu:", szescian.oblicz_objetosc())

    kula = Kula("kula", 0, 0, 0, 4)
    print("Objętość kuli:", kula.oblicz_objetosc())

if __name__ == "__main__":
    main()
