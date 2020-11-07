#
# Read two numbers, generate 2D array
#
input_str = input()
print(input_str.split(','))
rows, cols = input_str.split(',')
rows, cols = int(rows), int(cols)
matrix = [[x*y for y in range(cols)] for x in range(rows)]
print(matrix)