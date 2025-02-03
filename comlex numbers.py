class Complexnumber:
    def __init__(self, real, img) -> None:
        self.real = real
        self.img =  img
        
    def __str__(self) -> str:
        return f"{self.real} + {self.img}i"
    
    def __add__(self, other):
        newComplex = self.real + other.real 
        newComplex2 = self.img + other.img 
        return Complexnumber(newComplex, newComplex2)
    
c1 = Complexnumber(2, 3)
c2 = Complexnumber(4, 7)
total = c1 + c2
print(f"{c1}\n{c2}")
print(total)