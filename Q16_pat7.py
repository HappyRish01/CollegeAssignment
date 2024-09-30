def pat7(n):
    for i in range(n):
       
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        
        
        for j in range(i - 1, -1, -1):
            print(chr(65 + j), end=" ")
        
        
        print()


rows = 4
pat7(rows)

