#store input
numbers = []
#ask for 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
#identify whether a number appeared only once
unique_number = [num for num in numbers if numbers.count(num) == 1]
#print output
print("The numbers without duplicate are: ", unique_number)