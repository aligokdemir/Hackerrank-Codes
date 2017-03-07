#link to the challenge: https://www.hackerrank.com/challenges/find-digits

testcase = int(raw_input())
testcasecount = 0

while testcasecount < testcase:
    number = numbertemp = int(raw_input())
    digitcounter = 0
    while numbertemp > 0:
        digit = numbertemp % 10
        if digit == 0:   
            numbertemp = numbertemp / 10
        else:
            if number % digit == 0:
                digitcounter += 1
            numbertemp = numbertemp / 10
    print digitcounter
    testcasecount += 1
