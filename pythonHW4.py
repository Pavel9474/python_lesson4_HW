# Задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит список 
# простых множителей числа N.
# def simplemulty(n):
#     simplemulty_List = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             simplemulty_List.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         simplemulty_List.append(n)
#     return simplemulty_List
# print(simplemulty(int(input('Введите число: '))))

# Задача 2. В первой строке файла находится информация об 
# ассортименте мороженного, во второй - информация о том, 
# какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.
# icecream_list_in_storage=open('icecream.txt', 'r', encoding='utf8').readline().split(', ')
# print(icecream_list_in_storage)
# icecream_list_in_storage=set(icecream_list_in_storage)
# icecream_list_in_store=open('icecream.txt', 'r', encoding='utf8').read().split('\n')[1]
# print(icecream_list_in_store)
# icecream_list_in_store=set(icecream_list_in_store.split(', '))
# print(icecream_list_in_storage.difference(icecream_list_in_store))
# Задача 3. Выведите число π с заданной точностью. Точность выводится в 
# виде десятичной дроби.
import math
numbers_before_comma=int((input("Введите число знаков после запятой ")))
print(round(math.pi,numbers_before_comma))
# Задача 4*. Даны два файла, в каждом из которых находится 
# запись многочлена. Найдите сумму данных многочленов.


