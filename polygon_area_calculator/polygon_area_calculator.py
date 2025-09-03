class Rectangle:
    """
    Represents a rectangle.

    Attributes
    ----------
    width : int
        Width of the rectangle.
    height : int
        Height of the rectangle.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initialize a new Rectangle.

        Parameters
        ----------
        width : int
            The width of the rectangle.
        height : int
            The height of the rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self) -> str:
        """
        Return a formatted string representation of the Rectangle.

        The string includes:
        - A word to indicate that it is a rectangle.
        - The width of the rectangle.
        - The height of the rectangle.

        Returns
        -------
        str
            A formatted string with the information of the rectangle.
        """
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width: int) -> None:
        """
        Change the width of the rectangle.

        Parameters
        ----------
        width : int
            The new width of the rectangle.
        """
        self.width = width
    
    def set_height(self, height: int) -> None:
        """
        Change the height of the rectangle.

        Parameters
        ----------
        height : int
            The new height of the rectangle.
        """
        self.height = height
    
    def get_area(self) -> int:
        """
        Return the area of the shape.

        Returns
        -------
        int
            The area of the shape (rectangle or square).
        """
        return self.width * self.height
    
    def get_perimeter(self) -> int:
        """
        Return the perimeter of the shape.

        Returns
        -------
        int
            The perimeter of the shape (rectangle or square).
        """
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self) -> float:
        """
        Return the diagonal of the shape.

        Returns
        -------
        float
            The diagonal of the shape (rectangle or square).
        """
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self) -> str:
        """
        Return a string that represents the shape using lines of '*'. The number of lines is equal to the height and the number of '*' in each line is equal to the width. 

        Returns
        -------
        str
            A string with the representation of the shape.

            If the width or height is larger than 50, the string 'Too big for picture.' is returned.
        """
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return '\n'.join('*' * self.width for _ in range(self.height)) + '\n'
    
    def get_amount_inside(self, shape: "Rectangle") -> int:
        """
        Takes another shape as an argument and returns the number of times the passed in shape could fit inside the shape (with no rotations).

        Parameters
        ----------
        shape: Rectangle
            The shape we are going to evaluate, which can be a rectangle or a square.

        Returns
        -------
        int
            The number of times the passed in shape could fit inside the shape.
        """
        return (self.width // shape.width) * (self.height // shape.height)

class Square (Rectangle):
    """
    Represents a square and is a subclass of Rectangle.

    Attributes
    ----------
    length : int
        Length of each side of the square.
    """
    def __init__(self, length: int) -> None:
        """
        Initialize a new Square.

        Parameters
        ----------
        length : int
            Width and height of the square.
        """
        super().__init__(length, length)

    def __str__(self) -> str:
        """
        Return a formatted string representation of the Square.

        The string includes:
        - A word to indicate that it is a square.
        - The length of the square.

        Returns
        -------
        str
            A formatted string with the information of the square.
        """
        return f'Square(side={self.width})'

    def set_side(self, length: int) -> None:
        """
        Change the length of the square.

        Parameters
        ----------
        length : int
            The new length of the square.
        """
        self.width = length
        self.height = length

    def set_width(self, width: int) -> None:
        """
        Change both the width and the height.

        Parameters
        ----------
        width : int
            The new length of the square.
        """
        self.set_side(width)
    
    def set_height(self, height: int) -> None:
        """
        Change both the width and the height.

        Parameters
        ----------
        height : int
            The new length of the square.
        """
        self.set_side(height)