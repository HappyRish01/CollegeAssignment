def sum_and_product_of_digits(a):
    n = abs(a) 
    digit_sum = 0
    digit_product = 1

    if n == 0:  
        digit_product = 0

    while n > 0:
        digit = n % 10  
        digit_sum += digit
        digit_product *= digit
        n //= 10  

    return digit_sum, digit_product


n= int(input("Enter an integer: "))
sum_digits, product_digits = sum_and_product_of_digits(n)
print("Sum of digits of",n,"=",sum_digits)
print(f"Product of digits of",n,"=",product_digits)

