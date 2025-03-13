#store inputs
numbers = []
#ask numbers until invalid
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    #handle invalid input
    except ValueError:
        break
#sort numbers from highest to lowest
numbers.sort(reverse= True)
#print output
print("The numbers entered from highest to lowest are: ", numbers)