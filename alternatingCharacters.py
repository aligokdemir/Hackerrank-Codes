#link to the challenge: https://www.hackerrank.com/challenges/alternating-characters

numberoftestcase = input()
counter = 0
counter2 = 0
for i in range(numberoftestcase):
    s = raw_input()        
    for c in xrange(len(s)-1):        
        if s[c] == s[c+1]:
            s[c:]
            counter2 += 1            
    
    print counter2
    counter2 = 0
