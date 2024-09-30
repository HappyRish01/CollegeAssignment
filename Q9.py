def sums(n):
	s=0
	for i in range(1,n+1):
		s+=(i**i)
	return s
n=int(input("Enter number of term (n) :"))
print("Sum of the series upto n terms =",sums(n))