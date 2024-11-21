import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        self.__validate_sides()

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __validate_sides(self):
        if not all(isinstance(side, int) and side > 0 for side in self.__sides) or len(self.__sides) != self.sides_count:
            raise ValueError("Некорректные значения сторон.")

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
            self.__validate_sides()

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius**2

    def check_circle(self):
        if not isinstance(self.__radius, float) or self.__radius <= 0:
            raise ValueError("Некорректный радиус.")

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        s = sum(self.__sides) / 2
        return math.sqrt(s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2]))

    def check_triangle(self):
        if not all(isinstance(side, int) and side > 0 for side in self.__sides):
            raise ValueError("Некорректные значения сторон.")
        if not (self.__sides[0] + self.__sides[1] > self.__sides[2] and
                self.__sides[0] + self.__sides[2] > self.__sides[1] and
                self.__sides[1] + self.__sides[2] > self.__sides[0]):
            raise ValueError("Некорректные значения сторон: не соблюдается неравенство треугольника.")

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = [sides[0]] * self.sides_count

    def get_volume(self):
        return self.__sides[0]**3

    def check_cube(self):
        if not isinstance(self.__sides[0], int) or self.__sides[0] <= 0:
            raise ValueError("Некорректное значение стороны.")

# Проверка
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())