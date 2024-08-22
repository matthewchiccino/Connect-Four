#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """A class representing a Connect Four board with arbitrary dimensions."""
    
    def __init__(self, height, width):
        """Initializes a new Connect Four board with the given height and width."""
        self.height = height
        self.width = width
        # Create a 2D list to represent the board slots, initialized with spaces.
        self.slots = [[' '] * self.width for _ in range(self.height)]
        
    def __repr__(self):
        """Returns a string representation of the Board object."""
        s = ''  # Begin with an empty string

        # Add one row of slots at a time to the string representation
        for row in range(self.height):
            s += '|'   # Start each row with a vertical bar

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # Add a newline at the end of each row

        # Add a row of hyphens at the bottom of the board
        s += '-' * (self.width * 2 + 1) + '\n'

        # Add a row of column numbers beneath the hyphens
        s += ' '.join(str(col % 10) for col in range(self.width)) + ' '

        return s

    def add_checker(self, checker, col):
        """
        Adds the specified checker ('X' or 'O') to the specified column.
        Inputs:
            checker: A string representing the checker ('X' or 'O').
            col: An integer representing the column index.
        """
        assert checker in ('X', 'O'), "Checker must be either 'X' or 'O'."
        assert 0 <= col < self.width, "Column index is out of bounds."
        
        # Start from the bottom row and move upwards to find the first empty slot
        for row in reversed(range(self.height)):
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                break
    
    def reset(self):
        """Resets the board by setting all slots to empty spaces."""
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
    
    def add_checkers(self, colnums):
        """
        Adds alternating checkers to the board based on the provided column numbers.
        Input:
            colnums: A string of column numbers where checkers should be placed.
        """
        checker = 'X'  # Start with 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # Alternate between 'X' and 'O'
            checker = 'O' if checker == 'X' else 'X'

    def can_add_to(self, col):
        """
        Checks if a checker can be added to the specified column.
        Input:
            col: An integer representing the column index.
        Returns:
            True if a checker can be added, False otherwise.
        """
        if not (0 <= col < self.width):  # Check if column index is out of bounds
            return False 
        return self.slots[0][col] == ' '  # Check if the topmost row in the column is empty

    def is_full(self):
        """
        Checks if the board is completely full.
        Returns:
            True if the board is full, False otherwise.
        """
        return all(self.slots[0][col] != ' ' for col in range(self.width))

    def remove_checker(self, col):
        """
        Removes the topmost checker from the specified column.
        Input:
            col: An integer representing the column index.
        """
        for row in range(self.height):
            if self.slots[row][col] in ('X', 'O'):
                self.slots[row][col] = ' '
                break
    
    def is_horizontal_win(self, checker):
        """
        Checks for a horizontal win for the specified checker.
        Input:
            checker: A string representing the checker ('X' or 'O').
        Returns:
            True if there is a horizontal win, False otherwise.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if all(self.slots[row][col + i] == checker for i in range(4)):
                    return True
        return False
    
    def is_vertical_win(self, checker):
        """
        Checks for a vertical win for the specified checker.
        Input:
            checker: A string representing the checker ('X' or 'O').
        Returns:
            True if there is a vertical win, False otherwise.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if all(self.slots[row + i][col] == checker for i in range(4)):
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """
        Checks for a downward diagonal win (top-left to bottom-right) for the specified checker.
        Input:
            checker: A string representing the checker ('X' or 'O').
        Returns:
            True if there is a downward diagonal win, False otherwise.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if all(self.slots[row + i][col + i] == checker for i in range(4)):
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """
        Checks for an upward diagonal win (bottom-left to top-right) for the specified checker.
        Input:
            checker: A string representing the checker ('X' or 'O').
        Returns:
            True if there is an upward diagonal win, False otherwise.
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if all(self.slots[row - i][col + i] == checker for i in range(4)):
                    return True
        return False
        
    def is_win_for(self, checker):
        """
        Checks if the specified checker has won the game.
        Input:
            checker: A string representing the checker ('X' or 'O').
        Returns:
            True if the checker has won (horizontal, vertical, or diagonal), False otherwise.
        """
        assert checker in ('X', 'O'), "Checker must be either 'X' or 'O'."
        return (
            self.is_horizontal_win(checker) or 
            self.is_vertical_win(checker) or 
            self.is_down_diagonal_win(checker) or 
            self.is_up_diagonal_win(checker)
        )
