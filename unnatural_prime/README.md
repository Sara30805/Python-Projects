# Is Unnatural Prime

This is a Python script that given an integer, determine if that number is a prime number or a negative prime number.
It was developed as a **Daily Coding Challenge** from [freeCodeCamp](https://www.freecodecamp.org/).

## Features
- Checks if a number is prime (positive) or negative prime.
- Validates input type, raising a 'TypeError' if the input is not an integer.
- Efficiently tests divisibility using the square root method.
- Handles special cases: 0 and 1 are not considered primes.

## Usage
```python
from is_unnatural_prime import is_unnatural_prime

print(is_unnatural_prime(7))    # True
print(is_unnatural_prime(-11))  # True
print(is_unnatural_prime(1))    # False
print(is_unnatural_prime(9))    # False
```

## Tests
To run the tests for this project, navigate to the project root directory and execute:

```bash
python3 -m unittest discover tests
```