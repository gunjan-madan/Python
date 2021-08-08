#Errors and Exceptions

''' Task 1:  Exception(al) '''
print("***** Task 1: *****")
print()
# Uncomment each block of code, one at a time, and analyze the output
## Code Block 1
#num=1
#if num == 1
 #print("What is the output?")
 
## Code Block 2
#def incrementsal(sal):
# salary = sal*20/100
# return salary
## Call incrementsal() to get the incremented total salary
#print(incrementsal(2000))
 
## Code Block 3
#def add(num1,num2):
# print(num1+num2)
## Call add() to get the total
#add("st",12)

# What do you think happened in each code block? 
# Here we are looking at three types of error
# Code Block 1: Compile-Time Error
# - Here the code block has syntactical errors due to which the code fails to compile
# Code Block 2:  Logical Error
# - Here there is an error in the logic of the program. The incremented value should have been added to the existing salary.
# Code Block 3: Runtime Errors
# - Here the error is not detected by the compiler, but only when the program runs the desired output is not seen.

# An exception is handled using the following blocks:
# - try
# - except
# - else
# - finally 

# try block contains the code where there is a possibility of exceptions
# except block allows you to handle the error
# else block is executed if there is no exception
# finally block contains code that is executed, irrespective of the result of the try- and except blocks
# Note: else and finally blocks are not compulsory
# Uncomment the statement below, click Run 


#try:
# print(y)
#except:
# print("An exception occurred")


# What did you observe?
# The try block will generate an error, because 'y' is not defined
# Uncomment the statement below, click Run

#try:
#  print("Enjoy your coding classes")
#except:
#  print("Something went wrong")
#else:
#  print("All is well")
 
# What did you observe? 
# The try block does not raise any errors, so the else block is executed.


''' Task 2:  Try and Succeed '''
print("***** Task 2: *****")
print()
# Write a program that asks the user to enter two numbers and displays the sum if numbers are entered else displays an error message.


''' Task 3: Raise the Error '''
print("***** Task 3: *****")
print()
# You can use raise keyword to throw an exception if a condition has to be satisfied. . 
# The error message can be customized.
# Uncomment the statements and click Run.

#y = 10
#if y > 5:
#    raise Exception("x should not exceed 5.")

# What did you observe? 
# You will notice that the custom error message is displayed when the error occurs
# Write a program asking the user to enter a username which is not more than 15 characters in length. An exception should be raised if the length is greater than.

