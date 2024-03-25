
# Finite Field Element Class for F_{p^2}

class FElem:
    def __init__(self, a, b, p):
        self.a = a % p  # Coefficient for 1
        self.b = b % p  # Coefficient for x
        self.p = p     # The field characteristic (prime number)
        self.irreducible = [1, -1, -1]  # Coefficients for the irreducible polynomial x^2 - x - 1

    def __add__(self, other):
        if self.p != other.p:
            raise ValueError("Cannot add elements from different fields")
        return FElem(self.a + other.a, self.b + other.b, self.p)

    def __sub__(self, other):
        if self.p != other.p:
            raise ValueError("Cannot subtract elements from different fields")
        return FElem(self.a - other.a, self.b - other.b, self.p)

    def __mul__(self, other):
        if self.p != other.p:
            raise ValueError("Cannot multiply elements from different fields")
        a = (self.a * other.a + self.b * other.b) % self.p
        b = (self.a * other.b + self.b * other.a + self.b * other.b) % self.p
        return FElem(a, b, self.p)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.p == other.p

    def __str__(self):
        return f"{self.a};{self.b}"
