# You are going to write a program that calculats the sum of all the even numbers from 1 to 100, including 1 and 100. 

EvenNumberTotal = 0
for number in range(1, 101):
	if number%2 == 0:
		EvenNumberTotal+= number
print (EvenNumberTotal)
