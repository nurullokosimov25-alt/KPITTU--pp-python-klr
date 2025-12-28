
1.	##Logic.py
def running_sum(numbers):
    total = 0 

    for x in numbers:
        total += x
        yield total

2.	##tets_logic.py
import unittest
from logic import running_sum


class TestRunningSum(unittest.TestCase):

    def test_normal_case(self):
        data = [1, 2, 3]
        result = list(running_sum(data))
        self.assertEqual(result, [1, 3, 6])

    def test_empty_list(self):
        data = []
        result = list(running_sum(data))
        self.assertEqual(result, [])

    def test_negative_numbers(self):
        data = [5, -2, 4]
        result = list(running_sum(data))
        self.assertEqual(result, [5, 3, 7])


if __name__ == "__main__":
    unittest.main()

3.	## README.md
# Lab 7 — Part 2 (Команда 6)
