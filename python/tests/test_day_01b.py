from unittest import TestCase

from python.src.day_01b import find_top_three_calories_carried


class Day01bTest(TestCase):
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
        answer = find_top_three_calories_carried(input)
        self.assertEqual(45000, answer)

    def test_no_elf(self):
        input = """"""
        answer = find_top_three_calories_carried(input)
        self.assertEqual(0, answer)

    def test_one_elf(self):
        input = """1000
            2000
            3000
        """
        answer = find_top_three_calories_carried(input)
        self.assertEqual(6000, answer)

    def test_two_elf(self):
        input = """1000
            2000
            3000
            
            9000
        """
        answer = find_top_three_calories_carried(input)
        self.assertEqual(15000, answer)
