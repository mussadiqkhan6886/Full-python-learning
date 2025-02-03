def main(): # Main function
    number = get_number()
    meow(number)
    
def get_number(): # It will not accept value less than 1
    while True: # Loop until you enter number higher than 0
        n = int(input("Enter how many times you wanna print meow: "))
        if n > 0:
            break
    return n # return value of n
def meow(n): # Function saying meow
    for _ in range(n):
        print("Meow")
        
main()