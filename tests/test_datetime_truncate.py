from datetime import datetime
import unittest

from datetime_truncate import truncate

DEFAULT_DT = datetime(2012, 7, 12, 12, 14, 14, 342)


class TestDatetimeTruncate(unittest.TestCase):
    def setUp(self):
        self.default_dt = datetime(2012, 7, 12, 12, 14, 14, 342)

    def test_truncate_to_second(self):
        self.assertEqual(truncate(self.default_dt, 'second'),
                         self.default_dt.replace(microsecond=0))

    def test_truncate_to_minute(self):
        self.assertEqual(truncate(self.default_dt, 'minute'),
                         self.default_dt.replace(second=0, microsecond=0))

    def test_truncate_to_hour(self):
        self.assertEqual(truncate(self.default_dt, 'hour'),
                         self.default_dt.replace(minute=0, second=0,
                                                 microsecond=0))

    def test_truncate_to_day(self):
        self.assertEqual(truncate(self.default_dt, 'day'),
                         self.default_dt.replace(hour=0, minute=0,
                                                 second=0, microsecond=0))

    def test_truncate_to_month(self):
        self.assertEqual(truncate(self.default_dt, 'month'),
                         self.default_dt.replace(day=1, hour=0, minute=0,
                                                 second=0, microsecond=0))

    def test_truncate_to_year(self):
        self.assertEqual(truncate(self.default_dt, 'year'),
                         self.default_dt.replace(month=1, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))

    def test_truncate_to_week(self):
        self.assertEqual(truncate(self.default_dt, 'week'),
                         self.default_dt.replace(day=9, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate(self.default_dt.replace(day=9), 'week'),
                         self.default_dt.replace(day=9, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate(self.default_dt.replace(day=16), 'week'),
                         self.default_dt.replace(day=16, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))

    def test_truncate_to_quarter(self):
        self.assertEqual(truncate(self.default_dt.replace(month=2), 'quarter'),
                         self.default_dt.replace(month=1, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate(self.default_dt.replace(month=6), 'quarter'),
                         self.default_dt.replace(month=4, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(truncate(self.default_dt, 'quarter'),
                         self.default_dt.replace(month=7, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
        self.assertEqual(
            truncate(self.default_dt.replace(month=10), 'quarter'),
            self.default_dt.replace(month=10, day=1, hour=0,
                                    minute=0, second=0,
                                    microsecond=0)
        )

    def test_truncat_to_half_year(self):
        self.assertEqual(
            truncate(self.default_dt.replace(month=6), 'half_year'),
            self.default_dt.replace(month=1, day=1, hour=0,
                                    minute=0, second=0,
                                    microsecond=0)
        )
        self.assertEqual(truncate(self.default_dt, 'half_year'),
                         self.default_dt.replace(month=7, day=1, hour=0,
                                                 minute=0, second=0,
                                                 microsecond=0))
