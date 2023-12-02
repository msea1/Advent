from unittest import TestCase

from python.src.day_01a import find_most_calories_carried


class Day01aTest(TestCase):
    def test_provided_test(self):
        input = """1000
            2000
            3000
            
            4000
            
            5000
            6000
            
            7000
            8000
            9000
            
            10000
        """
        answer = find_most_calories_carried(input)
        self.assertEqual(24000, answer)

    def test_no_elf(self):
        input = """"""
        answer = find_most_calories_carried(input)
        self.assertEqual(0, answer)

    def test_one_elf(self):
        input = """1000
            2000
            3000
        """
        answer = find_most_calories_carried(input)
        self.assertEqual(6000, answer)

    def test_two_elf(self):
        input = """1000
            2000
            3000
            
            9000
        """
        answer = find_most_calories_carried(input)
        self.assertEqual(9000, answer)
