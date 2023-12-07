import pytest
from markdown_writter import MarkdownWritter, doc_module, doc
import re
#python -m pytest day1.py


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




def test_day_1_part_2_explaination(doc):
    doc.log(
"""
Your calculation isn't quite right. 
It looks like some of the digits are actually spelled out with letters: 
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
Adding these together produces 281.
"""
    )


def test_extract_digit_and_digit_letters_return_list_of_digit_and_letters_word_digit(doc):
    line            = "one2ZZZseven8AAA"
    expected_result = ["one","2","seven","8"]
    
    actual_result = extract_digit_and_digit_letters(line)
    doc.log(f"given ```{line}``` when calling ```extract_digit_and_digit_letters``` it return ```{actual_result}```")
    
    assert actual_result == expected_result

def test_extract_digit_and_digit_letters_should_handle_overlapping_word(doc):
    line            = "twone"
    expected_result = ["two","one"]
    
    actual_result = extract_digit_and_digit_letters(line)
    doc.log(f"given ```{line}``` when calling ```extract_digit_and_digit_letters``` it return ```{actual_result}```")
    
    assert actual_result == expected_result

def test_transform_to_digits_should_convert_string_digit_to_digit(doc):
    numbers = ["one","seven"]
    expected_numbers = [1,7]
    
    actual_result = transform_to_digit(numbers)
    doc.log(f"given ```{numbers}``` when calling ```transform_to_digit``` it return ```{actual_result}```")

    assert actual_result == expected_numbers

def test_transform_to_digits_should_convert_string_digit_to_digit_and_keep_others_digits(doc):
    numbers = ["one","4","seven"]
    expected_numbers = [1,4,7]
    
    actual_result = transform_to_digit(numbers)
    doc.log(f"given ```{numbers}``` when calling ```transform_to_digit``` it return ```{actual_result}```")

    assert actual_result == expected_numbers


@pytest.mark.parametrize("lines, expected_value", [
    ("onetwo",           12),
    ("threefour",        34),
    ("fivesix",          56),
    ("seveneight",       78),
    ("nine",             99),
    ("oneight",          18),
    ("fbnbj5two3twoneg", 51),
    ("""two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen""",281),
])
def test_calibrate_must_also_take_care_of_digits_spelled_in_letters(doc, lines, expected_value):
    result = calibrate(lines)
    doc.log(f"given lines ```{lines}```, calibrate return ```{result}```")
    assert result == expected_value

def test_calibrate_with_file_input(doc):
    text_input = ""
    with open("day_1_input.txt", "r") as file_input:
        text_input = file_input.read()
    
    result = calibrate(text_input)
    doc.log(f"given input day 1 file [day_1_input.txt](../day_1_input.txt), calibrate return ```{result}```")
    assert result == 53221

######## implementation ##############

def extract_digit_and_digit_letters(text:str):
    return re.findall(r'(?=(zero|one|two|three|four|five|six|seven|eight|nine|[0-9]))', text)

def transform_to_digit(numbers:list):
    dict_numbers = {
        "zero":0,"one":1,"two":2,"three":3,"four":4,
        "five":5,"six":6,"seven":7,"eight":8,"nine":9
    }
    
    digit_numbers = [dict_numbers[number] if number in dict_numbers else int(number)  for number in numbers]

    return digit_numbers


def calibrate(lines):
    sum = 0
    for line in lines.splitlines():
        numbers = extract_digit_and_digit_letters(line)
        digit_numbers = transform_to_digit(numbers)
        sum += int(f"{digit_numbers[0]}{digit_numbers[len(digit_numbers)-1]}")

    return sum
