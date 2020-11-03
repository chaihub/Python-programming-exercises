#
# Find all multiples of 7 in a range that are not divisible by 5
#
result=[]
for num in range(15,72):
    if (num%7 == 0) and (num%5 != 0):
        result.append(num)

print(result)