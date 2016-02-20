
from rpn import rpn 

LEFT_PAREN = '('
RIGHT_PAREN = ')'
PRECEDENCE = (None, 'assignment', 'paren', 'add_subtract', 'multiply_divide', 'unary_ops', 'exponent')
OPERATORS = ('+', '-', '*', '/')
FUNCTIONS = ('pow')
FUNCTION_ARG_SEP = (',')

class Kind:
	operator = 'operator'
	numeric = 'numeric'
	alpha = 'alpha'
	paren = 'paren'
	sep = 'sep'
	exhaust = 'exhausted'

class Token:

	def __init__(self, kind, value):
		self.kind = kind
		self.value = value

	def __repr__(self):
		return self.value

	def update(self, v):
		self.value += v

	def isfunc(self):
		return self.value in FUNCTIONS

	def issep(self):
		return self.value in FUNCTION_ARG_SEP

	def islparen(self):
		return self.value == LEFT_PAREN

	def isrparen(self):
		return self.value == RIGHT_PAREN

class ShuntingYard:
	"""
	implementation of shunting yard algorithm described here: 
		https://en.wikipedia.org/wiki/Shunting-yard_algorithm
	"""

	

	def __init__(self):
		self.operator_stack = []
		self.output_queue = []
		# self.functions = ('pow')
		# self.function_arg_sep = (',')
		# self.operators = ('+', '-', '*', '/')

	def peek(self):
		if len(self.operator_stack) > 0:
			return self.operator_stack[-1]

		return Token(Kind.exhaust, None)

	def _out(self, token):
		self.output_queue.append(token)

	def feed(self, tokens):

		for token in tokens:

			#If the token is a number, then add it to the output queue.
			if token.kind == Kind.numeric:
				self._out(token)


			#If the token is a function token, then push it onto the stack.
			elif token.isfunc():
				self.operator_stack.append(token)

			#If the token is a function argument separator (e.g., a comma)
			elif token.issep():

				#Until the token at the top of the stack is a left parenthesis, 
				#pop operators off the stack onto the output queue. 
				while self.peek().islparen():
					self._out(self.operator_stack.pop())

					#If no left parentheses are encountered, either the separator 
					#was misplaced or parentheses were mismatched.
					if len(self.operator_stack) == 0:
						pass

			#If the token is an operator, o1, then:
			elif token.kind == Kind.operator:

				#while there is an operator token o2, at the top of the operator stack and either
				while self.peek().kind == Kind.operator:
					# o2 = self.peek()

					#o1 is left-associative and its precedence is less than or equal to that of o2, or
					#o1 is right associative, and has precedence less than that of o2,
						#pop o2 off the operator stack, onto the output queue;
					self._out(self.operator_stack.pop())

				# at the end of iteration push o1 onto the operator stack.
				self.operator_stack.append(token)

			# If the token is a left parenthesis (i.e. "("), then push it onto the stack.
			elif token.islparen():
				self.operator_stack.append(token)

			# If the token is a right parenthesis (i.e. ")"):
			elif token.isrparen(): 
				# 	Until the token at the top of the stack is a left parenthesis, pop operators off the stack onto the output queue.
				while not self.peek().islparen():
					self._out(self.operator_stack.pop())

					if len(self.operator_stack) == 0:
						raise Exception('mismatched parentheses')

				# 	Pop the left parenthesis from the stack, but not onto the output queue.
				lp = self.operator_stack.pop()

				# 	If the token at the top of the stack is a function token, pop it onto the output queue.
				# if self.peek().isfunc():
				# 	self._out(self.operator_stack.pop())

				# 	If the stack runs out without finding a left parenthesis, then there are mismatched parentheses.
				# 	I did this above



		# When there are no more tokens to read:
		# 	While there are still operator tokens in the stack:
		while len(self.operator_stack) > 0:
			op = self.peek()

			#If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses.
			if op.islparen() or op.isrparen():
				raise Exception('mismatched parentheses')

			#Pop the operator onto the output queue.
			self._out(self.operator_stack.pop())


		# test 
		#print(self.output_queue)

class Calculator:

	def __init__(self):
		pass

	def calculate(self, calcinput):

		tokens = []

		for char in calcinput:
			tk = self.tokenizer(char)

			if len(tokens) > 0:
				ltk = tokens[-1]
				if ltk.kind == tk.kind and tk.kind in (Kind.alpha, Kind.numeric):
					ltk.update(tk.value)
					continue
			
			tokens.append(tk)

		s = ShuntingYard()
		s.feed(tokens)
		args = []
		for x in s.output_queue:
			args.append(x.value)


		return rpn(*args)

	def tokenizer(self, char):
		
		if char in OPERATORS:
			return Token(Kind.operator, char)

		elif char in (LEFT_PAREN, RIGHT_PAREN):
			return Token(Kind.paren, char)

		elif char in FUNCTION_ARG_SEP:
			return Token(Kind.sep, char)

		elif char.isnumeric():
			return Token(Kind.numeric, char)

		elif char.isalpha():
			return Token(Kind.alpha, char)

		raise ValueError('Unrecognized input')

if __name__ == '__main__':
	
	c = Calculator()
	answer = c.calculate('(50+50)*10')
	print(answer)







