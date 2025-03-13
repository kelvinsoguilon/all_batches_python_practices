#use for loop to iterate 100 numbers
print("The numbers from 0 to 100 except ending in 0 and 5 are: ")
for numbers in range(100):
    if numbers % 5 != 0:
        print(numbers, end=",")    #print result