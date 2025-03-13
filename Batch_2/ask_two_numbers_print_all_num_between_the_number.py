#ask 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#print all the numbers between the input
num1, num2 = sorted([num1, num2]) #arrange the input in ascending order
print(f"The numbers between {num1} and {num2} are: ")
for numbers in range(num1 + 1, num2):
    print(numbers, end = "\n")