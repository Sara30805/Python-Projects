import unittest
from polygon_area_calculator import Rectangle, Square

class TestRectangleAndSquare(unittest.TestCase):

    def test_rectangle_str(self):
        rect = Rectangle(3, 4)
        self.assertEqual(str(rect), "Rectangle(width=3, height=4)")

    def test_square_str(self):
        sq = Square(5)
        self.assertEqual(str(sq), "Square(side=5)")

    def test_area_perimeter_diagonal(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.get_area(), 12)
        self.assertEqual(rect.get_perimeter(), 14)
        self.assertAlmostEqual(rect.get_diagonal(), 5.0)

    def test_setters_rectangle(self):
        rect = Rectangle(3, 4)
        rect.set_width(10)
        rect.set_height(2)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)

    def test_setters_square(self):
        sq = Square(5)
        sq.set_side(7)
        self.assertEqual(sq.width, 7)
        self.assertEqual(sq.height, 7)
        sq.set_width(3)
        self.assertEqual(sq.width, 3)
        self.assertEqual(sq.height, 3)
        sq.set_height(9)
        self.assertEqual(sq.width, 9)
        self.assertEqual(sq.height, 9)

    def test_get_picture_small(self):
        rect = Rectangle(3, 2)
        expected = "***\n***\n"
        self.assertEqual(rect.get_picture(), expected)

    def test_get_picture_too_big(self):
        rect = Rectangle(60, 2)
        self.assertEqual(rect.get_picture(), "Too big for picture.")

    def test_amount_inside(self):
        rect1 = Rectangle(10, 10)
        rect2 = Rectangle(3, 2)
        self.assertEqual(rect1.get_amount_inside(rect2), 15)

    def test_amount_inside_square(self):
        rect = Rectangle(16, 16)
        sq = Square(4)
        self.assertEqual(rect.get_amount_inside(sq), 16)

if __name__ == "__main__":
    unittest.main()
