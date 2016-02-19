
# a more objecty version

class RPN:

	@staticmethod
	def parsenum(n):
		if isinstance(n, str):
			return float(n) if '.' in n else int(n)
		elif isinstance(n, (int, float)):
			return n 
		else:
			raise ValueError('Unable to parse input.')

	@staticmethod
	def isoperator(op):
		return op in ('+', '-', '*', '/')

	@staticmethod
	def math(arg, x, y):
		if arg is '+':
			return x + y
		elif arg is '-':
			return x - y
		elif arg is '*': 
			return x * y
		elif arg is '/':
			return x / y


class Calculator:

	def __init__(self):
		self._stack = []

	def next(self, arg):
		if RPN.isoperator(arg):
			y, x = self._stack.pop(), self._stack.pop()
			self._stack.append( RPN.math(arg, x, y) )
		else:
			self._stack.append(RPN.parsenum(arg))

		return self.peek()

	def args(self, args):
		for arg in args:
			self.next(arg)

	def answer(self):
		return self._stack.pop()

	def peek(self):
		return self._stack[-1]

