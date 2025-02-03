def main():
    x = get_int("Enter whats x: ")
    print(f"x is {x}")
    
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt)) # prompt will take any question as argument when caliing
        except ValueError:
            pass # It will pass ValueError if its catched 
            # We can also give statement for reminder 
            # print("Please enter int not string")
        else:
            return x # It will return value of x
    
main()