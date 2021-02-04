# Question 2
inputs = []
done = False

print("Input positive floats and press enter until done. When done, type 0.")

while not done:
    val = float(input())

    if val == 0:
        break

    elif val > 0:
        inputs.append(val)
        
    else:
        continue

def maxFunction(inputs):
    max = 0

    for i in inputs:
        if float(i) > max:
            max = float(i)
    
    return max

def minFunction(inputs):
    min = float('inf')

    for i in inputs:
        if float(i) < min:
            min = float(i)
    
    return min

def averageFunction(inputs):
    sum = 0
    
    for i in inputs:
        sum += i

    return sum / len(inputs)

print("Question 2: ")
print("The max of your list is: " + str(maxFunction(inputs)))
print("The min of your list is: " + str(minFunction(inputs)))
print("The average of your list is: " + str(round(averageFunction(inputs), 3)))
