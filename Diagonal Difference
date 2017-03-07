#link to the challenge: https://www.hackerrank.com/challenges/diagonal-difference

diagonal = int(raw_input())
a = []
for i in xrange(diagonal):
    liste = raw_input()
    liste = liste.split()
    a.append(liste)

leftsum = 0

for j in xrange(diagonal):
    leftsum += int(a[j][j])

rightsum = 0

sutun = diagonal-1
satir = 0
while(diagonal):
    rightsum += int(a[satir][sutun])
    satir += 1
    sutun -= 1
    diagonal -= 1

print abs(leftsum-rightsum)
