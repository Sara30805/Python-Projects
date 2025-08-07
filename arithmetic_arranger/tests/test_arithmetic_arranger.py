import unittest
from arithmetic_arranger import arithmetic_arranger

class TestArithmeticArranger(unittest.TestCase):

    def test_formatting_no_solution_1(self):
        problems = ["3801 - 2", "123 + 49"]
        expected = ("  3801      123\n-    2    +  49\n------    -----")
        self.assertEqual(arithmetic_arranger(problems), expected)

    def test_formatting_no_solution_2(self):
        problems = ["1 + 2", "1 - 9380"]
        expected = ("  1         1\n+ 2    - 9380\n---    ------")
        self.assertEqual(arithmetic_arranger(problems), expected)

    def test_formatting_no_solution_3(self):
        problems = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
        expected = ("    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----")
        self.assertEqual(arithmetic_arranger(problems), expected)

    def test_formatting_no_solution_4(self):
        problems = ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
        expected = ("  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------")
        self.assertEqual(arithmetic_arranger(problems), expected)

    def test_error_too_many_problems(self):
        problems = ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]
        self.assertEqual(arithmetic_arranger(problems), "Error: Too many problems.")

    def test_error_incorrect_operator(self):
        problems = ["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]
        self.assertEqual(arithmetic_arranger(problems), "Error: Operator must be '+' or '-'.")

    def test_error_number_more_than_four_digits(self):
        problems = ["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]
        self.assertEqual(arithmetic_arranger(problems), "Error: Numbers cannot be more than four digits.")
    
    def test_error_not_a_digit(self):
        problems = ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]
        self.assertEqual(arithmetic_arranger(problems), "Error: Numbers must only contain digits.")

    def test_formatting_solution_1(self):
        problems = ["3 + 855", "988 + 40"]
        expected = ("    3      988\n+ 855    +  40\n-----    -----\n  858     1028")
        self.assertEqual(arithmetic_arranger(problems, True), expected)

    def test_formatting_solution_2(self):
        problems = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"]
        expected = ("   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028")
        self.assertEqual(arithmetic_arranger(problems, True), expected)


if __name__ == "__main__":
    unittest.main()
