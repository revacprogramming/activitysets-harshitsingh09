# Regular Expressions

'''
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
'''

count = 0
reg = open(regex.txt)
