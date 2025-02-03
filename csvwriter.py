import csv

name = input("Enter Your name: ")
home = input("Enter your home: ")

with open("csvwri.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})