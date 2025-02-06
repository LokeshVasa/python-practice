print("Guess any random number from 0 to 100")
import random
input_number=int(input("GUESS THE NUMBER!!:-"))
generate_random_number=random.randint(0,100)
if (input_number == generate_random_number):
    print("CORRECT")
else:
    print("try Again")
    print(" ",generate_random_number)