#write__str__methodtoprintthevector as follows: 7i+8j+10k
#assume vector of the dimension 3 for this problem.
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def __mul__(self, other):
        # dot product
        return self.i * other.i + self.j * other.j + self.k * other.k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"


# Example
v1 = Vector(7, 8, 10)
v2 = Vector(1, 2, 3)

print(v1)         # 7i+8j+10k
print(v1 + v2)    # 8i+10j+13k
print(v1 * v2)    # 53
