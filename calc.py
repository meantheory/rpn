
import sys
from rpn import rpn

'''
One can run this by calling it on the command line

	python calc.py 5 3 -

	this will output 2

'''

if __name__ == '__main__':
	args = sys.argv[1:] #get rid of command name
	result = rpn(*args)

	print(result)