
operators = ['+', '-', '*', '/']

def rpn(*args):

	stack = [] #init stack

	# function for returning numbers from input
	def parsenum(n):

		if isinstance(n, str):
			# this will throw a ValueError if you pass it 
			# a string that can not be parse by these funcs.
			return float(n) if '.' in n else int(n)

		elif isinstance(n, (int, float)):
			return n
		else:
			raise ValueError('Unable to parse input')

	# performs the math
	def math(arg, x, y):

		if arg is '+':
			result = x + y
		elif arg is '-':
			result = x - y
		elif arg is '*': 
			result = x * y
		elif arg is '/':
			result = x / y # handle division by zero

		return result

	# go over input args
	for arg in args:

		if arg in operators:
			# pop 2 from the stack 
			y = stack.pop()
			x = stack.pop()
			result = math(arg, x, y)

			# push back to stack 
			stack.append(result)
			continue #continue to next arg

		stack.append(parsenum(arg))

	# return answer
	answer = stack.pop()
	return answer

def main():
	x = rpn(0, 2, '/')
	print(x)
	
if __name__ == '__main__':
	main()