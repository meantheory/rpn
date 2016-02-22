
import sys
from rpn import rpn

'''
One can run this by calling it on the command line

	python calc.py 5 3 -
	this will output 2
'''

def cli(args):
	try: 
		result = rpn(*args)

	except IndexError:
		result = "Can not find two operators to do an operation against"

	except ValueError:
		result = "Unrecognized value and unable to parse to int/float"

	return result

if __name__ == '__main__':
	result = cli(sys.argv[1:]) #get rid of command name
	print(result)