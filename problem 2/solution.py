# project euler problem 2


class Solver:

	MAX = 4000000

	@staticmethod
	def recursive():
		# Store sum 
		s = 0

		i = 0
		
		# Sum all even fibs recursively
		while True:
			seq = Solver.fib(i)
			i += 1

			# Exit condition
			if(seq > Solver.MAX):
				break

			if(seq % 2  ==0):
				s += seq

		print s

	@staticmethod
	def fib(n):
		if(n == 0):
			return 0
		if(n == 1):
			return 1
		if(n == 2):
			return 2

		return Solver.fib(n - 1) + Solver.fib(n - 2)

	@staticmethod
	def linear():

		# Start with saved
		s = 2

		# save last two fibs
		storedfib = [1, 2]
		
		while True:
			# Get new fib
			newfib = storedfib[0] + storedfib[1]
			
			# Exit condition
			if(newfib > Solver.MAX):
				break

			# Save last two fibs again
			storedfib[0] = storedfib[1]
			storedfib[1] = newfib

			if(newfib %2 == 0):
				s += newfib

		print s



def main():
	print "Solve using recursion... prepare to wait"
	Solver.recursive()

	print "Solve with loop"
	Solver.linear()


if __name__ == "__main__":
	main()