students = [
    {"name": "Hermione", "house" : "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house" : "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house" : "Griffandor", "patronus": "Jack Rusell terrier"},
    {"name": "Draco", "house" : "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"],student["house"], student["patronus"], sep=", ")
    