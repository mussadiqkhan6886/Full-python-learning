from testing import square

def main():
    positive_test()
    negative_test()
    zero_test()
    
def positive_test():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
    
def negative_test():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9

def zero_test():
    assert square(0) == 0

if __name__ == "__main__":
    main()