

def remove_char(char, str):
    return str.replace(char, "")


def main():
    s = "string"    ### string
    c = "i"         ### character
    
    print(s)
    s = remove_char(c, s)
    print(s)






if __name__ == "__main__":
    main()