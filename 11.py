def sumofseries(n):
    s = 0
    for i in range(1, n + 1):
        term = (-1) ** (i + 1) * i 
        s += term
    return s 

n = int(input("Enter number of terms (n): "))
print("Sum of the series =", sumofseries(n))

