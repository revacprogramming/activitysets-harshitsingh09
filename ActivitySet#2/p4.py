# Break a string into a list and then join the list into a string again

def get_cs():
    x = str(input("Enter a string:\n"))
    return x

def cs_to_lot(cs):
    x = list(cs)
    return x

def lot_to_cs(lot):
    x = "".join(lot)
    return x

def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()