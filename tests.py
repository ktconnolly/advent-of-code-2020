import unittest

import day_01
import day_02
import day_03
import day_04
import day_05


class Tests(unittest.TestCase):
    def test_day_01_part_1(self):
        self.assertEqual(494475, day_01.part_one())

    def test_day_01_part_2(self):
        self.assertEqual(267520550, day_01.part_two())

    def test_day_02_part_1(self):
        self.assertEqual(465, day_02.part_one())

    def test_day_02_part_2(self):
        self.assertEqual(294, day_02.part_two())

    def test_day_03_part_1(self):
        self.assertEqual(216, day_03.part_one())

    def test_day_04_part_1(self):
        self.assertEqual(237, day_04.part_one())

    def test_day_04_part_2(self):
        self.assertEqual(172, day_04.part_two())

    def test_day_05_part_1(self):
        self.assertEqual(951, day_05.part_one())

    def test_day_05_part_2(self):
        self.assertEqual(653, day_05.part_two())


if __name__ == "__main__":
    unittest.main()
