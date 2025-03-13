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
if numbers:
    frequency = {}

    for num in numbers: #check whether number is already entered
        if num in frequency:
            frequency += 1
        else:
            frequency = 1
#find the number with the highest frequency
#print output