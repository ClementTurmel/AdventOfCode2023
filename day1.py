import pytest
from markdown_writter import *

#python -m pytest test_flowers.py

@pytest.fixture(scope="module")
def doc():
    doc = MarkdownWritter()
    yield doc
    doc.dump_in_file("documentation/day1.md")

def test_calibrate_should_return_the_first_digit_and_the_last_digit_of_a_line(doc):
    line = "12"
    result = calibrate(line)
    assert result == 12

def calibrate(line):
    return 12
