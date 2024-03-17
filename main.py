#Maru Puran
#October 24 2023
#Create a program using conditionals to get a better understanding of their different usages and how programs can be adapted based on user input, and make choices based on it; program makes user enter a number and outputs a message based on what time of day the number equivilates to


###program time reminder

print("This is a program to tell you a schedule based on the time of day.\n")

number = int(input("Please enter a number between 0 and 23, inclusive, in integer form!: ")) #have the user input a number between 0 and 23; convert from string to integer and store in variable number

if number < 8: #check if user inputted number is less than 8
  print("It's too early to get up...") #if less than 8 print message in quotations
elif number < 12: #else check if user inputted number is less than 12
  print("Good morning!") #if less than 12 print message in quotations
elif number < 14: #else check if user inputted number is less than 14
  print("Lunch time!") #if less than 14 print message in quotations
elif number < 18: #else check if user inputted number is less than 18
  print("Good afternoon!")  #if less than 18 print message in quotations
elif number == 18: #else check if user inputted number equals 18
  print("Tea time!") #if equals to 18 print message in quotations
elif number < 19: #else check if user inputted number is less than 19
  print("Good evening!") #if less than 19 print message in quotations
elif number <= 22: #else check if user inputted number is less than 22
  print("Nearly bedtime!")  #if less than 22 print message in quotations
elif number == 23: #else check if user inputted number is equal to 23
  print("Good night!")  #if equal to 23 print message in quotations
elif number < 0 or number > 23: #else checks if number is less than 0 or greater than 23, meaning it's out of range
  print("Sorry, I don't recognize that.") #let user know the computer can't recognize it