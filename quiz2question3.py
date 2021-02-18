# Question 3
print("Tree height?: ")
cols = abs(int(input()))
rows = 2 * cols - 1

for x in range(rows):
    star = False

    for y in range(cols):
        w = cols - 1
        T_x = w - abs(w - x)

        if (T_x + y) == w:
            star = True

        if star:
            print("<3", end = "")
        else:
            print("  ", end = "")

    print("")    
           
print("Level = ", cols)
