def isPalindrome(num):
    "finds if a 6 digit number is a palindrome"
    for i in range(3):
    	if (num / (10**(5-i)) % 10 != num / (10**i) % 10):
	    return False
    return True

termA = 1000
foundPalindrome = 0
while(termA > 99):
    termA -= 1
    termB = 1000
    while (termB > 99):
    	termB -= 1
	product = termA * termB
	if(isPalindrome(product) and product > foundPalindrome):
	    foundPalindrome = product
print "result: " + str(foundPalindrome)

