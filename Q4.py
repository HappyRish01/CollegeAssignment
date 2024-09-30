yr=int(input("Enter an year :"))
if yr%100==0:
	century=True
	if yr%400==0:
		leap=True
	else:
		leap=False
else:
		century=False
		if yr%4==0:
			leap=True
		else:
			leap=False
		
if leap:
	print(yr,"is a leap year")
else:
	print(yr,"is not a leap year")
if century:
	print(yr,"is a century")
else:
	print(yr,"is not a century")

