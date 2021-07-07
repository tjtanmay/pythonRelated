import random
import math
upper=int(input("Enter range, Upper bound:\n"))
lower=int(input("Lower bound:\n"))
x = int(random.randint(lower, upper))
chance_left= round(math.log(upper - lower + 1, 2))
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
count=0
while (count < chance_left):
	count +=1
	print (f"guess number {count}:")
	guess=int(input("enter your guess: \n"))
	
	if guess == x:
		print("Congratulations!")
	elif guess < x:
		print("Try Again! You guessed too small")
	elif guess > x:
		print("Try Again! You guessed too high")
	elif count==chance_left:
		print("Better Luck Next Time!")
		break;

		
