import random

print("\t*** HUNGMAN GAME ***\n")

movies = ['pushpa', 'avengers', 'bahubali', 'avtar', 'pathan', 'mission impossible']
one_movie = list(random.choice(movies).lower())

chance = 5
s = ["_ " for i in one_movie]
print("Guess the Movie name: ")
print(" ".join(s))
while chance != 0:
    print(f"\tyou have {chance} chance left.")

    ch = input("\nGuess the Movie name: ").lower()

    if ch not in one_movie:
        print("you have guessed wrong...!!")
        chance -= 1
        print(" ".join(s))
        continue
    j = 0
    for i in one_movie:
        if i == ch:
            s.pop(j)
            s.insert(j, ch)
        j += 1
    print(" ".join(s))
    if s == one_movie:
        print("\n\tYou *** WIN *** the Game.... !!!")
        break
else:
    print("\n\tYou loose the Game..!!")
