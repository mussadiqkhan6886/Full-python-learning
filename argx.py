def main():
    yell("This", "is", "CS50")
    
def yell(*words):
    # List comprehension
    # up = [word.upper() for word in words] 
    up = map(str.upper, words) # Using map function
    print(*up) # Unpacking list
    
main()