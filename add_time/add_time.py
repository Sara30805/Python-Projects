def add_time(start: str, duration: str, day_of_week: str = '') -> str:
    """
    This function calculates the new time after adding a duration to a start time.
    
    It is part of the Scientific Computing with Python course from freeCodeCamp. Apart from the project requirements, it also has an error control which is specified in the docstring.

    Parameters:
    ----------
    start : a start time string in the format "HH:MM AM/PM".
    duration : a duration string in the format "HH:MM".
        It is the duration that we are going to add to the start time.
    day_of_week : a string representing the day of the week (optional).
        If provided, it will include the day of the week in the output.
        It is case-insensitive and can be any day of the week

    Returns:
    -------
    str
        A string that contains the new time after adding the duration to the start time.
    
    Raises:
    ------
    ValueError
        Raised for invalid inputs, including but not limited to:
        - `start` is not a string.
        - `duration` is not a string.
        - `day_of_week` is not a string or is invalid.
        - `start` hour is not between 1 and 12.
        - `start` minute is not between 0 and 59.
        - `start` does not end with AM or PM.
        - `duration` is invalid (negative or minutes >= 60).
        - `start` not in the format "HH:MM AM/PM".
        - `start` hour and minute are not integers.
        - `duration` not in the format "HH:MM".
        - `duration` hours and minutes are not integers.
    """

    # a list with the days of the week that will be used to determinate the final day
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # error control
    if not isinstance(start, str):
        raise ValueError('start must be a string')
    if not isinstance(duration, str):
        raise ValueError('duration must be a string')
    if not isinstance(day_of_week, str):
        raise ValueError('day_of_week must be a string')
    if day_of_week != '' and day_of_week.lower() not in [day.lower() for day in days_of_week]:
        raise ValueError('the day of the week is wrong')

    # parse start time
    try:
         start_hour, rest = start.split(':')
         start_minute, start_am_pm = rest.split(" ")
    except ValueError:
        raise ValueError("start must be in the format 'HH:MM AM/PM'")
    try:
        start_hour = int(start_hour)
        start_minute = int(start_minute)
    except ValueError:
        raise ValueError("start hour and minute must be integers")

    # error control
    if not (1 <= start_hour <= 12):
        raise ValueError('start hour must be between 1 and 12')
    if not (0 <= start_minute <= 59):
        raise ValueError('start minute must be between 0 and 59')
    if start_am_pm not in ['AM', 'PM']:
        raise ValueError('start must end with AM or PM')

    # parse duration
    try:
        duration_hour, duration_minute = duration.split(':')
    except ValueError:
        raise ValueError("duration must be in the format 'HH:MM'")

    try:
        duration_hour = int(duration_hour)
        duration_minute = int(duration_minute)
    except ValueError:
        raise ValueError("duration hours and minutes must be integers")

    # error control
    if duration_hour < 0 or duration_minute < 0 or duration_minute >= 60:
        raise ValueError('duration is invalid')
    
    # calculate total hours and minutes
    final_hour = start_hour + int(duration_hour) + (start_minute + duration_minute) // 60
    final_minute = (start_minute + duration_minute) % 60

    # determine how many 12-hour periods have passed
    periods_passed = final_hour // 12
    final_hour %= 12
    if final_hour == 0:
        final_hour = 12

    # determine final am/pm
    final_am_pm = start_am_pm
    if periods_passed % 2 == 1:
        if start_am_pm == 'AM':
            final_am_pm = 'PM'
        elif start_am_pm == 'PM':
            final_am_pm = 'AM'
    
    # prepare day of the week
    final_day_of_week = ''

    day_index = 0
    if day_of_week != '':
        for day in days_of_week:
            if day.lower() == day_of_week.lower():
                break
            day_index += 1
        

    # calculate days later and format day info
    days_later = periods_passed // 2 if start_am_pm == 'AM' else (periods_passed + 1) // 2
    day_information = ''
    if day_of_week != '':
        final_day_of_week = f', {days_of_week[(day_index + days_later) % 7]}'
    if days_later == 1:
        day_information = ' (next day)'
    elif days_later > 1:
        day_information = f' ({days_later} days later)'
    
    # construct final time string
    new_time = f'{str(final_hour)}:{final_minute:02d} {final_am_pm}{final_day_of_week}{day_information}'

    return new_time