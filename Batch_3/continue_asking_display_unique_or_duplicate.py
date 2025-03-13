#store input and duplicates
unique_num = []
duplicate_num = set()
#ask number until invalid
while True:
    try:
        num = int(input("Enter a number: "))
        #invalid condition
        if num < 0:
            break
        #check whether first entry and print unique
        #check whether duplicate and print duplicate
