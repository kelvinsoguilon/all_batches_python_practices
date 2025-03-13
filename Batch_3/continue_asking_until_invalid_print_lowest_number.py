#store inputs
numbers = []
#while loop to ask continuously
while True:
    try:
        num = int(input("Enter a number: "))
        #invalid condition
        if num < 0:
            break
        #ensures negative numbers are not stored
        numbers.append(num)
    #Handle error
    except ValueError:
        print("Invalid input.")
#print lowest number
print("The lowest number is:", min(numbers))