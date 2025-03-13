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
            frequency[num] += 1
        else:
            frequency[num] = 1
    #find the number with the highest frequency
    highest_frequency = None
    highest_count = 0

    for num, count in frequency.items(): #counts the appearance of a number
        if count > highest_count:
            highest_count = count #the number of appearance
            highest_frequency = num #find the number that appeared the most
#print output
print(f"The number with the most duplicate is {highest_frequency}, that appeared {highest_count} times.")