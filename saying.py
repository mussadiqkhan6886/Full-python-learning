# main function having hello and goodbye fucntions
def main():
    hello("World") # arguement World
    goodbye("World") # arguement World

def hello(name):
    print(f"Hello {name}")

def goodbye(name):
    print(f"Goodbye {name}")
   
if __name__ == "__main__":  # If this code or .py file is execute directly from here it will call main() else if wont execute if its imported
    main()