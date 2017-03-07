#link to the challenge: https://www.hackerrank.com/challenges/pangrams

enter = raw_input().lower()
char = "abcdefghijklmnopqrstuxyzvw"
enter = ''.join(sorted(enter))
enter = ''.join(set(enter))      

for c in enter:
    if c in " ,+'!-*()?[]{}=/%:;.0123456789 ":
        c = '' 
    
if len(enter) == len(char):
    print "not pangram"
else:
    print "pangram"
