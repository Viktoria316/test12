import math

class Figure:
    __sides = []
    __color = []
    filled = False



    def __init__(self, rgb, *side):
        self.color = list(rgb)
        self.side = side[0]
        self.filled = True

    # ===== Работа с цветом
    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    def _is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]

    # =====

    # ===== Работа со сторонами
    def __is_valid_sides(self, *args):
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def set_sides(self, *args):
        massive_list = []
        self.sides = list(args)
        if self.__is_valid_sides(self, *args):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                massive_list.append(self.side)
            self.sides = massive_list
            self.get_sides()

    def get_sides(self):
        self.__sides = self.sides
        return self.__sides

    def __len__(self):
        return self.side * self.sides_count

    # =====



class Circle(Figure):
    sides_count = 1
    __radius = None
    def set_radius(self):
        self.__radius = self.__len__() / (2 * math.pi)
        return self.__radius

    def get_square(self):
        self.set_radius()
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4



class Cube(Figure):
    sides_count = 12

    def set_side_lst(self):
        set_side_lst = []
        for element in range(self.sides_count):
            set_side_lst.append(self.sides)
        self.__sides = set_side_lst
        return self.__sides

    def get_volume(self):
        return self.side ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())





'''
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

# Дополнительные проверки
circle1.check_circle()
cube1.check_cube()

# Проверка треугольника
triangle1 = Triangle((100, 100, 100), 3, 4, 5)
triangle1.check_triangle()
triangle2 = Triangle((100, 100, 100), 1, 2, 5)
try:
    triangle2.check_triangle()
except ValueError as e:
    print(e)
'''
'''

a = '1010100010'
print(int(a, 2))

b = '254'
print(bin(224))

print(2 ** 11)
'''
'''
from threading import Thread
from random import randint
from time import sleep


class Table:

    def __init__(self, number, quest=None):
        self.number = number
        self.guest = quest


class Guest(Thread):

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, queue, *tables):
        super().__init__(queue, *tables)
        self.queue = queue


    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")



    def discuss_guests(self):
        def discuss_guests(self):
            while not self.queue.empty() or any(table.guest is not None for table in self.tables):

                for table in self.tables:
                    if table.guest and not table.guest.is_alive():
                        # Гость ушел, освобождаем стол
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None

                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()



'''
'''
import hashlib
import time


# Класс User
class User:
  def __init__(self, nickname, password, age):
    self.nickname = nickname
    self.password = self.hash_password(password)
    self.age = age

  # Метод для хэширования пароля
  def hash_password(self, password):
    return int(hashlib.sha256(password.encode()).hexdigest(), 16)

  def __repr__(self):
      return self.nickname


# Класс Video
class Video:
  def __init__(self, title, duration, adult_mode=False):
    self.title = title
    self.duration = duration
    self.time_now = 0
    self.adult_mode = adult_mode

  def __repr__(self):
    return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"


# Класс UrTube
class UrTube:
  def __init__(self):
    self.users = []  # Список пользователей
    self.videos = []  # Список видео
    self.current_user = None  # Текущий пользователь

  # Метод логина
  def log_in(self, nickname, password):
    hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
    for user in self.users:
      if user.nickname == nickname and user.password == hashed_password:
        self.current_user = user
        print(f"Пользователь {nickname} успешно вошел в систему.")
        return
    print("Неправильный логин или пароль.")

  # Метод регистрации
  def register(self, nickname, password, age):
    for user in self.users:
      if user.nickname == nickname:
        print(f"Пользователь {nickname} уже существует")
        return
    new_user = User(nickname, password, age)
    self.users.append(new_user)
    self.current_user = new_user
  def log_out(self):
    print(f"Пользователь {self.current_user.nickname} вышел из системы.")
    self.current_user = None

  # Метод добавления видео
  def add(self, *videos):
    for video in videos:
      if any(v.title == video.title for v in self.videos):
        print(f"Видео '{video.title}' уже существует.")
      else:
        self.videos.append(video)

  # Метод для поиска видео по ключевому слову
  def get_videos(self, search_term):
    search_term = search_term.lower()
    return [video.title for video in self.videos if search_term in video.title.lower()]

  # Метод для просмотра видео
  def watch_video(self, title):
    if not self.current_user:
      print("Войдите в аккаунт, чтобы смотреть видео")
      return


    for video in self.videos:
      if video.title == title:
        if video.adult_mode and self.current_user.age < 18:
          print("Вам нет 18 лет, пожалуйста покиньте страницу")
          return
        for second in range(video.time_now + 1, video.duration + 1):
          print(second, end=' ')
          time.sleep(1)
          video.time_now = second
        print("\nКонец видео")
        video.time_now = 0
        return


# Пример использования
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
'''
'''

import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == User('').hash_password(password):
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в аккаунт.")
                return
        print("Неправильный никнейм или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошёл в аккаунт.")

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_term):
        return [video.title for video in self.videos if search_term.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу.")

                    return

                for current_time in range(video.duration):
                    print(f"Прошло секунд: {current_time + 1}")
                    time.sleep(1)
                print("Конец видео.")
                return

        print("Видео не найдено.")


# Пример кода для проверки
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

'''
'''
from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.GREEN + 'зеленый текст')
print(Back.YELLOW + 'на желтом фоне')
print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
print('обычный текст')
class Human:

    def say(self):
        print("Я в хьюмон")


class Student(Human):

    def do_homework(self):
        print("Я в студенте")

class Homework(Student):

    def math_(self):
        print('я в хомворке')

x = Homework()
x.say()



'''

'''

class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal, Plant):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal, Plant):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)




'''









#
# def calculate_structure_sum(data_structure):
#     summa = 0
#     for i in data_structure:
#         if isinstance(i, (int, float)):
#              print(i)
#              summa += i
#         elif isinstance(i, str):
#             summa += len(i) + 1
#         elif isinstance(i, (list, tuple, set, dict)):
#             summa += calculate_structure_sum(i)
#         else:
#             pass
#     return summa
#
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
# print(calculate_structure_sum(data_structure))
#
# #73 интов
# # 2
# # 2
# # 8
# # 5
# # 11
#
#
# simple(data_structure)

'''
def calculate_structure_sum(data_structure):
  """
  Рекурсивно подсчитывает сумму чисел и длин строк в вложенных структурах данных.

  Args:
    data_structure: Вложенная структура данных для анализа.

  Returns:
    int: Сумма всех чисел и длин строк в структуре данных.
  """
  total_sum = 0
  for element in data_structure:
    if isinstance(element, (int, float)):
      total_sum += element
    elif isinstance(element, str):
      total_sum += len(element) + 1
    elif isinstance(element, (list, tuple, set, dict)):
      total_sum += calculate_structure_sum(element)  # Рекурсивный вызов
    else:
      pass  # Пропускаем элементы других типов

  return total_sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99






'''
'''
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print(get_multiplied_digits(40203))
'''

'''
def calculate_structure_sum(data_structure):
    summa = 0
    for i in data_structure:
        if isinstance(i, (int, float)):
            summa += i
        elif isinstance(i, str):
            summa += len(i) + 1
        elif isinstance(i, (list, tuple, set, dict)):
            summa += calculate_structure_sum(i)
        else:
            pass
    return summa

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


# #data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

result = calculate_structure_sum(data_structure)
print(result)


'''



'''
def password(first_number):
    needed_pass = ''
    for k in range(1, first_number):
        for v in range(k + 1, first_number):
            if first_number % (k + v) == 0:
                needed_pass += str(k) + str(v)
    return needed_pass

print('Число на первом камне: ')
print(password(int(input())))
'''


'''
Домашнее задание по уроку "Распаковка параметров и параметры функции"

Цель задания: Освоить создание функций с параметрами по умолчанию и
практику вызова этих функций с различным количеством аргументов.

Задача "Распаковка":

1.Функция с параметрами по умолчанию:
Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
Функция должна выводить эти параметры.
Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
'''


'''
def print_params(a = 1, b = 'строка', c = True):
  print(a, b, c)

print(1)
print(print_params()) # Вывод: 1 строка True. Выводит дефолтные значения

print(2)
print(print_params(1, 2, 3)) # Вывод: 1 2 3. Выводит заданные значения

print(3)
print(print_params(4, 5)) # Вывод: 4 5 True. Заменяет значения первых двух параметров a, b

print(4)
print_params(b = 25) # Работает, заменяя дефолтное значение b на значение 25

print(5)
print_params(c = [1,2,3]) # Работает, заменяя дефолтное значение c на значение [1,2,3]

print(6)
# Не работает, так как в принимающей функции заданных параметров меньше, чем мы ей передаем
# print(print_params(6, 7, 8, 9))
'''

'''
2.Распаковка параметров:
Создайте список values_list с тремя элементами разных типов.
Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, 
и значениями разных типов.
Передайте values_list и values_dict в функцию print_params, используя распаковку параметров 
(* для списка и ** для словаря).
'''
'''
# values_list = [1, 'string', True]

import random

def find_pairs(first_number):
    pairs = []
    for i in range(1, first_number):
        for j in range(1, first_number):
            if (i + j) % first_number == 0:
                pairs.append((i, j))
    return pairs

while True:
  first_number = random.randint(3, 20)  # Случайное число от 3 до 20
  print("Число в первой вставке:", first_number)
  pairs = find_pairs(first_number)
  if pairs:
      print("Пары чисел для второй вставки:", pairs)
      break 
  else:
      print("Для этого числа пар нет.")

'''


'''



import random

def find_pairs(number):
  pairs = []
  for i in range(1, number):
    for j in range(i, number):
      if (i + j) % number == 0:
        pairs.append((i, j))
  return pairs


number = int(input("Введите число из первой вставки (от 3 до 20): "))


if number < 3 or number > 20:
  print("Неверное число. Введите число от 3 до 20.")
else:
  pairs = find_pairs(number)
  if pairs:
    result = []
    for pair in pairs:
      result.extend(pair)
    print("Пароль:", *result)
  else:
    print("Для этого числа пар нет.")







'''



'''
def single_root_words(root_word, *other_words):
    same_words = []
    print(root_word)
    print(*other_words)
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
'''
'''

def find_pairs(number):
  pairs = []
  for i in range(1, number):
    for j in range(i, number):
      if (i + j) % number == 0:
        pairs.append((i, j))
  return pairs

number = int(input("Введите число из первой вставки (от 3 до 20): ")) # Первая?? вставка

if number < 3 or number > 20:
  print("Неверное число. Введите число от 3 до 20.")
else:
  pairs = find_pairs(number)
  if pairs:
    result = []
    for pair in pairs:
      result.extend(pair)
    print("Пароль:", *result)
  else:
    print("Для этого числа пар нет.")



'''













'''
2023/10/05 00:00|Домашняя работа по уроку "Пространство имен и способы вызова функции"
Цель: закрепить знание использования параметров в функции и знания из предыдущих модулей.

Задача("Однокоренные"):
Напишите функцию single_root_words, которая принимает одно
обязательное слово в параметр root_word, а далее неограниченную
последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех
слов списка other_words, которые содержат root_word или наоборот root_word
содержит одно из этих слов. После вернуть список same_words в качестве результата
своей работы.

Пункты задачи:
Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
Создайте внутри функции пустой список same_words, который пополнится нужными словами.
При помощи цикла for переберите предполагаемо подходящие слова.
Пропишите корректное относительно задачи условие, при котором добавляются слова в
результирующий список same_words.
После цикла верните образованный функцией список same_words.
Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей занчение.
Пример результата выполнения программы:

Исходный код:
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

Вывод на консоль:
['richiest', 'orichalcum', 'richies']
['Able', 'Disable']

'''

'''
def single_root_words(root_word, *other_words):
    same_words = []
    for i in same_words:
        


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)

'''






'''
Задача "Матрица воплоти":
Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.

Пункты задачи:
Объявите функцию get_matrix и напишите в ней параметры n, m и value.
Создайте пустой список matrix внутри функции get_matrix.
Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
В первом цикле добавляйте пустой список в список matrix.
Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
Во втором цикле пополняйте ранее добавленный пустой список значениями value.
После всех циклов верните значение переменной matrix.
Выведите на экран(консоль) результат работы функции get_matix.

'''

'''
def get_matrix(n, m, value):
    matrix = []
    for a in range(n):
        print(1.0)
        print(n)
        print(1.0)
        # matrix.append([a][a])
        matrix.append([])
        print(2.0)
        print(matrix)
        print(2.0)
        print(matrix)
        for b in range(m):
            print(4.0)
            print(b)
            print(4.0)
            matrix[a].append(value)
            print(matrix)
    return matrix

result1 = get_matrix(2, 2, 10)
print(result1)
#print(get_matrix(2, 2,10))


'''
'''
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
'''

# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# students_s = sorted(students)
# print(students_s)
# numbers = [1, 2, 3, 4, 5]
# primes = []
# not_primes = []
#
# def is_prime(num):
#   """
#   Функция проверки простого числа.
#   """
#   if num <= 1:
#     return False
#   for i in range(2, int(num*0.5) + 1):
#     if num % i == 0:
#       return False
#   return True
#
# for number in numbers:
#
#   if is_prime(number):
#     primes.append(number)
#   elif number == 1:
#     continue
#   else:
#     not_primes.append(number)
#
# print(f"Простые числа: {primes}")
# print(f"Не простые числа: {not_primes}")