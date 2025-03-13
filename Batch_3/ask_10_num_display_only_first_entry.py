#store input
numbers = []
duplicated_number = set()
#ask for 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))
    #check if number already entered
    if num not in duplicated_number:
        numbers.append(num)
        duplicated_number.add(num)
#print result
print("The numbers displayed only in their first occurence are: ", numbers)