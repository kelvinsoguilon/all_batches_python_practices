#Variable to store value
odd_number = 0
#Ask for 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))

    if num % 2 == 1: #process to identify if a number is odd
        odd_number += 1 
#Print the number of odd numbers
print("The number of odd numbers entered is: ", odd_number)