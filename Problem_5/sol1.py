def check(num):
    for i in range(1, 21):
    	if num % i != 0:
	    return False
    return True

num = 0
solFound = False
while(not solFound):
    num += 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    solFound = check(num)
print str(num)
