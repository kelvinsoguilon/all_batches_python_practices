#store inputs
numbers = []
#ask continuously until invalid
while True:
    try:
        num = int(input("Enter a number: "))
        #invalid condition
        if num < 0:
            break
        #move input to list
        numbers.append(num)
    #handle ValueError
    except ValueError:
        print("Invalid input.")
#sort input from low to high
#print output