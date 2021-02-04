# Question 3
print("Number of rows: ")
rows = int(input())

print("Number of columns: ")
cols = int(input())

for i in range(0, rows):
    for j in range(0, cols):
        if (i > 0 and i < (rows - 1)) and (j > 0 and j < (cols - 1)):
            print(" ", end = "")
        
        elif (i == 0 or i == (rows - 1)) and (j > 0 and j < (cols - 1)):
            print("-", end = "")

        elif (j == 0 or j == (cols - 1)) and (i > 0 and i < (rows - 1)):
            print("|", end = "")
        
        else:
            print("+", end = "")

    print("")
