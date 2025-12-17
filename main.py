print("grade checker program")

name = input("enter your name: ")
score = int(input("enter your score: "))

if score >= 90:
    print(f"{name}, your grade is A")
else:
    print(f"{name}, your grade is low")