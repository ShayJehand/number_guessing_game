import random

correct_guess=0
rounds= 0
while True:
    rounds += 1
    computer = random.randint(1,10)

    try:
       user_guess=int(input("Enter a number(1-10)."))

    except ValueError:
                 print("Invalid input! Please enter numbers only.")
                 continue
    
    if user_guess < 1 or  user_guess >10:
            print("Please enter a number between 1 and 10")
            continue
            
    if user_guess == computer:
        print("Great! You guessed it right")
        correct_guess += 1

        choice = input("Do you want to play again?(Yes/NO).").lower().strip()

        if choice == "no":
            print("Goodbye!")
            break 

        
    elif user_guess > computer:
        print("Too high!","It is",computer)

    else:
        print("Too low!","It is ",computer)
    
   

print(f"You played {rounds} rounds.")
print(f"You guessed it {correct_guess} times.")