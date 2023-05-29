from __future__ import annotations
import itertools
import random
import math


def sample_function() -> float:
    """This is a sample function that returns pi."""
    return math.pi


def add(a: int, b: int) -> int:
    """This is a sample function that adds two numbers."""
    return a + b


class Matrix(object):

    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self.data = [[0. for _ in range(columns)] for _ in range(rows)]

    def randomize(self) -> None:
        """Randomize the matrix."""
        for row in range(self.rows):
            for column in range(self.columns):
                self.data[row][column] = random.uniform(0, 1)

    def __add__(self, other: Matrix) -> Matrix:
        """Add two matrices together."""
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions.")

        result = Matrix(self.rows, self.columns)

        for row, column in itertools.product(range(self.rows), range(self.columns)):
            result.data[row][column] = self.data[row][column] + \
                other.data[row][column]
        return result

    def __sub__(self, other: Matrix) -> Matrix:
        """Subtract two matrices."""
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions.")

        result = Matrix(self.rows, self.columns)

        for row, column in itertools.product(range(self.rows), range(self.columns)):
            result.data[row][column] = self.data[row][column] - \
                other.data[row][column]
        return result

    def __mul__(self, other: Matrix) -> Matrix:
        """Multiply two matrices."""
        if self.columns != other.rows:
            raise ValueError(
                "The number of columns in the first matrix must be equal to the number of rows in the second matrix.")

        result = Matrix(self.rows, other.columns)

        for row, column in itertools.product(range(self.rows), range(other.columns)):
            result.data[row][column] = sum(
                self.data[row][i] * other.data[i][column]
                for i in range(self.columns)
            )
        return result

    def __str__(self) -> str:
        """Return a string representation of the matrix."""
        return f"Matrix({self.rows}, {self.columns})"

    def __repr__(self) -> str:
        """Return a string representation of the matrix."""
        return f"Matrix({self.rows}, {self.columns})"
