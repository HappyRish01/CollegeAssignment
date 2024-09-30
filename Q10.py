def series_sum(x, n):
    s_sum = 0.0

    for i in range(1, n + 1):
        term =  (x ** i) / i
        s_sum += term

    return s_sum


x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))
result = series_sum(x, n)
print("The sum of the first",n,"terms of the series =",result)
