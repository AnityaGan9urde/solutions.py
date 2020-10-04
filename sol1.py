#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#This is the solution for the first exercise:

name = input("Your name: ") #name input
age = int(input("Your age: ")) #age input in int
print("Your name is " + name)
print("Your age is " + str(age))

#Now the year when the person turns 100
year = 2020 + (100 - age)
print(name + " you will turn 100 in the year " + str(year) + ".")
