# Arithmetic Arranger

This is a Python script that formats and arranges arithmetic problems vertically.  
It was developed as part of the **Scientific Computing with Python** certification from [freeCodeCamp](https://www.freecodecamp.org/).

## Features
- Accepts a list of arithmetic problems (addition and subtraction only).
- Formats each problem in vertical arrangement.
- Optionally displays the result of each operation.
- Performs input validation:
  - Maximum of five problems.
  - Operands must only contain digits.
  - Operands must be no more than four digits.
  - Only '+' and '-' operators are allowed.

## Example Usage
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"], True))
