#store the odd numbers
odd_numbers = []
#use while loop to print numbers to 100
count = 0
while count < 100:
    count += 1
    if count % 2 == 1:
        odd_numbers.append(count)
#print output
print("The odd numbers from 0 to 100 are: ", odd_numbers)