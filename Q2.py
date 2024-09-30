def greatest_num(a,b,c):
	if a>=b and a>=c:
		return a
	elif b>=a and b>=c:
		return b
	else:
		return c
		
a=int(input("Enter the fisrt number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
greatest=greatest_num(a,b,c)
print("Greatest number out of the entered three numbers is ",greatest)
