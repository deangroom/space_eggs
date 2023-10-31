'''
A def() function is a routine that performs a specific task.
When we want a program to perform a task, we call the function that performs that task.
Often, computers are used to automate repetitive tasks.
'''
# This function adds two numbers
def add(a, b):
    return a + b
# it 'returns' the result of adding two numbers using the 'return' keyword

# the function is a self contained unit of code that can be called from anywhere in the program
# if you click the arrow to the left of the line number, you can collapse the function
# this means it's not part of the main program and you can't see the code inside it unless you expand it
# this is useful for keeping your code tidy and organised
# it also means you can reuse the function in other programs

#here is how we call the function
print(add(2, 3))
# the function is called with two arguments, 2 and 3
# the function returns the result of adding 2 and 3, which is 5
# the result is printed to the console

# we can also call the function with variables
x = 5
y = 7
print(add(x, y))
# the function is called with the variables x and y
# the function returns the result of adding x and y, which is 12
# the result is printed to the console

number1 = int(input("Enter a number: ")) #we've done this before right?
number2 = int(input("Enter another number: ")) #we've done this before right?

add(number1, number2) #this doesn't output anything at all, it just runs the result of the function which is the sum of the two numbers

if add(number1, number2) > 10: #this is a conditional statement
    print("The sum of your numbers is greater than 10") #this is the code that will run if the condition is true
else:
    print("The sum of your numbers is less than 10")

#here we are using the return value of the function to determine what code to run next. It's called a binary decision

#here is another example of a function
def say_hello(name):
    print(f"Hello {name}")

say_hello("John") #this will print "Hello John" to the console
say_hello("Mary") #this will print "Hello Mary" to the console
say_hello("Bob") #this will print "Hello Bob" to the console

'''
Functions are useful because they allow us to reuse code
We can write a function once and use it many times
We can also pass different values to the function each time we call it
This makes our code more efficient and easier to maintain
'''



