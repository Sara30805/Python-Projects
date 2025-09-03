# Add Time

This is a Python script that adds a duration to a specific time.
It was developed as part of the **Scientific Computing with Python** certification from [freeCodeCamp](https://www.freecodecamp.org/).

## Features
- Adds a duration (hours and minutes) to a given start time in 12-hour format (AM/PM).
- Optionally handles the day of the week.
- Returns the new time, correctly handling:
  - Transition from AM to PM.
  - Crossing over to the next day.
  - Multiple days later, indicating how many days have passed.
- Performs input validation:
  - Time format must be correct (e.g., '3:30 PM').
  - Duration format must be correct (e.g., '2:12').

## Usage
```python
from add_time import add_time

print(add_time("3:30 PM", "2:12"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
```

## Tests
To run the tests for this project, navigate to the project root directory and execute:
```bash
python3 -m unittest discover tests
```
