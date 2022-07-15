# Convert connected string to list of strings

def get_cs():
    x = str(input("Enter a string:\n"))
    return x

def cs_to_lot(cs):
    x = list(cs)
    return x

def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)

if __name__ == '__main__':
    main()