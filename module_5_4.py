'''
Домашнее задание по уроку "Различие атрибутов класса и экземпляра"
Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создай  те новый класс Buiding с атрибутом total
Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных
объектов класса Building total
В цикле создайте 40 объектов класса Building и выведите их на экран командой print
Полученный код напишите в ответ к домашнему заданию
'''

class Buiding():
    total = 0
    def __init__(self):
        Buiding.total += 1


buildings = [Buiding() for i in range(40)]
for building in buildings:
    print(building)
