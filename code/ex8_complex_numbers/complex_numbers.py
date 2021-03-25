from constants import COMPLEX_ERROR

class ComplexNumbers:

    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag
    
    def __eq__(self, other):
        if isinstance(other, ComplexNumbers):
            return self.real == other.real and self.imag == other.imag
        else:
            raise TypeError(COMPLEX_ERROR)
    
    def __str__(self):
        return str(self.real + self.imag)
      
    def __add__(self, other):
        if isinstance(other, ComplexNumbers):
            return ComplexNumbers(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError(COMPLEX_ERROR)
    
    def __mul__(self, other):
        if isinstance(other, ComplexNumbers):
            return ComplexNumbers((self.real * other.real) - (self.imag * other.imag), (self.imag * other.real) + (self.real * other.imag))
        else:
            raise TypeError(COMPLEX_ERROR)
