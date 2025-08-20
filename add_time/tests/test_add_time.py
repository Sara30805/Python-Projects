import unittest
from add_time import add_time

class TestAddTime(unittest.TestCase):

    def test_add_time_no_day_of_week_1(self):
        start, duration = '3:30 PM', '2:12'
        expected = '5:42 PM'
        self.assertEqual(add_time(start, duration), expected)

    def test_add_time_no_day_of_week_2(self):
        start, duration = '11:55 AM', '3:12'
        expected = '3:07 PM'
        self.assertEqual(add_time(start, duration), expected)
    
    def test_add_time_next_day_no_day_of_week_1(self):
        start, duration = '2:59 AM', '24:00'
        expected = '2:59 AM (next day)'
        self.assertEqual(add_time(start, duration), expected)
    
    def test_add_time_days_later_no_day_of_week_1(self):
        start, duration = '11:59 PM', '24:05'
        expected = '12:04 AM (2 days later)'
        self.assertEqual(add_time(start, duration), expected)

    def test_add_time_days_later_no_day_of_week_2(self):
        start, duration = '8:16 PM', '466:02'
        expected = '6:18 AM (20 days later)'
        self.assertEqual(add_time(start, duration), expected)
    
    def test_add_time_day_of_week_1(self):
        start, duration, day_of_week = '3:30 PM', '2:12', 'Monday'
        expected = '5:42 PM, Monday'
        self.assertEqual(add_time(start, duration, day_of_week), expected)

    def test_add_time_next_day_day_of_week_1(self):
        start, duration, day_of_week = '2:59 AM', '24:00', 'saturDay'
        expected = '2:59 AM, Sunday (next day)'
        self.assertEqual(add_time(start, duration, day_of_week), expected)

    def test_add_time_days_later_day_of_week_1(self):
        start, duration, day_of_week = '11:59 PM', '24:05', 'Wednesday'
        expected = '12:04 AM, Friday (2 days later)'
        self.assertEqual(add_time(start, duration, day_of_week), expected)

    def test_add_time_days_later_day_of_week_2(self):
        start, duration, day_of_week = '8:16 PM', '466:02', 'tuesday'
        expected = '6:18 AM, Monday (20 days later)'
        self.assertEqual(add_time(start, duration, day_of_week), expected)


if __name__ == "__main__":
    unittest.main()
