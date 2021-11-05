# ##rogerson robotics
# if an item costs more than €10000 the purvhaser rescives a message saying "go to tender"
# if an item  cost between €500 and €10000 inclusive the message received is "get 3 quotes"
# otherwise the item can be purchased.
# under should be asked for the cost of the item they want to purchase.
# there should be a welcome message 

# print ("welcome to rogerson robotics")
# item = int (input("how much do you want to pay? "))

# if item > 10000:
#   print ("go to tender fuck face")
# elif 500 <= item <= 10000:
#   print ("get 3 quotes")
# else:
#   print ("what would you like to buy")

#while loop 
# a while loop keeps repeating while the condition is true and stops when it is false . A while loop could keep going forever 

## create a variable called counter and initialise give it a starting value

# counter = 0 

# while counter<7 : 
#   print (counter)
#   counter +=1
# print ("the loop is finished")
# ##when the value gets above 6 , this will hapen . This isn the whole point where the condiotion is not TRUE anymore .




#example - entering grades 
## create variable yo let the user to enter their percentage

# grade = float (input("enter your grade mark between 0 and 100 percent"))

# while grade <0 or grade > 100 :
#   print ("error ! mark outisde of the accepted range")

#   grade = float (input("enter your grade mark between 0 and 100 percent"))

# Name: Guessing Game v3
# Purpose: A program to demonstrate the multiple if statement

# import random

# number = random.randint(1, 10)
# # The next line can be commented out later ...
# print(number) # have a sneak peek at the number to guess!

# guess = int(input("Enter a number between 1 and 10: "))

# # Evaluate the condition
# if guess == number:
#     print("Correct")
#     print("Well done!")
# elif guess < number:
#     print("Hard luck!")    
#     print("Too low")
# else:
#     print("Hard luck!")    
#     print("Too high")


# print("Goodbye")
###############################
##improve our code with a while loop
# we will give the user 3 guesses top guess the correct answer

# Name: Guessing Game v4
# Purpose: A program to demonstrate counter controlled repetition using while
# Description: The user is given 3 'chances'


# import random

# number = random.randint(1, 10)
# print(number) # have a sneak peek!

# # Initialise a loop counter
# counter = 0

# # Loop 3 times
# while counter < 3:

#     guess = int(input("Enter a number between 1 and 10: "))
#     if guess == number:
#         print("Correct")
#         break # exit the loop immediately!
#     elif guess < number:
#         print("Too low")
#     else:
#         print("Too high")

#     counter = counter + 1

# print("Goodbye")

################################################################# use booylan datatypes (true or False) user has unlimted guesses

# Name: Guessing Game v5
# Purpose: A program to demonstrate sentinel controlled repetition using while
# Description: The user is given an unlimited number of chances

# import random

# number = random.randint(1, 10)
# print(number) # have a sneak peek!

# correct = False # initialise the loop guard variable

# Loop until the variable 'correct' becomes True (while correct == False)
# while not correct: 

#     guess = int(input("Enter a number between 1 and 10: "))
#     if guess == number:
#         print("Correct")
#         correct = True # this will cause the loop to exit on the next iteration
#     elif guess < number:
#         print("Too low")
#     else:
#         print("Too high")


# print("Goodbye")

# Name: Guessing Game v7
# Purpose: A program to demonstrate data validation
# Description: This is the exact same as version 6 except the input is validated

# Guess Game v7 - while - go again? - data validation
# import random

# number = random.randint(1, 10)

# # Initialise the loop guard variable
# keepGoing  = True

# # Loop as long as keepGoing is True
# while keepGoing:

#     guess = input("Enter a number between 1 and 10: ")
#     # Validate. Make sure the value entered is numeric
#     while not guess.isdigit():
#        guess = input("Enter a number between 1 and 10: ")

#     # Convert the string to an integer
#     guess = int(guess)

#     if guess == number:
#         print("Correct")
#         goAgain = input("Play again? (Y/N): ")
#         if goAgain.upper() == "N":
#             keepGoing = False
#         else:
#             # Get a new number
#             number = random.randint(1, 10)

#     elif guess < number:
#         print("Too low")

#     else:
#         print("Too high")

# print("Goodbye")


# counter=0
# while counter<6:
#   number=int(input("please enter a number"))
#   print(number)
#   counter+=1

# sentance = input("enter a sentance : ")
# spacecount = 0 
# for word in sentance:
#  if word == " ":
#   spacecount +=1
# print("spaces=", spacecount)
# print("words=", wordcount)

# counter = 0
# while counter < 11:
#   print (counter)
#   counter +=1

# for num in range(1, 10):
#   print(num)















