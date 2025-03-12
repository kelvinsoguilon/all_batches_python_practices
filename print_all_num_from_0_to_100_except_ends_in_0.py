#variable to store the numbers that don't end in 0
output = []
#iterate through 100 numbers
for numbers in range(101):
    #check if number ends in 0
    if numbers % 10 == 0:
        output.append(numbers)
#print the output