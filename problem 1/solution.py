# project euler problem 1

class Solver:

	@staticmethod
	def mod():
		sum = 0

		# below 1000 => we want < 1000, 
		for i in range(3, 1000):
			if(i % 5 == 0 or i % 3 == 0):
				sum += i

		print sum

	@staticmethod
	def alt():
		sum = 0

		for i in range(3, 1000):
			if(Solver.multthree(i) or Solver.multfive(i)):
				sum += i

		print sum

	@staticmethod
	def multfive(val):
		# We know something's a multiple of 5 if it ends in 0 or 5
		strval = str(val)

		if(int(strval[-1]) == 0 or int(strval[-1]) == 5):
			return True

		return False

	@staticmethod
	def multthree(val):
		# We know something's a multiple of 3 if the sum of the digits
		# is divisible by 3...
		# Why do this? 
		# Suppose you have 9999, you can check 9999 % 3 == 0, but isn't it 
		# better if we checked (9 + 9 + 9 + 9) = 36 % 3 == 0?
		strval = str(val)
		
		s = sum([int(x) for x in strval])

		if(s % 3 == 0):
			return True

		return False

def main():
	print "Solve using mod"
	Solver.mod()

	print "Solve using alt"
	Solver.alt()


if __name__ == "__main__":
	main()
