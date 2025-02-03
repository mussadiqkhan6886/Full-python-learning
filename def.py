# A main function which have another is_even function
def main():
    x = int(input("Enter x value: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
    
def is_even(n):
    return True if n % 2 == 0 else False # by using Teriatry operator
    # or
    # return n % 2 == 0 it will return true or false by own 
main()