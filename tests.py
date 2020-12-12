import unittest

import day_01
import day_02
import day_03
import day_04
import day_05
import day_06
import day_07
import day_08
import day_09
import day_10
import day_11
import day_12


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

    def test_day_03_part_2(self):
        self.assertEqual(6708199680, day_03.part_two())

    def test_day_04_part_1(self):
        self.assertEqual(237, day_04.part_one())

    def test_day_04_part_2(self):
        self.assertEqual(172, day_04.part_two())

    def test_day_05_part_1(self):
        self.assertEqual(951, day_05.part_one())

    def test_day_05_part_2(self):
        self.assertEqual(653, day_05.part_two())

    def test_day_06_part_1(self):
        self.assertEqual(6506, day_06.part_one())

    def test_day_06_part_2(self):
        self.assertEqual(3243, day_06.part_two())

    def test_day_07_part_1(self):
        self.assertEqual(179, day_07.part_one())

    def test_day_07_part_2(self):
        self.assertEqual(18925, day_07.part_two())

    def test_day_08_part_1(self):
        self.assertEqual(1548, day_08.part_one())

    def test_day_08_part_2(self):
        self.assertEqual(1375, day_08.part_two())

    def test_day_09_part_1(self):
        self.assertEqual(373803594, day_09.part_one())

    def test_day_09_part_2(self):
        self.assertEqual(51152360, day_09.part_two())

    def test_day_10_part_1(self):
        self.assertEqual(2176, day_10.part_one())

    def test_day_10_part_2(self):
        self.assertEqual(18512297918464, day_10.part_two())

    def test_day_11_part_1(self):
        self.assertEqual(2273, day_11.part_one())

    def test_day_11_part_2(self):
        self.assertEqual(2064, day_11.part_two())

    def test_day_12_part_1(self):
        self.assertEqual(1710, day_12.part_one())

    def test_day_12_part_2(self):
        self.assertEqual(62045, day_12.part_two())


if __name__ == "__main__":
    unittest.main()
