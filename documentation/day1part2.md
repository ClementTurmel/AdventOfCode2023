#### test_day_1_part_1_explanation


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
 

#### test_calibrate_should_return_the_addition_of_numbers_created_from_first_and_last_digit_of_each_line

given lines ```12```, calibrate return ```12```

given lines ```36```, calibrate return ```36```

given lines ```4abcd8```, calibrate return ```48```

given lines ```a57b```, calibrate return ```57```

given lines ```1b2c3```, calibrate return ```13```

given lines ```a6g7fce
    tisnro4kfe2
    frf8jrej9rt```, calibrate return ```198```

given lines ```aaaa7bbbb```, calibrate return ```77```

given lines ```1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet```, calibrate return ```142```

#### test_day_1_part_2_explaination


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


#### test_extract_digit_and_digit_letters_return_list_of_digit_and_letters_word_digit

given ```one2ZZZseven8AAA``` when calling ```extract_digit_and_digit_letters``` it return ```['one', '2', 'seven', '8']```

#### test_extract_digit_and_digit_letters_should_handle_overlapping_word

given ```twone``` when calling ```extract_digit_and_digit_letters``` it return ```['two', 'one']```

#### test_transform_to_digits_should_convert_string_digit_to_digit

given ```['one', 'seven']``` when calling ```transform_to_digit``` it return ```[1, 7]```

#### test_transform_to_digits_should_convert_string_digit_to_digit_and_keep_others_digits

given ```['one', '4', 'seven']``` when calling ```transform_to_digit``` it return ```[1, 4, 7]```

#### test_calibrate_must_also_take_care_of_digits_spelled_in_letters

given lines ```onetwo```, calibrate return ```12```

given lines ```threefour```, calibrate return ```34```

given lines ```fivesix```, calibrate return ```56```

given lines ```seveneight```, calibrate return ```78```

given lines ```nine```, calibrate return ```99```

given lines ```oneight```, calibrate return ```18```

given lines ```fbnbj5two3twoneg```, calibrate return ```51```

given lines ```two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen```, calibrate return ```281```

#### test_calibrate_with_file_input

given input day 1 file [day_1_input.txt](../day_1_input.txt), calibrate return ```53221```

