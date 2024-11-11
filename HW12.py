#Name:Ethan Wright
#Class: 5th Hour
#Assignment: HW12

#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.
num = 5
for i in range(num):
    print (num)
    num -= 1
print("Hello World!")
#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
for i in range(31):
    if i % 2 == False:
        print(i)
I = 1
while i < 30:
    print(I)
#3. Create a for loop that prints 5 different animals from a list.
animals = ("Bear", "Lion" , "bat", "monkey" , "house")
for i in animals:
    print(i)
#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")

txt = "batman" [::-1]
print(txt)

