import unittest
from datetime import datetime


def convert_date_format(date_str: str) -> str:
    """
    Convert a date string from 'YYYY-MM-DD' to 'DD-MM-YYYY'.
    Raises ValueError for invalid formats or impossible dates.
    """
    if not isinstance(date_str, str):
        raise ValueError("date_str must be a string")
    # Strict ISO-like parsing
    parsed = datetime.strptime(date_str, "%Y-%m-%d")
    return parsed.strftime("%d-%m-%Y")


class TestConvertDateFormat(unittest.TestCase):
    def test_basic_conversion(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("1999-01-01"), "01-01-1999")
        self.assertEqual(convert_date_format("2000-12-31"), "31-12-2000")

    def test_leap_year_and_edge_days(self):
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")  # leap day valid
        self.assertEqual(convert_date_format("2024-02-29"), "29-02-2024")  # leap year

    def test_month_and_day_zero_padding(self):
        self.assertEqual(convert_date_format("2023-03-07"), "07-03-2023")
        self.assertEqual(convert_date_format("2023-11-09"), "09-11-2023")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-13-01")  # invalid month
        with self.assertRaises(ValueError):
            convert_date_format("2023-00-10")  # invalid month 0
        with self.assertRaises(ValueError):
            convert_date_format("2023-04-31")  # April has 30 days
        with self.assertRaises(ValueError):
            convert_date_format("2021-02-29")  # not a leap year
        with self.assertRaises(ValueError):
            convert_date_format("15-10-2023")  # wrong format
        with self.assertRaises(ValueError):
            convert_date_format("20231015")    # no dashes
        with self.assertRaises(ValueError):
            convert_date_format(None)          # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()


