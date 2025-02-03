def main():
    n = int(input("Enter number: "))
    sq = square(n)
    print(f"square of {n} is {sq}")
    
def square(n):
    return n + n


if __name__ == "__main__":
    main()