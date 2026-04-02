# Simple functions like the deletion, access, and insertion are supported by the array implementation.
# The matrix is represented as a list of lists, and its operations such as the insertion of rows and elements, the deletion of rows and elements, as well access to the particular elements are done.
# This enables the simple and two-dimensional arrays to be handled.

class Array:
    def __init__(self):
        self.arr = []

    # Insertion at a specific index
    def insert(self, index, value):
        self.arr.insert(index, value)

    # Deletion from a specific index
    def delete(self, index):
        if 0 <= index < len(self.arr):
            self.arr.pop(index)

    # Accessing an element by index
    def access(self, index):
        if 0 <= index < len(self.arr):
            return self.arr[index]
        return None


class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Insertion of a value into a specific row and column
    def insert(self, row, col, value):
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
            self.matrix[row][col] = value

    # Deletion of a value at a specific row and column
    def delete(self, row, col):
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
            self.matrix[row][col] = 0

    # Accessing an element at a specific row and column
    def access(self, row, col):
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
            return self.matrix[row][col]
        return None

# Example usage for Array:
arr = Array()
# Inserting 5 at index 0
arr.insert(0, 5)
# Inserting 10 at index 1
arr.insert(1, 10)
# Accessing value at index 0
print(arr.access(0))
# Deleting value at index 0
arr.delete(0)
# Accessing value at index 0 after deletion
print(arr.access(0))

# Example usage for Matrix:
# Creating a 3x3 matrix
matrix = Matrix(3, 3)
# Inserting 5 at position (0, 1)
matrix.insert(0, 1, 5)
# Accessing the element at position (0, 1)
print(matrix.access(0, 1))
# Deleting the value at position (0, 1)
matrix.delete(0, 1)
# Accessing the element at position (0, 1) after deletion
print(matrix.access(0, 1))