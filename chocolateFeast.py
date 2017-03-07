#link to the challenge: https://www.hackerrank.com/challenges/chocolate-feast

T = int(raw_input())
for i in range (0,T):
    param,fiyat,kampanya = [int(x) for x in raw_input().split(' ')]
    a = copsayisi = param / fiyat
    while copsayisi >= kampanya:
        a += copsayisi / kampanya
        b = copsayisi % kampanya
        copsayisi = copsayisi / kampanya
        b += copsayisi % kampanya
        if  b >= kampanya:
            a += b / kampanya
    print a
