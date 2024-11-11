import time
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





a = [12,4,3,6,7]
print(buble_sort(a))