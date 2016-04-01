__author__ = 'ali'

x = raw_input()
x = x.split()

first = int(x[0])
sec = int(x[1])

for i in xrange(int(x[2])-2):
    summ = sec**2 + first
    first = sec
    sec = summ

print summ
