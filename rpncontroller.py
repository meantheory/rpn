
from rpn import rpn
from rpnalt import Calculator

VALUE_ERROR = "Unrecognized value and unable to parse to int/float"
INDEX_ERROR = "Can not find two operators to do an operation against"

def dorpn(args):
	try: 
		result = rpn(*args)

	except IndexError:
		result = INDEX_ERROR

	except ValueError:
		result = VALUE_ERROR

	return result

def dorpnalt(args):

	c = Calculator()
	result = c.args(args)
	return result

