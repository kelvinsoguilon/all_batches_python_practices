#store the even numbers
even_number = []
#use for loop to iterate 100 numbers
for numbers in range(101):
    if numbers % 2 == 0: #check if num is even
        even_number.append(numbers)
#print the even numbers
print("The even numbers from 0 to 100 are: ", even_number)