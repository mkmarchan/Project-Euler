termA = 1
termB = 2
sum = 0
while (termB < 4000000):
    if(termB % 2 == 0):
    	sum += termB
    temp = termB
    termB = termA + termB
    termA = temp
print sum
