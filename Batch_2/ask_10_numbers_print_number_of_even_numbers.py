#store count of even numbers
even_numbers = 0
#ask 10 numbers
for num in range(10):
    user = int(input("Enter a number: "))
#identify if number is even
    if user % 2 == 0:
        even_numbers += 1
#print output
print("The number of even numbers is: ", even_numbers)