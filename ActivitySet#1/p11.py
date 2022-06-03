# Regular Expressions

'''
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
'''

import re
fh = open("regex_sum_269097.txt")
sum = 0
for line in fh:
    num = re.findall('[0-9]+',line)
    length = len(num)
    for i in range(length):
        sum += int(num[i])
print(sum)