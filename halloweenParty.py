#link to the challenge: https://www.hackerrank.com/challenges/halloween-party

testcase = int(raw_input(""))
for i in range (0,testcase):
    degisken = int(raw_input(""))
    if degisken % 2 == 0:
        degisken /= 2
        print degisken*degisken
    else:
        degisken /= 2
        print degisken*(degisken+1)
