#
# Read two numbers, generate 2D array
#
input_str = input()
myList = input_str.split(',')
myList.sort(key=str.lower, reverse=True)
# myList = sorted(input_str.split(','))
print(myList)