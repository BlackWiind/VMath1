#Линейная интерполяция

from math import cos
from array import *

h = 0.009
some_max = 15
c = 5
x = c
fx = array('d', [])
fy = array('d', [])


def calc(value: float) -> float:
    answer = c ** 3 * cos((value + 10 * c) / c)
    return round(answer, 4)


print("\t _______________________________\t\t")
print("\t|\tТаблица значений функций|\t")
print("\t|_______________________________|\t\t")
for i in range(some_max):
    fx.append(x)
    fy.append(calc(x))
    print("\t| x=%.4f" % x, "\t | y=%.4f" % fy[i], "\t|")
    x += h
x = c
print("\t _______________________________\t\n")
print("\t ___________________________________\t\t")
print("\t| Результаты линейной интерполяции  |")
print("\t|___________________________________|\t\t")
print("\t|     X      | Y(прибл) | Y(точное) |\t\t")
print("\t|___________________________________|\t\t")
for i in range(some_max - 1):
    x += 0.6 * h
    for j in range(len(fx)):
        if x < fx[j] and x > fx[j-1]:
            answer = fy[j] + ((x - fx[j]) / h) * (fy[j] - fy[j-1])
            print("\t| %.4f" % x, "    |%.4f" % answer, "   |  ", calc(x), " |")
            break
    x += 0.6 * h
input("Нажмите любую клавишу...")
