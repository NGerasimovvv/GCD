import math
from timeit import default_timer as timer

start = timer()

#инициализация
a = 39955052105692998713
b = 64814593495702640189

g = 1 

i = 1

vivod = []

j = 0

#пока оба числа четные, делим их на два и увеличиваем g в 2 раза
while a % 2 == 0 and b % 2 == 0:

    a = a // 2
    b = b // 2 
    g = g*2
    
    print ('#%d a = %d  b = %d g = %d' %(i,a,b,g))

    i = i+1

#инициализация

u = a
v = b

A = 1
B = 0
C = 0
D = 1

print ('#%d u = %d v = %d A = %d B = %d C = %d D = %d' %(i,u,v,A,B,C,D))

i = i + 1

#пока u не будет равно 0
while u != 0:
    #если u четное
    while u % 2 == 0:
        #делим u на 2
        u = u // 2
        #изменяем коэффициенты
        if A % 2 == 0 and B % 2 == 0:
            A = A // 2
            B = B // 2
        else:
            A = (A + b) // 2
            B = (B - a) // 2

        vivod.append((i,u,v,A,B,C,D))

        i = i + 1

    #если v четное
    while v % 2 == 0:
        #делим v на 2
        v = v // 2
        #изменяем коэффициенты
        if C % 2 == 0 and D % 2 == 0:
            C = C // 2
            D = D // 2
        else:
            C = (C + b) // 2
            D = (D - a) // 2

        vivod.append((i,u,v,A,B,C,D))

        i = i + 1

    #в зависимости от значений v и u меняем коэффициенты
    if u >= v:
        u = u - v
        A = A - C 
        B = B - D 
    else:
        v = v - u
        C = C - A
        D = D - B

    vivod.append((i,u,v,A,B,C,D))

    i = i + 1

d = g*v
x = C 
y = D
print("Time 1st program: {0:.10f} secs".format(timer() - start))

for j in range(len(vivod)):
    print ('#%d u = %d v = %d A = %d B = %d C = %d D = %d' %(vivod[j]))

print ('NOD = %d x = %d y = %d' %(d,x,y))

print ('a*x + b*y = %d*%d + %d*%d = %d' %(a, x, b, y, (a * x + b * y)))

