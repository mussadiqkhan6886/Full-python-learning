import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin "] 
    
    @classmethod # You can call class method without initiating it , it does not need object to call
    def sort(cls, name):
        print(name, "is im", random.choice(cls.houses))
            
Hat.sort("Harry")