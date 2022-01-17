# Split string method
import random 
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


names_length= len(names)
#print(names_length) testing the length of the list
person = random.randint(0 ,names_length -1)
print (f"{names[person]} is going to buy the meal today!")


#better solution with choice() function: 
person_who_will_pay = random.choice(names)
print (person_who_will_pay + "is going to buy the meal today!")