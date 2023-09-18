from lib.greet import *

def test_greet_james():
    result = greet('James')
    assert result == "Hello, James!"

def test_greet_simon():
    result = greet('Simon')
    assert result == "Hello, Simon!"