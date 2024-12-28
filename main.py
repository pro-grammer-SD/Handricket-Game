from random import randint

print("Welcome to Soumalya's Hand-Cricket Game!")
choice = input("Select your choice: 1 for Batting, 2 for Bowling: ")

score = []

if choice == "1":
    print("You have chosen to bat first!")
    notOut = True
    while notOut:
        user = int(input("Enter your number: "))
        computer = randint(1, 10)
        print(f"Computer's number: {computer}")
        if user == computer:
            print("You are out!")
            notOut = False
        else:
            score.append(user)
            print(f"Your score: {sum(score)}")

elif choice == "2":
    print("You have chosen to bowl first!")
    notOut = True
    while notOut:
        user = int(input("Enter your number: "))
        computer = randint(1, 10)
        print(f"Computer's number: {computer}")
        if user == computer:
            print("Computer is out!")
            notOut = False
        else:
            score.append(computer)
            print(f"Computer's score: {sum(score)}")
else:
    print("Invalid input! Please try again.")