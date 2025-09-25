class Vector:
    def __init__(self, d):
        if isinstance(d, list):
            self.coords = d
        else:
            self.coords = [0] * d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __mul__(self, other):
        # scalar multiplication
        if isinstance(other, (int, float)):
            return Vector([c * other for c in self.coords])
        # dot product
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("dimensions must agree")
            return sum(self.coords[i] * other.coords[i] for i in range(len(self.coords)))
        else:
            raise TypeError("unsupported operand type for *")

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __neg__(self):
        return Vector([-c for c in self.coords])

    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)
