
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











# oporn=a[random.randint(0, t-1)]
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1
x = int(len([1,2,3,4,54,6,7,8,47,2,52,545,24,]))-1
print(quick_sort([1,2,3,4,54,6,7,8,47,2,52,545,24,],0, x))





def selection_sort(a):
    for i in range(len(a) - 1):
        imin = i
        for j in range(i + 1, len(a)):
            if a[j] < a[imin]:
                imin = j
        a[i], a[imin] = a[imin], a[i]







def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j = i - 1
        while j >= 0 and a[j] > tmp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = tmp

