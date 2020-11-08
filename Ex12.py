#
# Find and print all numbers with only even digits within a given range
#
skipDigits = ['1', '3', '5', '7', '9']
for number in range(23,100):
    numberChars = str(number)
    for x in skipDigits:
        if (x in numberChars):
            # print(number, 'has some odd digits')
            break
    else:
        print(number, 'has all even digits')