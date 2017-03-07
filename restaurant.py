#link to the challenge: https://www.hackerrank.com/challenges/restaurant

testcase = int(raw_input(""))

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

for i in xrange(testcase):
    n = raw_input("")
    n = n.split()
    answer = (int(n[0])*int(n[1])) / (gcd(int(n[0]), int(n[1])))**2
    print answer   
