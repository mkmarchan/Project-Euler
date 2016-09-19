import math

eligibleSquares = []

for i in range(1, int(math.sqrt(1000))):
    eligibleSquares.append(i**2)

print eligibleSquares[:]

csq = 0
bsq = 0
asq = 0
num = 1000
found = False
for i in range(len(eligibleSquares) - 1, -1, -1):
    num1 = num
    csq = eligibleSquares[i]
    num2 = num1 - csq
    print "step 1: " + str(num2)
    for j in range(i - 1, -1, -1):
        bsq = eligibleSquares[j]
	num3 = num2 -bsq
	print "step 2: " + str(num3)
	if (num3 > 0):
	    for k in range(j - 1, -1, -1):
	        asq = eligibleSquares[k]
		num4 = num3 - asq
		print "step 3: " + str(num4)
		if (num4 == 0):
		    found = True
		    break
	    if found:
	        break
        if found:
	    break
print "asq: " + str(asq) + " bsq: " + str(bsq) + " csq: " + str(csq)
print math.sqrt(asq)*math.sqrt(bsq)*math.sqrt(csq)

