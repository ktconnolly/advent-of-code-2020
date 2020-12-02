import unittest

import day_01
import day_02


class Tests(unittest.TestCase):
    def test_day_01_part_1(self):
        self.assertEqual(494475, day_01.part_one())

    def test_day_01_part_2(self):
        self.assertEqual(267520550, day_01.part_two())

    def test_day_02_part_1(self):
        self.assertEqual(465, day_02.part_one())

    def test_day_02_part_2(self):
        self.assertEqual(294, day_02.part_two())


if __name__ == "__main__":
    unittest.main()
