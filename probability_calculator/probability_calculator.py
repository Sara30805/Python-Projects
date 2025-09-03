import copy
import random

from typing import List, Dict

class Hat:
    """
    Represents a hat with balls of different colors inside

    Attributes
    ----------
    contents: List[str]
        A list with colors that symbolize the balls that are inside the hat.
    """
    def __init__(self, **kwargs: int) -> None:
        """
        Initialize a new Hat.

        Parameters
        ----------
        **kwargs: int
            A dictionary with the colors as keys and the number of balls of that color as values.
        """
        # Ensure the hat is initialized with at least one ball
        if len(kwargs) < 1:
            raise ValueError("Hat must contain at least one ball")

        self.contents = []

        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls: int) -> List[str]:
        """
        Randomly remove balls from the hat.

        Parameters
        ----------
        num_balls : int
            The number of balls to draw.

        Returns
        -------
        List[str]
            A list with the colors of the balls drawn.
        """
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
    
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn
        

def experiment(hat: Hat, expected_balls: Dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    """
    Perform a probability experiment of drawing specific balls from a hat.

    Parameters
    ----------
    hat : Hat
        The hat object containing balls.
    expected_balls : dict of str to int
        A dictionary indicating the minimum number of each ball color 
        that should be drawn for the experiment to be considered successful.
    num_balls_drawn : int
        The number of balls to draw out of the hat in each experiment.
    num_experiments : int
        The total number of experiments to perform.

    Returns
    -------
    float
        The estimated probability of drawing at least the expected balls.
    """
    successful_experiments = 0
    for _ in range(num_experiments):

        # Copy the hat to avoid modifying the original

        hat_copy = copy.deepcopy(hat)

        # Draw balls from the copied hat
        balls_drawn = hat_copy.draw(num_balls_drawn)

        # Check if the drawn balls satisfy expected counts

        success = True

        for color, count in expected_balls.items():
            if balls_drawn.count(color) < count:
                success = False
                break
        
        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments