from unittest import TestCase

from day_01a import generate_answer as generate_a, return_bookend_numbers
from day_01b import generate_answer as generate_b


class Day01aTest(TestCase):
    def test_provided_test(self):
        input_given = """1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
        """
        answer = generate_a(input_given)
        self.assertEqual(answer, 142)

    def test_return_bookend_numbers(self):
        self.assertEqual(return_bookend_numbers("1abc2"), 12)
        self.assertEqual(return_bookend_numbers("pqr3stu8vwx"), 38)
        self.assertEqual(return_bookend_numbers("a1b2c3d4e5f"), 15)
        self.assertEqual(return_bookend_numbers("treb7uchet"), 77)


class Day01bTest(TestCase):
    def test_provided_test(self):
        input_given = """two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen
        """
        answer = generate_b(input_given)
        self.assertEqual(answer, 281)
