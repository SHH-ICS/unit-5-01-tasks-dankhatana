# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

random_num = random.randint(start, end)

print("Random number:", random_num)
