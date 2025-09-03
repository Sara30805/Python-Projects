# Probability Calculator

This is a Python script that simulates drawing balls of different colors from a hat to estimate probabilities through repeated experiments. 
It was developed as part of the **Scientific Computing with Python** certification from [freeCodeCamp](https://www.freecodecamp.org/).

## Features
- Create a Hat object with any number of balls of different colors.
- Randomly draw a given number of balls from the hat.
- Run multiple probability experiments using repeated ramdom sampling.
- Calculate the likelihood of drawing at least a certain combination of balls.

## Usage
```python
from hat import Hat, experiment

# Create a hat with balls
hat = Hat(red=3, blue=2, green=6)

# Draw balls directly
drawn = hat.draw(4)
print("Balls drawn:", drawn)

# Run an experiment
probability = experiment(
    hat=Hat(black=6, red=4, green=3),   # fresh hat for each experiment
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print("Estimated Probability:", probability)
```

## Tests
To run the tests for this project, navigate to the project root directory and execute:
```bash
python3 -m unittest discover tests
```