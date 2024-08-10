
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