
import random
t= 10

def buble_sort(a):
    n=len(a)
    x = True
    while x:
        x = False
        j = 0
        for i in a:
            j = j+1
            for j in range(n-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    x = True
    return a




a = [random.randint(0,t-1) for i in range(t-1)]

buble_sort(a)
print()











oporn=a[random.randint(0, t-1)]
def qsort(a):
    m=[]
    n=[]
    for i in a:
        if oporn >= i:
            m.append(i)
        elif oporn<i:
            n.append(i)
            

