num1 = 0
num2 = 999
count = 0

while num1 != num2:
    num1 = int(input())
    
    if num1 < 0:
        break
    
    print('num1 = ', num1)

    if (num1 % 2) == 0:
        count += 1
    
print('Number of positive even inputs: ', count)