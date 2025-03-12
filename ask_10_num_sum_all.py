#Store the numbers
sum = 0
#Ask for 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))
    sum += num #add the number to the previous input
#Print sum of all
print("The sum of the 10 numbers is: ", sum)