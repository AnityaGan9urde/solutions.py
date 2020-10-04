#Ask the user for a number. 
#Depending on whether the number is even or odd, print out an appropriate message to the user.
#Solution for the exercise:

num = int(input("Give a number: ")) #input number

#if the number is perfectly diveded by 2 then it is even
if num%2 == 0:
    print("The number is even.")
#if not then it is odd
else:
    print("The number is odd.")


#extra
if num%4 == 0:
    print("The number is also divisible by 4.")
