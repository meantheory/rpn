
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

class CalculatorException(Exception):
	pass

class Calculator:

	def __init__(self):
		self.clear()

	def next(self, arg):
		if RPN.isoperator(arg):
			a = self.peek()
			b = self.peek(2)
			if a and b:
				y, x = self._stack.pop(), self._stack.pop()
				self._stack.append( RPN.math(arg, x, y) )
			else:
				raise CalculatorException('Can not find two operators to do an operation against')
		else:
			self._stack.append(RPN.parsenum(arg))

		return self.peek()

	def clear(self):
		self._stack = []

	def args(self, args):
		for arg in args:
			self.next(arg)

	def answer(self):
		return self._stack.pop()

	def peek(self, n=1):
		try:
			return self._stack[-n]
		except IndexError:
			return False

