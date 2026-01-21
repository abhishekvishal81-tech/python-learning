#write a class vector representing a vector of n dimensions.overload the + and * operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, *values):
        #  Vector(1,2,3) OR Vector([1,2,3])
        if len(values) == 1 and isinstance(values[0], (list, tuple)):
            self.data = list(values[0])
        else:
            self.data = list(values)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"Vector({self.data})"

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for addition")
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __mul__(self, other):
        # dot product
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for dot product")
        return sum(a * b for a, b in zip(self.data, other.data))


# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Sum:", v1 + v2)       # Vector([5, 7, 9])
print("Dot:", v1 * v2)       # 32
