#link to the question: https://www.hackerrank.com/challenges/is-fibo

sifirinci, birinci = 0, 1
liste = [0, 1]
counter = 0
noftestcase = int(raw_input(""))
a = 0


while counter < 100:
    sifirinci, birinci = birinci, (sifirinci + birinci)         
    liste.append(sifirinci + birinci)
    counter += 1

while a < noftestcase:
    q = int(raw_input(""))
    if q in liste:
        print "IsFibo"
    else:
        print "IsNotFibo"
    a += 1
