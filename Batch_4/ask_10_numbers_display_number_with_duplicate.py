#store unique and duplicates
unique_num = []
duplicate_num = set()
#ask 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))
    #check whether number is unique
    if num in unique_num:
        duplicate_num.add(num)
    unique_num.append(num)
#print output
print("The numbers with duplicates are: ", duplicate_num)