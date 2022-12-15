# на вход подается строка с матем выражением - сделать решение этой строки(результат)


#print(eval('2 * 3 / 6'))

str_1 = "10 / 2 * 3 + 5 - 3"
num = str_1.split()
print(num)
tmp=0

while len(num) != 1:
    while '*' in num or '/' in num:
        if num.count('*') > 0 and num.count('/') > 0:
             if num.index('/') > num.index('*'):
                 num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                 num.pop(num.index('*') + 1)
                 num.pop(num.index('*'))
                                  
             else:                 
                 num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                 num.pop(num.index('/') + 1)
                 num.pop(num.index('/'))
                      
        else:
            if '*' in num:
                 num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                 num.pop(num.index('*') + 1)
                 num.pop(num.index('*'))
                  
            else:
                 num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                 num.pop(num.index('/') + 1)
                 num.pop(num.index('/'))
                 
    while  '+' in num or '-' in num:    
        if '+' in num:
            num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
            num.pop(num.index('+') + 1)
            num.pop(num.index('+'))
        if '-' in num:
            num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
            num.pop(num.index('-') + 1)
            num.pop(num.index('-'))
                
                  
print(num)     
            
            
#print(tmp)
#print(str_lst.index('*'))
