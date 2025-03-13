#store input
numbers = []
#ask continuously
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    #invalid condition
    except ValueError:
        break
#check the frequency of numbers
#find the number with the highest frequency
#print output