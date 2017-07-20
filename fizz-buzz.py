# coding: utf-8

def fizzbuzz(num):
	if num % 15 == 0:
		print "Fizz Buzz"
	elif num % 3 == 0:
		print "Fizz"
	elif num % 5 == 0:
		print "Buzz"
	else:
		print num

if __name__ == "__main__":
	n = input()
	for i in range(n):
		fizzbuzz(i+1)

