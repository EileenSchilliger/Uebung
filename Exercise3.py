
import random
num = random.randint(0,100)

print("Guess a number between 0 and 100.")

while True:
      ty = int(input("Guess the right number:"))
      if ty < num:
        print("the number is bigger")
      if ty > num:
        print("the number is smaller")
      if ty == num:
        print("Congratulations, this is the right number!")
        break