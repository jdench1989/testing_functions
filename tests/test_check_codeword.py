from lib.check_codeword import *

def test_check_codeword_correct():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_check_codeword_incorrect():
    result = check_codeword('llama')
    assert result == "WRONG!"

def test_check_codeword_nearly_correct():
    result = check_codeword('hare')
    assert result == "Close, but nope."