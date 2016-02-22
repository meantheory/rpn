
import sys, os
from rpnalt import Calculator
from rpnalt import CalculatorException
import rpncontroller


'''
One can run this by calling it on the command line

	python calc2.py
'''

def cli():
	i = input(' > ')
	return i 

def cliloop():

	c = Calculator()

	while True: 
		i = cli()

		#quit the calculator
		if i is 'q' or i is '':
			break
			
		#clear the calculator
		if i is 'c':
			c.clear()
			continue

		#handle calculator input
		try: 
			print(c.next(i))

		except CalculatorException:
				print('Ignoring "%s", need two values to operate on.' % i)

		except ValueError:
			print(rpncontroller.VALUE_ERROR)

def main():
	try: 
		cliloop()
	except (KeyboardInterrupt, SystemExit):
		print('\n GOODBYE')

if __name__ == '__main__':
	main()