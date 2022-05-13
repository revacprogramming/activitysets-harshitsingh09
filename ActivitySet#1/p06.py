# Loops & Iterators

# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

largest = None
smallest = None

while True:
    num = input("Enter a number? ")

    if num == "done":
        break

    # ...

    print(num)

print("Maximum", largest)
