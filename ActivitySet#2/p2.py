# Sum of two numbers using functions

def add(a, b):
    sum = a + b
    return sum

def output(a, b, sum):
    print(f"Sum of {a} and {b} is {sum}")

def input_two_numbers():
    a = int(input("Enter first number:\n"))
    b = int(input("Enter second number:\n"))
    return a, b

def main():
    a, b = input_two_numbers()
    sum = add(a, b)
    output(a, b, sum)


if __name__ == '__main__':
    main()