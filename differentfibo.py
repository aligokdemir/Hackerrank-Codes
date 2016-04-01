__author__ = 'ali'

#to visit challenge page: https://www.hackerrank.com/challenges/fibonacci-modified

x = raw_input()
x = x.split()

first = int(x[0])
sec = int(x[1])

for i in xrange(int(x[2])-2):
    summ = sec**2 + first
    first = sec
    sec = summ

print summ
