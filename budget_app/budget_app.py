import math

class Category:
    """
    Represents a category of items in a budget.

    Attributes
    ----------
    category_name : str
        Name of the category.
    ledger : list of dict
        List of transactions (deposits and withdrawals) in the category.
    """
    def __init__(self, category_name: str) -> None:
        """
        Initialize a new Category.

        Parameters
        ----------
        category_name : str
            The name of the category.
        """
        self.category_name = category_name
        self.ledger = []

    def __str__(self) -> str:
        """
        Return a formatted string representation of the Category.

        The string includes:
        - A centered title surrounded by '*' with total length 30.
        - A list of ledger items with description and amount.
        - The total balance at the end.

        Returns
        -------
        str
            A formatted string with the ledger and balance.
        """

        # First line with the title
        lines = [self.category_name.center(30, '*')]

        # Next lines with the information in the ledger
        for item in self.ledger:
            lines.append(f"{item['description'][:23].ljust(23)}{item['amount']:>7.2f}")

        lines.append(f'Total: {self.get_balance():.2f}')
        return '\n'.join(lines)


    def deposit(self, amount: float, description: str='') -> None:
        """
        Deposit an amount into the ledger.

        Parameters
        ----------
        amount : float
            The amount to deposit.
        description : str, optional
            A description of the deposit (default is an empty string).
        """
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount: float, description: str='') -> bool:
        """
        Withdraw an amount from the ledger if sufficient funds are available.

        Parameters
        ----------
        amount : float
            The amount to withdraw.
        description : str, optional
            A description of the withdrawal (default is an empty string).

        Returns
        -------
        bool
            True if the withdrawal was successful, False otherwise.
        """
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True
    
    def get_balance(self) -> float:
        """
        Calculate the current balance of the category.

        Returns
        -------
        float
            The total balance (sum of all deposits and withdrawals).
        """
        return sum(item['amount'] for item in self.ledger)
    
    def transfer(self, amount: float, budget_category: 'Category') -> bool:
        """
        Transfer an amount from the current category to another.

        Parameters
        ----------
        amount : float
            The amount to transfer.
        budget_category : Category
            The destination category.

        Returns
        -------
        bool
            True if the transfer was successful, False otherwise.
        """
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {budget_category.category_name}')
        budget_category.deposit(amount, f'Transfer from {self.category_name}')
        return True

    def check_funds(self, amount: float) -> bool:
        """
        Check if there are sufficient funds for a transaction.

        Parameters
        ----------
        amount : float
            The amount to check.

        Returns
        -------
        bool
            True if there are enough funds, False otherwise.
        """
        return amount <= self.get_balance()

    def get_total_withdraw(self) -> float:
        """
        Calculate the total amount withdrawn from the category.

        Returns
        -------
        float
            The sum of all withdrawals (absolute value).
        """
        return sum(-item['amount'] for item in self.ledger if item['amount'] < 0)

def calculate_totals(categories: list[Category]) -> dict[str, float]:
    """
    Generate the total withdraws for each category.

    Parameters
    ----------
    categories: list
        A list with the categories that are going to be evaluated.

    Returns
    -------
    dict[str, float]
        A dictionary with the categories to be shown as the keys and their total withdraw as the values.

        """
    return {category.category_name: category.get_total_withdraw() for category in categories}


def calculate_percentages(categories: list[Category]) -> dict[str, int]:
    """
    Generate a dictionary mapping category names to their spending percentages (rounded down to nearest 10%).

    Parameters
    ----------
    categories: list
        A list with the categories that are going to be evaluated.

    Returns
    -------
    dict[str, float]
        A dictionary with the categories to be shown as the keys and their withdraw percentage regarding the other categories.

        """
    totals = calculate_totals(categories)
    total = sum(totals.values())
    return {k: math.floor(v / total * 100 / 10) * 10 for k, v in totals.items()}
    
def generate_chart_lines(categories_withdraw: dict[str, int], categories: list[Category]) -> list[str]:
    """
    Generate the main lines of the spending chart.

    Parameters
    ----------
    categories_withdraw: dict
        A dictionary where the key is a category name and the value is the spending percentage (rounded down to nearest 10).
    categories: list
        A list of Category instances to include in the chart.

    Returns
    -------
    list[str]
        Each element is a line of the chart showing the 'o' markers.
    """
    lines = []
    for i in range(10, -1, -1):
        line = f'{str(i*10).rjust(3)}| '
        line += ''.join(['o  ' if categories_withdraw[category.category_name] >= i * 10 else '   ' for category in categories])
        lines.append(line)
    lines.append(f"    -{'---' * len(categories)}")
    return lines

def generate_labels(categories: list[Category]) -> list[str]:
    """
    Generate the labels to print in the chart.

    Parameters
    ----------
    categories : list
        The categories to show in the chart.

    Returns
    -------
    list[str]        
        Each element is a line of the chart.
    """
    lines = []
    for i in range(max([len(category.category_name) for category in categories])):
            lines.append('     ' + '  '.join([category.category_name[i] if i < len(category.category_name) else ' ' for category in categories]) + '  ')
    return lines

def create_spend_chart(categories: list[Category]) -> str:
    """
    Create a bar chart showing the percentage spent by category.

    Parameters
    ----------
    categories : list of Category
        List of budget categories to include in the chart.

    Returns
    -------
    str
        A formatted string representing the spending chart.
    """

    categories_withdraw = calculate_percentages(categories)

    lines = ['Percentage spent by category']

    lines += generate_chart_lines(categories_withdraw, categories) + generate_labels(categories)

    return '\n'.join(lines)