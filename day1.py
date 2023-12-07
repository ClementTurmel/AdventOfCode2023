import pytest
from markdown_writter import *
import re
#python -m pytest day1.py

@pytest.fixture(scope="module")
def doc():
    doc = MarkdownWritter()
    yield doc
    doc.dump_in_file("documentation/day1.md")


@pytest.mark.parametrize("line, expected_value", [
    ("12",      12),
    ("36",      36),
    ("4abcd8",  48),
    ("a57b",    57),
    ("1b2c3",   13),
    ("""a6g7fce
     tisnro4kfe2
     frf8jrej9rt""", 67+42+89),
    ("aaaa7bbbb", 77),
    ("""1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet""", 142)
])
def test_calibrate_should_return_the_addition_of_numbers_created_from_first_and_last_digit_of_each_line(doc, line, expected_value):
    result = calibrate(line)
    doc.log(f"given lines ```{line}```, calibrate return ```{result}```")
    assert result == expected_value


def test_calibrate_with_file_input(doc):
    text_input = ""
    with open("day_1_input.txt", "r") as file_input:
        text_input = file_input.read()
    
    result = calibrate(text_input)
    assert result == 55834


def calibrate(lines):
    sum = 0
    for line in lines.splitlines():
        numbers = re.findall(r'[0-9]', line)
        sum += int(f"{numbers[0]}{numbers[len(numbers)-1]}")

    return sum
