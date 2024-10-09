# Write a program to implement operator overloading for complex number arithmetic.

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
# addition
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
# subtraction
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
# multiplication
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
# true division
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)
# string method
    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

# Example usage:
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

# Addition
print(f"{c1} + {c2} = {c1 + c2}")

# Subtraction
print(f"{c1} - {c2} = {c1 - c2}")

# Multiplication
print(f"{c1} * {c2} = {c1 * c2}")

# Division
print(f"{c1} / {c2} = {c1 / c2}")
