#name Ethan Wright
#Class 5 hour
#assigment HW6

print("hello Word!")

nums = 9

if nums % 2 == 0:
    if nums % 3 == 0:
        print(nums // 2)
        print(nums // 3)
    else:
        print("that it is not divisible by 3")
        print(nums // 2)
else:
    if nums % 3 == 0:
        print("that it is not divisible by 2")
        print(nums // 2)
    else:
        print("that neither is divisible by 2 or 3")



