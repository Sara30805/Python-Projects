# Budget App

This is a Python script that manages a simple budget by categories and visually represents spending.  
It was developed as part of the **Scientific Computing with Python** certification from [freeCodeCamp](https://www.freecodecamp.org/).

## Features
- Allows creation of budget categories.
- Supports deposits, withdrawals, and transfers between categories.
- Tracks transactions in a ledger for each category.
- Calculates total withdrawals per category.
- Generates a text-based bar chart showing the percentage of spending per category.
- Includes type hints for better code clarity and maintainability.

## Usage
```python
from budget import Category, create_spend_chart

# Create categories
food = Category('Food')
clothing = Category('Clothing')

# Add deposits and withdrawals
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
food.transfer(50, clothing)

# Display ledger
print(food)
print(clothing)

# Generate spending chart
print(create_spend_chart([food, clothing]))
```

## Tests
To run the tests for this project, navigate to the project root directory and execute:
```bash
python3 -m unittest discover tests
```