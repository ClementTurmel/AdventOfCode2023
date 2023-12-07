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

#### test_calibrate_with_file_input

given input day 1 file [day_1_input.txt](../day_1_input.txt), calibrate return ```55834```

