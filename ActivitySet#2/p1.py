def add(a, b):
    sum = a + b
    return sum


def main():
    a = int(input("Enter first number!\n"))
    b = int(input("Enter second number!\n"))
    c = add(a, b)
    print(f"The sum of {a} and {b} is {c}")

main()