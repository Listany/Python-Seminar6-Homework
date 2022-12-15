# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst=list(map(int,input("Задайте последовательность чисел: ").split()))

# def get_uniq_numbers(lst):
#     uniq_lst=[]
    
#     for i in lst:
#         if i in uniq_lst:
#             continue
#         else:
#             uniq_lst.append(i)
    
#     return uniq_lst

# print(get_uniq_numbers(lst))
#lst = set(lst)

lst_uniq=[]
for i in lst:
    if i not in lst_uniq:
     lst_uniq.append(i)
print(lst)
print(lst_uniq)