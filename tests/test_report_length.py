from lib.report_length import *

def test_report_length_empty_string():
    assert report_length('') == "This string was 0 characters long."

def test_report_length_short_string():
    assert report_length('hi') == "This string was 2 characters long."

def test_report_length_long_string():
    assert report_length('aaaaaaaaaaaaaaaaaaaa') == "This string was 20 characters long."

def test_report_length_string_of_num():
    assert report_length('123456789') == "This string was 9 characters long."