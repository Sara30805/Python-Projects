def arithmetic_arranger(problems: list[str], show_answers: bool = False) -> str:

    """
    This function formats up to five arithmetic problems (addition and subtraction) and optionally shows their solutions. 
    
    It is part of the Scientific Computing with Python course from freeCodeCamp. Apart from the project requirements, it also has an error control which is specified in the docstring.

    Parameters:
    ----------
    problems : list of strings
        A list of arithmetic problems as strings (e.g., "32 + 698").
        Each problem must contain two operands and one operator (+ or -).
    show_answers : bool, optional
        If True, the function includes the solutions beneath each problem.
        Defaults to False.

    Returns:
    -------
    str
        A single string that contains the arranged arithmetic problems formatted
        vertically and separated by four spaces. If show_answers is True,
        the solutions are also included.

        If an error occurs, the function instead returns a string with an appropiate error message:
            - "Error: Too many problems." (more than five problems are provided)
            - "Error: Numbers must only contain digits." (operands contain non-digit characters)
            - "Error: Numbers cannot be more than four digits." (operands are more than four digits in length)
            - "Error: Operator must be '+' or '.'." (operator is not '+' or '-')
    """
    
    # error control
    if len(problems) > 5:
        return 'Error: Too many problems.'

    #separating the components of each arithmetic problem
    problems_separated = []

    for problem in problems:
        num1, operator, num2 = problem.split()

        # checking the operators are correct
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
    
        # calculating the number of spaces each operation uses
        width = max(len(num1), len(num2)) + 2

        # solving the problems in case the second argument is True
        result = 0
        if show_answers:
            result = int(num1) + int(num2) if operator == '+' else int(num1) - int(num2)

        # append structured problem data to the list
        problems_separated.append({
            'num1': num1,
            'operator': operator,
            'num2': num2,
            'width': width,
            'result': result
        })
    
    # creating the final string
    lines = [[], [], []]

    # adding the first operand
    for problem in problems_separated:
        lines[0].append(' ' * (problem['width'] - len(problem['num1'])) + problem['num1'])
    
    # adding the operation and the second operand
    for problem in problems_separated:
        lines[1].append(problem['operator'] + ' '*(problem['width'] - len(problem['num2']) - 1) + problem['num2'])

    # line of dashes under each operation
    for problem in problems_separated:
        lines[2].append('-'*problem['width'])

    # adding the solutions to the problem
    if show_answers:
        lines.append([])
        for problem in problems_separated:
            lines[3].append(' ' * (problem['width'] - len(str(problem['result']))) + str(problem['result']))

    # joining each one of the lines
    final_string = []
    for line in lines:
        final_string.append('    '.join(line))
    return '\n'.join(final_string)