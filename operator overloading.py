class Vault:
    def __init__(self, gallons, sickles, knuts):
        self.gallons = gallons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"gallons {self.gallons}, sickles {self.sickles}, knuts {self.knuts}"
    
    def __add__(self, other):
        gallons = self.gallons + other.gallons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(gallons, sickles, knuts)
        
        
harry = Vault(20, 30, 100)
print(harry)

rob = Vault(100,50,10)
print(rob)

total = harry + rob
print(total)