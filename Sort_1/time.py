import time
import alllesort1
import random
t= 10**5

a = [random.randint(0,t-1) for i in range(t-1)]
Start = time.time()
alllesort1.insertion_sort(a)
Finush = time.time()
Res_msec = (Finush - Start)*1000
print(Res_msec)