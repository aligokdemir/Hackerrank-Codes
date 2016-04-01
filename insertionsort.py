__author__ = 'ali'

def insertionSort(ar):
    for i in range(0,len(ar)):
        x = ar[i]
        j = i-1
        while j >= 0 and ar[j]>x:
            ar[j+1] = ar[j]
            for _ in ar:
                print _,
            print ""
            j -= 1
        ar[j+1] = x
    return ar
m = input()
ar = [int(i) for i in raw_input().strip().split()]

insertionSort(ar)
for _ in ar:
    print _,
