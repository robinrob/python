import unittest

from time_conversion import time_conversion

class TimeConversionTestCase(unittest.TestCase):
    def test_should_convert_00_00_00AM(self):
        self.assertEquals(time_conversion('12:00:00AM'), '00:00:00')

    def test_should_convert_01_00_00AM(self):
        self.assertEquals(time_conversion('01:00:00AM'), '01:00:00')

    def test_should_convert_11_59_59AM(self):
        self.assertEquals(time_conversion('11:59:59AM'), '11:59:59')

    def test_should_convert_11_59_59PM(self):
        self.assertEquals(time_conversion('11:59:59PM'), '23:59:59')

    def test_should_convert_12_00_00PM(self):
        self.assertEquals(time_conversion('12:00:00PM'), '12:00:00')

    def test_should_convert_06_00_00PM(self):
        self.assertEquals(time_conversion('06:00:00PM'), '18:00:00')

    def test_should_convert_09_00_00PM(self):
        self.assertEquals(time_conversion('09:00:00PM'), '21:00:00')

    def test_should_convert_12_40_22AM(self):
        self.assertEquals(time_conversion('12:40:22AM'), '00:40:22')
