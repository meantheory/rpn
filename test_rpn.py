
import pytest
from rpn import rpn

# basic, is it alive tests

def test_addition():
	assert rpn('2', 2, '+') == 4

def test_subtraction():
	assert rpn('7', '3', '-') == 4

def test_multiply():
	assert rpn('2', 2, '*') == 4

def test_division():
	assert rpn('8', '2', '/') == 4

# now lets get more diabolical

def test_bad_str():
 	with pytest.raises(ValueError):
 		rpn('this', 'bad', '+')

def test_zero():
	with pytest.raises(ZeroDivisionError):
		rpn('2', '0', '/')

def test_wikipedia_example():
	assert rpn(5, 1, 2, '+', 4, '*', '+', 3, '-') == 14

def test_weird_chars():
	with pytest.raises(ValueError):
		# below looks normal but the minus symbol is 
		# some different unicode symbol so it won't
		# recognize it as an operator and blow up 
		assert rpn(5, 3, '−') == 2

def test_weird_input_array():
	with pytest.raises(ValueError):
		assert rpn([5, 3, '-']) == 2

def test_bad_input_string():
	with pytest.raises(ValueError):
		assert rpn('5 3 -') == 2

# example input from excercise 

def test_example_1():
	assert rpn(5, 8, '+') == 13

def test_example_2():
	assert rpn(-3, -2, '*', 5, '+') == 11

def test_example_3():
	assert rpn(2, 9, 3, '+', '*') == 24

def test_example_4():
	assert rpn(20, 13, '-', 2, '/') == 3.5