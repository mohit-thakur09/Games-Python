import random

print("********** GUESSING NUMBER GAME **********")
print("\nGuess number in between 1 to 50.\n you have 5 chance to guess!")

ans = random.randint(1, 50)
chance = 5

name = input("\nEnter your name: ")
print("-------------------------------------------------")
print("Now Game starts...")
print("-------------------------------------------------")

while chance != 0:
    num = int(input("\nEnter Number: "))
    if num < ans:
        print('\tAdd some more numbers!!')
    elif num > ans:
        print('\tsubtract some more numbers!!')
    elif num == ans:
        print(f'\t******* {name}!!********')
        print('\t*******You Win The GAME!!********')
        break
    chance -= 1
    print(f"You Have {chance} chance left!! ")
    print("-------------------------------------------------")
else:
    print("Correct number is: ", ans)
    print(f'\t {name}')
    print('\t OOPS!! You LOOSE The GAME!!')
