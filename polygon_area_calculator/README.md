# Polygon Area Calculator

This is a Python project that calculates properties of rectangles and squares using object-oriented programming.  
It was developed as part of the **Scientific Computing with Python** certification from [freeCodeCamp](https://www.freecodecamp.org/).

## Features
- Implements a `Rectangle` class with methods to:
  - Set width and height.
  - Calculate area, perimeter, and diagonal.
  - Generate a visual representation of the shape using `*`.
  - Determine how many times another shape fits inside it.
- Implements a `Square` class that inherits from `Rectangle`:
  - Initialize with a single side.
  - Override width and height setters to keep sides equal.
  - Additional method `set_side` to change the length of all sides simultaneously.
- Proper string representation for both shapes:
  - `Rectangle(width=5, height=10)`
  - `Square(side=9)`

## Usage
```python
from polygon_calculator import Rectangle, Square

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

## Tests
To run the tests for this project, navigate to the project root directory and execute:
```bash
python3 -m unittest discover tests
```
