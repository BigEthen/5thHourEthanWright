#Name:Ethan Wright
#Class: 5th Hour
#Assignment: HW15


#1. Create a def function that prints out "Hello World!"

#2. Create a def function that calculates the average of three numbers.

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.

#4. Create a def function that loops from 1 to the number put in the argument.

#5. Call all of the functions created in 1 - 4 with relevant arguments.

def hello_world():
    print("hello world!")

def average(one,two,three):
    return one+two+three / 3
print (average(3,3,3))

def fun(b1,b2,b3,b4,b5):
    return [b1,b2,b3,b4,b5]
fun = fun("cat","Dog","Goat","mouse","cow")
print("Goat")

for i in range(1):
    def f():
     return i

