import argparse

parser = argparse.ArgumentParser(description="Then Program prints the name of dog")

parser.add_argument("-c", "--color", metavar="color",required=True, choices={"red", "yellow"},
                    help="The color to search for")
args = parser.parse_args()
print(args.color)