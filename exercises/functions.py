# Write your solution for 1.4 here!

def is_prime(x):
	for i in range(x - 1, 1, -1):
		if x % i == 0:
			print(i);
			return False
	return True;

print(is_prime(4))