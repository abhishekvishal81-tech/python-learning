#override the __len__() method on vector of problem 5 to display the dimension of the vector
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

    def __len__(self):
        return 3   # dimension of this vector is fixed (3D)


# Example
v = Vector(7, 8, 10)
print(v)        # 7i+8j+10k
print(len(v))   # 3
