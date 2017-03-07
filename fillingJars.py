#link to the challenge: https://www.hackerrank.com/challenges/filling-jars

n = raw_input("")
n = n.split()
toplam = 0

for i in xrange(int(n[1])):
    input = raw_input("")
    input = input.split()
    a = int(input[0])
    b = int(input[1])
    k = int(input[2])
    toplam += ((b+1) - a)*k

print toplam/int(n[0])
