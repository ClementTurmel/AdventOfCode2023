import pytest
from markdown_writter import *
import re
#python -m pytest day1.py



@pytest.fixture(scope="module")
def doc_module(request):
    doc = MarkdownWritter()
    yield doc
    doc.dump_in_file("documentation/day1.md")

@pytest.fixture(scope="function")
def doc(doc_module, request):
    if request.function.__name__ != doc_module.last_documented_test_name:
        doc_module.log(f"#### {request.function.__name__}")
        doc_module.last_documented_test_name = request.function.__name__

    yield doc_module

def test_day_1_part_1_explanation(doc):
    doc.log("""
        The newly-improved calibration document consists of lines of text; 
        
        each line originally contained a specific calibration value that the Elves now need to recover. 
        
        On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

        For example:
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet

        In this example, the calibration values of these four lines are 12, 38, 15, and 77. 
        
        Adding these together produces 142.
        
        Consider your entire calibration document. What is the sum of all of the calibration values
 """)

@pytest.mark.parametrize("lines, expected_value", [
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
def test_calibrate_should_return_the_addition_of_numbers_created_from_first_and_last_digit_of_each_line(doc, lines, expected_value):
    result = calibrate(lines)
    doc.log(f"given lines ```{lines}```, calibrate return ```{result}```")
    assert result == expected_value


def test_calibrate_with_file_input(doc):
    text_input = ""
    with open("day_1_input.txt", "r") as file_input:
        text_input = file_input.read()
    
    result = calibrate(text_input)
    doc.log(f"given input day 1 file ```[day_1_input.txt](../day_1_input.txt)```, calibrate return ```{result}```")
    assert result == 55834


def calibrate(lines):
    sum = 0
    for line in lines.splitlines():
        numbers = re.findall(r'[0-9]', line)
        sum += int(f"{numbers[0]}{numbers[len(numbers)-1]}")

    return sum
