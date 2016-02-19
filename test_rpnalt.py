
import pytest
from rpnalt import Calculator

@pytest.fixture(scope="module")
def c():
	return Calculator()


# basic, is it alive tests

def test_addition(c):
	
	c.next('2')
	c.next(2)
	c.next('+')

	assert c.answer() == 4

def test_subtration(c):

	c.args([7, 3, '-'])
	assert c.answer() == 4

	c.args([10, 3, '-'])
	assert c.answer() == 7


def test_multiply(c):

	c.args([2, 2, '*'])
	assert c.answer() == 4

def test_division(c):

	c.args([8, 2, '/'])
	assert c.answer() == 4

# now lets get more diabolical

def test_bad_str(c):
 	with pytest.raises(ValueError):
 		c.args(['this', 'bad'])

# def test_zero():
# 	with pytest.raises(ZeroDivisionError):
# 		rpn('2', '0', '/')

def test_wikipedia_example(c):

	c.args([5, 1, 2, '+', 4, '*', '+', 3, '-'])
	assert c.answer() == 14

def test_weird_chars(c):
	with pytest.raises(ValueError):
		# below looks normal but the minus symbol is 
		# some different unicode symbol so it won't
		# recognize it as an operator and blow up 
		c.args([5, 3, '−']) == 2

def test_weird_input_args(c):
	with pytest.raises(TypeError):
		c.args(5, 3, '-') == 2

def test_bad_input_string(c):
	with pytest.raises(ValueError):
		c.args('5 3 -') == 2

# # example input from excercise 

def test_example_1(c):

	c.args([5, 8, '+'])
	assert c.answer() == 13

def test_example_2(c):

	c.args([-3, -2, '*', 5, '+'])
	assert c.answer() == 11

def test_example_3(c):

	c.args([2, 9, 3, '+', '*'])
	assert c.answer() == 24

def test_example_4(c):

	c.args([20, 13, '-', 2, '/']) 
	assert c.answer() == 3.5
