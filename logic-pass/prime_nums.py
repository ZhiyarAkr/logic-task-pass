
def main():
    n = 100 ###### Depth

    
    p = {4, 6, 8}
    j = 3
    r = 0
    if n >= 2:
        print(2)

    for i in range(3,n + 1):
        if i%2 and not i in p:
            j = 3
            while i%j and j < i:
                j = j + 1
            if i != j:
                p.add(i)
                r = i + i
                while r < n:
                    p.add(r)
                    r = r + i
            else:
                print(i)
        else:
            p.add(i)
                    





    

    









if __name__ == "__main__":
    main()