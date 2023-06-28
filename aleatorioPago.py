# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size = len(names) - 1
random_integer = random.randint(0, size)
selected = names[random_integer]
print(f"{selected} is going to buy the meal today!")