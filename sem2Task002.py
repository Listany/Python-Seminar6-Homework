# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. 
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math

num = int(input("Введите число: "))

res = list(math.factorial((i)) for i in range(1, num+1))
print(res)


# mult_arr=[]
# count=1

# for i in range(0, num):
#     count=1
#     for j in range (1, i +2):
#         count=count*j
#     mult_arr.append(count)    

# print(mult_arr)

