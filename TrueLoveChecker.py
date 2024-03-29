# Instructions

# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

#     Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

# e.g.

# name1 = "Angela Yu"

# name2 = "Jack Bauer"

# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."
# Example Input 1

# name1 = "Kanye West"
# name1 = "Kanye West"

# name2 = "Kim Kardashian"
# name2 = "Kim Kardashian"

# Example Output 1

# Your score is 42, you are alright together.
# Your score is 42, you are alright together.

# Example Input 2

# name1 = "Brad Pitt"
# name1 = "Brad Pitt"

# name2 = "Jennifer Aniston"
# name2 = "Jennifer Aniston"

# Example Output 2

# Your score is 73.
# Your score is 73.

# e.g. When you hit run, this is what should happen:

# https://cdn.fs.teachablecdn.com/nfSILIPSNaIOwWhPR5vr

# The testing code will check for print output that is formatted like one of the lines below:

# "Your score is 47, you are alright together."
# "Your score is 125, you go together like coke and mentos."
# "Your score is 54."
# "Your score is 47, you are alright together."
# "Your score is 125, you go together like coke and mentos."
# "Your score is 54."

# Hint

#     The lower() function changes all the letters in a string to lower case. 

# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

#     The count() function will give you the number of times a letter occurs in a string. 

# https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

#===My solution:
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
L_name1= name1.lower()
L_name2= name2.lower()
T_Name = L_name1.count("t") + L_name2.count("t")
R_Name = L_name1.count("r")+ L_name2.count("r")
U_Name = L_name1.count("u")+ L_name2.count("u")
E_Name = L_name1.count("e")+ L_name2.count("e")
true_total= T_Name + R_Name + U_Name +E_Name

L_Name = L_name1.count("l") + L_name2.count("l")
O_Name = L_name1.count("o")+ L_name2.count("o")
V_Name = L_name1.count("v")+ L_name2.count("v")
#E_Name = L_name1.count("e")+ L_name2.count("e")
love_total= L_Name + O_Name + V_Name +E_Name
Love_Score = int(str(true_total) + str(love_total))

if Love_Score<15 or Love_Score >90:
  print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif  Love_Score >=40 and Love_Score <=50:
  print(f"Your score is {Love_Score}, you are alright together.")
else:
  print(f"Your score is {Love_Score}.")