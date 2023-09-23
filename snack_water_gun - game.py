import random
choice = 'y'
while choice == 'y':
    turn = 5
    item = ["s", "w", "g"]

    comp_points = 0
    user_points = 0
    draw_points = 0

    print("GAME \n  SNACK, WATER & GUN \n")
    print(" s for Snack\n w for Water\n g for Gun")
    user_name = input("Enter Your Name: ")
    while turn > 0:
        select = random.choice(item)
        print("--------X-----X-----X-----X--------")
        user_choice = input("\n Enter your choice: ")

        if select == user_choice:
            turn -= 1
            print(f"\nMatch DRAW...!!!\n\t better luck for next time\n you have only {turn} turns")
            draw_points += 1

        elif select == 's' and user_choice == 'w':
            turn -= 1
            print(f"\nOop's you loose...!!!\n\t better luck for next time\n you have only {turn} turns")
            comp_points += 1

        elif select == 'w' and user_choice == 'g':
            turn -= 1
            print(f"\nOop's you loose...!!!\n\t better luck for next time\n you have only {turn} turns")
            comp_points += 1

        elif select == 'g' and user_choice == 's':
            turn -= 1
            print(f"\nOop's you loose...!!!\n\t better luck for next time\n you have only {turn} turns")
            comp_points += 1

        elif select == 'w' and user_choice == 's':
            turn -= 1
            print(f"\nyou win...!!!\n\t GOOD LUCK\n you have only {turn} turns")
            user_points += 1

        elif select == 's' and user_choice == 'g':
            turn -= 1
            print(f"\nyou win...!!!\n\t GOOD LUCK\n you have only {turn} turns")
            user_points += 1

        else:
            print("Invalid choice")

    print("--------X-----X-----X-----X--------")
    print(f"\n Draw {draw_points}\n You Won {user_points}\n Computer Win {comp_points}")

    print("--------X-----X-----X-----X--------")
    if user_points > comp_points:
        print(f"\nCongratulations {user_name}....!!!\n you won the Game")
    elif user_points == comp_points:
        print(f"\n Dear {user_name}....!! Match Draw")
    else:
        print(f"\nYou Loose the Game\n Try Again {user_name}")

    choice = input("\n Play Again(y/n): ")
    if choice == 'y':
        continue
    else:
        break