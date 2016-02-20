

import pytest
from shunt import Calculator

def test_one():
	c = Calculator()
	assert c.calculate('(50+50)*10') == 1000