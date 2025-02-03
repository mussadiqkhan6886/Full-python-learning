from String import hello

def main():
    testing_default()
    testing()

def testing_default():
    assert hello() == "hello, World"
    
def testing():
    assert hello("Mussadiq") == "hello, Mussadiq"
    
if __name__ == "__main__":
    main()