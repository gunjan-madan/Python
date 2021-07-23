#keyword arguments
#We can specify argument name with the value so that caller does not have to remember order of parameters.

''' Task 1:  Order of parameters '''
print("***** Task 1: *****")
print()

# def studentDetails(name,ID, age, city, school):
#   print("Student's name is ", name)
#   print(name, "'s' ID is ", ID)
#   print(name, "'s' age is ",age)
#   print(name, "'s' resides in ", city)
#   print(name, "'s' studies in ", school )

#Call the function


#In the above way, we have to remember the order of parameters.

#studentDetails(name="Michael", age=12, city="NY", ID=1234, school="Sommerville")

''' Task 2:  Variable arguments '''
print("***** Task 2: *****")
print()
#We can also pass varying number of arguments to the function
# def myFun(*args): 
#     for arg in args: 
#         print (arg)

# print("Result of * args: ")
# myFun('Hello', 'Welcome', 'to', 'Python')

''' Task '''
#Write a function that take **args (all integers and min 5 numbers) and find their average


''' Task 4:  Variable arguments with Keywords '''
print("***** Task 4: *****")
print()
#Can also pass varying number of arguments through keywords using double star
def myFun2(**kwargs): 
    for key, value in kwargs.items():
        print ("% s == % s" %(key, value))


print("\nResult of **kwargs")
myFun2(first ='Coding', mid ='Is', last ='Interesting') 


''' Task '''
#Write a function that take **kwargs 
#Take five numbers input from user, send it to function using **kwargs with their keywords (First, Second, Third, Fourth, Fivth)
#Find the maximum and print the number along with the keyword


'''Task4: Global vs Local Variables'''
print("***** Task 4: *****")
print()
#Global variables are the ones that are defined and declared outside any function and are not specified to any function. They can be used by any part of the program.
#Local variables are specific to a particular function
# This function has a variable with 
# name same as s. 

# def f():  
#     s = "Me too."
#     print(s) 
    
# # Global scope 
# s = "I love python" 
# f() 
# print(s)
