import math

def Is_prime(n):
	for i in range(2,int(math.sqrt(n)) + 1):
		if n % i ==0:
			return False
	return True

num = input("number?:")
num = int(num)
for i in range(2,num):
	if Is_prime(i):
		print(i)
