class Students:
    def __init__(self, name, home):
        self.name = name
        self.home = home
        
    def __str__(self): #It will run just by simpling printing Students class
        return f"{self.name} from {self.home}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    # Getter
    @property
    def home(self):
        return self._home
    
    # Setter
    @home.setter
    def home(self, home):
        if home not in ["Gryffindor", "hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid home ")
        self._home = home
    
    @classmethod
    def get(cls):
        name = input("Enter name: ").title()
        home = input("Enter home: ").title()
        return cls(name, home)
    
def main():
    student = Students.get()
    # student.home = "Khan"
    print(student)
        
if __name__ == "__main__":
    main()