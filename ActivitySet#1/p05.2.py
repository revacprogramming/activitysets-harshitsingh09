# Loops & Iterators

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = 0
smallest = 0
while True:
  try:
    num = (input("Enter a number: "))
    if num == 'done':
      break
  except:
      print("Please enter integers only")
      continue
  #code needs fixing
  num = float(num)
  if (num > smallest):
    largest = num
  else:
    smallest = num
print("Maximum is ", largest)
print("Minimum is ", smallest)