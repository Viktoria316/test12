'''
2023/10/12 00:00|Дополнительное практическое задание по модулю*
Дополнительное практическое задание по модулю: "Подробнее о функциях."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности


Задание "Раз, два, три, четыре, пять .... Это не всё?":
Все ученики урбана, без исключения, - очень умные ребята. Настолько умные,
что иногда по утру сами путаются в том, что намудрили вчера вечером.
Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые).
Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

Увидев это студент задался вопросом: "А есть ли универсальное решение
для подсчёта суммы всех чисел и длин всех строк?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре
(списку, словарю и т.д.) по-разному.

Ученику пришлось каждый раз использовать индексацию и обращение по ключам -
универсального решения для таких структур он не нашёл.

Помогите сокурснику осуществить его задумку.

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99


Примечания (рекомендации):
Весь подсчёт должен выполняться одним вызовом функции.
Рекомендуется применить рекурсивный вызов функции, для каждой
внутренней структуры.
Т.к. каждая структура может содержать в себе ещё несколько элементов,
можно использовать параметр *args
Для определения типа данного используйте функцию isinstance.

Файл с кодом (module3hard.py) прикрепите к домашнему заданию или
пришлите ссылку на ваш GitHub репозиторий с файлом решения.

'''

def calculate_structure_sum(data_structure):
    summa = 0
    for i in data_structure:
        if isinstance(i, (int, float)):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, (list, tuple, set)):
            summa += calculate_structure_sum(i)
        elif isinstance(i, (dict)):
            for key, value in i.items():
                if isinstance(key, str):
                    summa += len(key)
                if isinstance(value, str):
                    summa += len(value)
                if isinstance(key, int):
                    summa += key
                if isinstance(value, int):
                    summa += value
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
print(calculate_structure_sum(data_structure))

#73 интов
# 2
# 2
# 8
# 5
# 11
