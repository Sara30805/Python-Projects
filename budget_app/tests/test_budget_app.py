import unittest
from budget_app import Category, create_spend_chart

class TestBudgetApp(unittest.TestCase):

    def setUp(self):
        self.food = Category("Food")
        self.clothing = Category("Clothing")
        self.auto = Category("Auto")

    def test_deposit(self):
        self.food.deposit(1000, "initial deposit")
        self.assertEqual(self.food.get_balance(), 1000)

    def test_withdraw(self):
        self.food.deposit(1000)
        result = self.food.withdraw(100.25, "groceries")
        self.assertTrue(result)
        self.assertEqual(self.food.get_balance(), 899.75)

    def test_withdraw_insufficient_funds(self):
        self.food.deposit(50)
        result = self.food.withdraw(100, "expensive meal")
        self.assertFalse(result)
        self.assertEqual(self.food.get_balance(), 50)

    def test_transfer_successful(self):
        self.food.deposit(500)
        result = self.food.transfer(200, self.clothing)
        self.assertTrue(result)
        self.assertEqual(self.food.get_balance(), 300)
        self.assertEqual(self.clothing.get_balance(), 200)

    def test_transfer_insufficient_funds(self):
        self.food.deposit(50)
        result = self.food.transfer(100, self.clothing)
        self.assertFalse(result)
        self.assertEqual(self.food.get_balance(), 50)
        self.assertEqual(self.clothing.get_balance(), 0)

    def test_get_total_withdraw(self):
        self.food.deposit(1000)
        self.food.withdraw(100, "groceries")
        self.food.withdraw(50, "restaurant")
        self.assertEqual(self.food.get_total_withdraw(), 150)

    def test_create_spend_chart(self):
        self.food.deposit(1000)
        self.food.withdraw(100, "groceries")
        self.clothing.deposit(500)
        self.clothing.withdraw(150, "clothes")
        chart = create_spend_chart([self.food, self.clothing])
        chart_correct = 'Percentage spent by category\n100|       \n 90|       \n 80|       \n 70|       \n 60|    o  \n 50|    o  \n 40| o  o  \n 30| o  o  \n 20| o  o  \n 10| o  o  \n  0| o  o  \n    -------\n     F  C  \n     o  l  \n     o  o  \n     d  t  \n        h  \n        i  \n        n  \n        g  '
        self.assertEqual(chart, chart_correct)
        

if __name__ == "__main__":
    unittest.main()
