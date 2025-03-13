#store inputs
numbers = []
#continuously ask until invalid
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    #handle invalid input
    except ValueError:
        break
#average the numbers
if numbers:
    average = sum(numbers) / len(numbers)
#print result
print("The average of all the numbers entered is: ", int(average))