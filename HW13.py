#Name:Ethan Wright
#Class: 5th Hour
#Assignment: HW13


#1. Create a list containing 10 integers of your choice.
yrr = (10,15,20,25,30,35,40,45,50,55)
#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for i in yrr:
    if i % 2:
        evenNumbers += 1
    else:
        oddNumbers += 1
# Print the total count of even and odd numbers.
print(evenNumbers, "even numbers")
print(oddNumbers, "odd numbers")