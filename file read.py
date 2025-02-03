with open("names.txt") as file:
    for name in sorted(file):
        print(f"hello, {name.rstrip()}")