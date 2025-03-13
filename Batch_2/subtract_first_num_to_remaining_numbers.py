#variable to store inputs
numbers = []
#ask 10 numbers
for num in range(10):
    user = int(input("Enter a number: "))
    numbers.append(user)
#set variable to first input
answer = numbers[0]
#iterate first input to subtract to remaining numbers
for num in numbers[1:]:
    answer -= num
#print result
print("The first number subtracted to the remaining numbers is: ", answer)