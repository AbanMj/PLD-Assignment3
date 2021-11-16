#Program 2: Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number

def lowest_func():
    first = int(input("Enter your 1st number: "))
    second = int(input("Enter your 2nd number: "))
    third = int(input("Enter your 3rd number: "))
    return first, second, third

first, second, third = lowest_func()

if first < second and first < third:
    small = first
else:
    if second < first and second < third:
        small = second
    else:
        if third < first and third < second:
            small = third
        else:
            pass

print(f"The lowest number among the 3 numbers is {small}.")
