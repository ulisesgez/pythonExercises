"""
Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.
Example Input 2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
Example Output 2
Your score is 73.
The testing code will check for print output that is formatted like one of the lines below:

"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."
Score Comparison
Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.

Name 1	Name 2	Score
Catherine Zeta-Jones     	Michael Douglas    	99
Brad Pitt	Jennifer Aniston	73
Prince William	Kate Middleton	67
Angela Yu	Jack Bauer	53
Kanye West	Kim Kardashian	42
Beyonce	Jay-Z	23
John Lennon	Yoko Ono	18
"""
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
completename = name1 + name2
letters1 = ["t", "r", "u", "e"]
letters2 = ["l", "o", "v", "e" ]
count1 = 0
count2 = 0

for letter in completename:
    if letter in letters1:
        count1 += 1
for letter in completename:
    if letter in letters2:
        count2 += 1
convert = (str(count1) + str(count2))
result = int(convert)

if result < 48:
    print(f"Your score is {result}, you are alright together.")
elif result < 125:
    print(f"Your score is {result}.")
else:
    print(f"Your score is {result}, you go together like coke and mentos.")