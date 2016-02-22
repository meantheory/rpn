
import sys
import rpncontroller

'''
One can run this by calling it on the command line

	python calc.py 5 3 -
	this will output 2
'''

def cli(args):
	return rpncontroller.dorpn(args)

if __name__ == '__main__':
	result = cli(sys.argv[1:]) #get rid of command name
	print(result)