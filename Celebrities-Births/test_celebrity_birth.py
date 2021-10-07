
from datetime import Date
import unittest

class DateTestCase(unittest.TestCase):
    def test_it__(self):
        date = DateTestCase('day', 'month', 'year')
        expected_value = '01/01/2021'
        actual_value = DateTestCase.test_it__()
        self.assertEqual(expected_value, actual_value)


    def test_is_date_valid(self, day: int, month: int, year: int) -> bool:
        date = DateTestCase('day', 'month', 'year')
        expected_value = '01/01/2021'
        actual_value = DateTestCase.test_is_date_valid()
        self.assertEqual(expected_value, actual_value)

      

    
    def test_from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return cls(day, month, year)


class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.date = Date('')
    def test_transform_name(self):
        expected_value = ''
        actual_value = self.date
        self.assertEqual(expected_value, actual_value)

