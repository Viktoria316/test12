'''
Задача «Сложная сдача».
Описание: Одна из задач, в которой лучше исключить человеческий фактор, — подсчёт сдачи.
Определите, какую сдачу нужно выдать тому, кто купил 4,5кг черешни по цене 34 руб/кг
'''

price = 34
mas = 4.5
mas1 = 5
purchare = (mas1 * price)
purchare1 = (mas * price)
# print(purchare)
# print(purchare1)
purchare3 = purchare - purchare1
print('Сдача: ' + str(purchare3))


'''
Задача «Сдача всем».
Описание: Кроме ягод в магазине продаётся множество других товаров,
которые продаются на развес. Давайте автоматизируем расчёт сдачи и для них!
'''
print('Цена ')
price = input()
print('Масса ')
mas = input()
print('количество денег у покупателя ')
money = input()
purchare = int(mas) * int(price)
purchare1 = int(money) - int(purchare)
print('Сдача: ' + str(int(purchare1)))

'''
Задача «Работаем с выводом данных».

Описание: Сдачу посчитать, конечно, все могут, но красивый чек напечатать — не так просто.
'''
print('название товара ')
product_name = input()

print('Цена ')
price = input()

print('Вес товара ')
mas = input()

print('Количество денег у покупателя ')
money = input()

purchare = int(mas) * int(price)
purchare1 = int(money) - int(purchare)

print('Чек ' + product_name + ' - ' + mas + 'кг' + ' - ' + price + 'руб/кг Итого: ' + str(purchare) + 'руб Внесено: ' + money + 'руб Сдача: ' + str(purchare1) + 'руб' )


'''
Задача «Самая простая задача на свете».
Описание: Давай сделаем что-то действительно интересное.
'''
N = input('Одно натуральное число ?')
B = ('Купи конструктор!' * int(N))
print(B)

'''
Задача «Автоматизируем простоту!».
Описание:
Формат ввода
В первой строке записано одно натуральное число ? Во второй строке записано любимое дело.
Формат вывода
? строк вида: Обожаю писать "<любимое дело>"!
'''
N = input('Одно натуральное число ? ')
B = input('Введите ваше любимое дело: ')
C = (str(B) * int(N))
D = ('Обожаю писать "' + C + '"!')
print(D)








