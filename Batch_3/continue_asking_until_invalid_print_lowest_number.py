#store inputs
numbers = []
#while loop to ask continuously
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
        #invalid condition
        if num < 0:
            break
    #Handle error
    except ValueError:
        print("Invalid input.")
#print lowest number