def triangle_type(a,b,c):
	if a==b and b==c:
		return "Equilateral"
	elif a==b and b!=c:
		return "Isosceles"
	else:
		return "Scalene"

a=float(input("Enter the length of side A in cm :"))
b=float(input("Enter the length of side B in cm :"))
c=float(input("Enter the length of side C in cm :"))
typ=triangle_type(a,b,c)
print("The triangle is",typ,"triangle")
