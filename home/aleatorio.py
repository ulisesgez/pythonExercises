import random

random_integer = random.randint(1, 10)
print(random_integer)# 1 - 10

random_float = random.random()
print(random_float)# 0.000000 - 0.999999

random_float * 5 # 0.000000 - 4.999999

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

#

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")