__author__ = 'ali'

testcase = int(raw_input())
counter = 0
for i in range (testcase):
    orstr = raw_input()
    cpystr = orstr[::-1]
    for x in range(len(orstr)-1):
        if abs(ord(orstr[x+1]) - ord(orstr[x])) == abs(ord(cpystr[x+1]) - ord(cpystr[x])):
            counter += 1
        else:
            print "Not Funny"
            break
    if counter == len(orstr)-1:
        print "Funny"
    counter = 0
