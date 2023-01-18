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
# import math
# numbers_before_comma=int((input("Введите число знаков после запятой ")))
# print(round(math.pi,numbers_before_comma))
# Задача 4*. Даны два файла, в каждом из которых находится 
# запись многочлена. Найдите сумму данных многочленов.
# Результат: 8x^2 + 4x + 8
letter=[]
first=open('first.txt', encoding='utf8').read().split(' ')
second=open('second.txt', encoding='utf8').read().split(' ')
for i,j in zip(first,second):
    if type(i)==str or type(j)==str:
        if i.find('^')!=-1 or j.find('^')!=-1:
            if i[i.find('^')-1]==j[j.find('^')-1] and i[i.find('^')+1]==j[j.find('^')+1]:
                print(int(i[i.find('^')-2])+int(j[j.find('^')-2]))
        elif i.find('x')!=-1 or j.find('x')!=-1:
            if i[i.find('x')]-1=='x' or j[j.find('x')]-1:
                print(1x)
                else:
                print(int(i[i.find('x')]-1)+int)

        
#             if i.find('^')!=-1:
#                 for j in i:
#                     power=i[1+(i.find('^'))]
#                     mult=i[(i.find('^'))-1]
#                     print(power)
                    
#             else:
#                 i[i.find('x')-1]
#                 print(i)

        
    
#     if type(i)== int and type(j)==int:
#         k=i+j
    
        
print(first)
print(second)

