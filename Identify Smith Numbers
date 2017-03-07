#link to the challenge: https://www.hackerrank.com/challenges/identify-smith-numbers

n = int(raw_input())
temp = n
primef = []

while(n%2 == 0):
    primef.append(2)
    n /= 2
for i in xrange(3,int(n**.5),2):
    while(n%i == 0):
        primef.append(i)
        n = n/i
if(n>2):
    primef.append(n)
summ = 0
while(temp):
    summ += temp%10
    temp/=10
summ2 = 0
for a in xrange(len(primef)):
    temp2 = primef[a]
    while(temp2):
        summ2 += temp2%10
        temp2/=10

if(summ == summ2): print 1
else: print 0
