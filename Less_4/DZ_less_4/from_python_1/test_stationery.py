import sys
import unittest

sys.path.append('../')
from from_python_1.stationery import Pen, Pencil, Handle


class TestStationery(unittest.TestCase):
    pen = Pen('ручка')
    pencil = Pencil('карандаш')
    handle = Handle('маркер')

    def test_pen_correct(self):
        """
        Testing correct pen.draw()
        :return:
        """
        self.assertEqual(self.pen.draw(), 'Запуск отрисовки ручкой')

    def test_pen_incorrect(self):
        """
        Testing incorrect pen.draw()
        :return:
        """
        self.assertNotEqual(self.pen.draw(), 'Wrong message')

    def test_pencil_correct(self):
        """
        Testing correct pencil.draw()
        :return:
        """
        self.assertEqual(self.pencil.draw(), 'Запуск отрисовки карандашом')

    def test_pencil_incorrect(self):
        """
        Testing incorrect pencil.draw()
        :return:
        """
        self.assertNotEqual(self.pencil.draw(), 'Wrong message')

    def test_handle_correct(self):
        """
        Testing correct handle.draw()
        :return:
        """
        self.assertEqual(self.handle.draw(), 'Запуск отрисовки маркером')

    def test_handle_incorrect(self):
        """
        Testing incorrect handle.draw()
        :return:
        """
        self.assertNotEqual(self.handle.draw(), 'Wrong message')


if __name__ == '__main__':
    unittest.main()