import math
from timeit import default_timer as timer

start = timer()

#инициализация

a = 3149656550306601505505231786181628854803098311861097173903261996018613761976379
b = 8672790786542571628484447306811660674381735368203185296287291066679593367042721

r = []
r.append(a)
r.append(b) 

x =[]
x.append(1)
x.append(0)

y =[]
y.append(0)
y.append(1)

q = []

vivod = []

i = 1
j = 0

while 1:

    #делим r_(i-1) на r_(i) с остатком
    q.append(r[i-1] // r[i]) #целая часть
    r.append(r[i-1] % r[i])   #остаток

    #если остаток 0, то выходим из цикла
    if r[i+1] == 0:
        break
    #иначе меняем коэффициенты x и y, выводим итерацию цикла и увеличиваем i на 1
    else:
        x.append(x[i-1] - q[i-1] * x[i])
        y.append(y[i-1] - q[i-1] * y[i])
        vivod.append((i,r[i+1], q[i-1], x[i], y[i]))
        i = i + 1


print("Time 1st program: {0:.10f} secs".format(timer() - start))

for j in range(len(vivod)):
    print('#%d r = %d q = %d x = %d and y = %d' %(vivod[j]))

print ('#%d r = %d q = %d x = %d and y = %d' %(i,r[i], q[i-1], x[i], y[i]))

print ('NOD = %d x = %d y = %d' %(r[i], x[i], y[i]))

print ('a*x + b*y = %d*%d + %d*%d = %d' %(a, x[i], b, y[i], (a * x[i] + b * y[i])))