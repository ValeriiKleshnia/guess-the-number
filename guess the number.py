import random
number_to_guess = random.randint(1, 100)
while True:
 guess = int(input("Guess a number from 1 to 100:"))
 if guess == number_to_guess:
  print("Congratulations, you have guessed the number!")
  break
 elif guess < number_to_guess:
  print("The hidden number is greater.")
 else:
  print("The hidden number is smaller.")

