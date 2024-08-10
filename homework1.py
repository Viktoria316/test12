name = 'это моя строка'
# name2 = 'это новая строка'


'''
1. Задача «Часть от целого».
Описание: вывести указанную часть текста.
Пример: дано предложение «Сейчас на Земле появился новый вид роботов.
Раньше их называли „железной оравой “, 
но это не очень точное определение». Требуется вывести только первое предложение.
'''
a = "Сейчас на Земле появился новый вид роботов. Раньше их называли „железной оравой “, но это не очень точное определение"
print(a[:43]) #1


'''
2. Задача «Палиндром».
Описание: вывести слово в обратном порядке.
Пример: дано слово «радар».
Требуется вывести его в обратном порядке. 
Помимо этого проверьте указанный пример для слова: “норма” 
'''
a = 'радар'
b = 'норма'
print(a[::-1]) #2
print(b[::-1]) #2


'''
3.Задача «Равные части».
Описание: разделить заданную строку пополам на две части и поменять их местами.
Пример: дана строка «кенгуру». Требуется получить «урукенг».
'''
# print(name[2:4]) #3
a = 'кенгуру'
b = a[:4]
c = a[4:]
print(a[:4])
print(a[4:])
print(c + b)
print(a[4:] + a[:4])



'''
4. Задача «Четные и нечетные».
Описание: используя срезы, вывести все чётные и нечётные символы заданной строки.
Пример: дана строка «нейропрограммирование». Требуется вывести «нйорграмрвне ерпормиоаи».
'''
a = 'нейропрограммирование'
b = a[0::2]
c = a[1::2]
print(b + ' ' + c)


'''
5.Задача «Обратный порядок».
Описание: вывести заданную строку в обратном порядке без первого и последнего символа.
Пример: дана строка «нейропластичность». Требуется получить «тсончитсалпорйе».
'''
# print(len(name)) #5
a = 'нейропластичность'
b = a[1:-1]
c = b[::-1]
print(c)