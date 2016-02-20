

import pytest
from shunt import Calculator

def test_one():
	c = Calculator()
	assert c.calculate('(50+50)*10') == 1000

def test_two():
	c = Calculator()
	assert c.calculate('((50+50)*10)/2/2') == 250

def test_wikipedia_example():
	c = Calculator()
	assert c.calculate('5 + ((1 + 2) * 4) - 3') == 14