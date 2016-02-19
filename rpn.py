
operators = ['+', '-', '*', '/']

def rpn(*args):

	stack = [] #init stack

	# function for returning numbers from input
	def parsenum(n):

		if isinstance(n, str):
			# this will throw a ValueError if you pass it 
			# a string that can not be parse by these funcs.
			return float(n) if '.' in n else int(n)

		return n

	def math(arg):
		print(stack)
		# pop 2 from the stack 
		x = stack.pop()
		y = stack.pop()

		# perform op

		if arg is '+':
			result = x + y
		elif arg is '-':
			result = x - y
		elif arg is '*': 
			result = x * y
		elif arg is '/':
			result = x / y # handle division by zero

		return result

	for arg in args:

		if arg in operators:
			result = math(arg)
			# push back to stack 
			stack.append(result)
			break #continue to next arg

		try:
			stack.append(parsenum(arg))
		except ValueError:
			print('I only understand numbers, try again')
			return		

	answer = stack.pop()
	return answer

def main():

	x = rpn('2', 2, '+')
	print(x)
	

if __name__ == '__main__':
	main()