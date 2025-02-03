def meow(n: int) -> str:
    """
    meow n times
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    ;rtype: str
    """
    return "meow\n" * n
    
number: int = int(input("Enter number: ")) # The colons : just show what type variable should be
cat: str = meow(number)
print(cat, end="")