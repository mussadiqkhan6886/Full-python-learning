def main():
    get_pattern(3)    

def get_pattern(size):
    for _ in range(size): # Loop until given size
        get_row(size)
        
def get_row(n): # Its for each row
    print("#" * n) # Print '#' 3 times
    
main()