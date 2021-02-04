# Question 1
# implementation
print("Enter four numbers, pressing enter after each.")

inputs = []
done = False
iter = 0

while not done:
    if iter == 3:
        done = True

    val = float(input())
    inputs.append(val)
    iter += 1
    
def maxFunction(inputs):
    max = 0

    for i in inputs:
        if int(i) > max:
            max = int(i)
    
    return max

def minFunction(inputs):
    min = float("inf")

    for i in inputs:
        if int(i) < min:
            min = int(i)
    
    return min

# testing
print("Question 1:")
print("The maximum of your list is: " + str(maxFunction(inputs)))
print("And the minimum of your list is: " + str(minFunction(inputs)))
