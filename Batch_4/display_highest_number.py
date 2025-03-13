#store inputs
numbers = []
#ask continuously until invalid
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    #handle invalid input
    except ValueError:
        break    
#print output
print("The highest number entered is: ", max(numbers))