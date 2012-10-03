# project euler problem 2


class Solver:

	MAX = 4000000

	@staticmethod
	def recursive():
		sum = 0

		i = 0
		
		while True:
			seq = Solver.fib(i)
			i += 1

			if(seq > Solver.MAX):
				break

			if(seq % 2  ==0):
				sum += seq

		print sum

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
		s = 0
		# for i in range(2, Solver.MAX):



def main():
	print "Solve using recursion... prepare to wait"
	Solver.recursive()


if __name__ == "__main__":
	main()