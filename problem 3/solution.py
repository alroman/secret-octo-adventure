# Project Euler problem 3

import math


class Solver:

	TARGET = 600851475143

	''' Reuse some of our methods from problem 1 '''
	@staticmethod
	def multfive(val):
		# We know something's a multiple of 5 if it ends in 0 or 5
		strval = str(val)

		if(int(strval[-1]) == 0 or int(strval[-1]) == 5):
			return True

		return False

	@staticmethod
	def multthree(val):
		strval = str(val)

		s = sum([int(x) for x in strval])

		if(s % 3 == 0):
			return True

		return False

	''' 
		Check if a number is prime... Can probably make more 
		efficient with some more tests
	'''
	@staticmethod
	def is_prime(val):
		# Let's rule out divisible by 5
		if(Solver.multfive(val)):
			return False

		# Let's rule out divisible by 3
		if(Solver.multthree(val)):
			return False

		# Let's attempt trial division
		sqrt = int(math.sqrt(val))

		# Check if it's possible to divide number by values
		# from 7 < i < sqrt(val)
		i = 7

		while True:
			# We can divide the number, so it's not prime
			if(val % i == 0):
				return False

			# Only consider odd numbers
			i += 2

			# We have one..
			if(i > sqrt):
				break

		return True

	@staticmethod
	def solve():
		# Pick a range...
		rng = int(math.sqrt(VAL))
		
		# Save the factors
		factors = []

		# Save divided target
		divided = Solver.TARGET

		# Work with odd numbers only
		for i in range(7, rng, 2):

			# If a number is prime and it divides the 'target' value,
			# then it's a prime factor
			if(Solver.is_prime(i) and divided % i == 0):

				# Save the prime factor
				factors.append(i)

				# Remove it from the 'target'
				divided /= i

				# Do exit test..
				if(divided == 1):
					break

		print factors



def main():
	print "Thinking..."
	print "Here are prime factors"
	Solver.solve()


if __name__ == "__main__":
	main()
