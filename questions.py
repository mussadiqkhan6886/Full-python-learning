qusetions = {
    "a":"Who created python language?:\n \na)Guido Van Rossum\nb)Elon Musk\nc)Markzuker burg",
    "b":"Is Earth Flat:\n \na)Yes\nb)No\nc)Cube",
    "c":"Who created meta:\n \na)Guido Van Rossum\nb)Elon Musk\nc)Markzuker burg",
}

def logic():
    score = 0
    for key, values in qusetions.items():
        print("\n", values)
        answer: str = input("Enter answer a,b or c: ")
        if answer == key:
            score += 1
            print("\nCORRECT")
        else:
            print("\nWRONG")
        total = float(f"{score/len(qusetions) * 100}")
    print(f"\nYour score percantage is: {round(total, 3)}")
    print(f"Your score is {score} out of {len(qusetions)}")
        
        
logic()