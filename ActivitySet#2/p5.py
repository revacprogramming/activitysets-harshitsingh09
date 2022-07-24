# Convert a string to dictionary 

def get_cs():
    x = str(input("Enter a string:\n"))
    return x

def cs_to_dict(cs):
    x = cs.split()
    #print(x)
    x.remove('=')
    print(x)

def dict_to_cs(d):
    pass
    
def main():
    cs = get_cs()
    d = dict()
    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)    

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()