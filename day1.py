import pytest
from markdown_writter import *

#python -m pytest day1.py

@pytest.fixture(scope="module")
def doc():
    doc = MarkdownWritter()
    yield doc
    doc.dump_in_file("documentation/day1.md")


@pytest.mark.parametrize("line, expected_value", [
    ("12", 12),
    ("36", 36),
    ("4abcd8", 48)
])
def test_calibrate_should_return_the_first_digit_and_the_last_digit_of_a_line(doc, line, expected_value):
    result = calibrate(line)
    assert result == expected_value

def calibrate(line):
    return int(f"{line[0]}{line[len(line)-1]}")
