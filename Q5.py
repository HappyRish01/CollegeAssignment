def grade(m1,m2,m3,m4,m5):
	tm=m1+m2+m3+m4+m5
	prcnt=tm/5
	return tm,prcnt
m1=int(input("Enter marks in subject 1(out of 100) :"))
m2=int(input("Enter marks in subject 2(out of 100) :"))
m3=int(input("Enter marks in subject 3(out of 100) :"))
m4=int(input("Enter marks in subject 4(out of 100) :"))
m5=int(input("Enter marks in subject 5(out of 100) :"))
total_marks,percentage=grade(m1,m2,m3,m4,m5)
print("Total marks of the student = ",total_marks)
print("Percentage of the student = ",percentage)
if percentage>=90:
	print("Grade is A+")
elif percentage>=80 and percentage<=89:
	print("Grade is A")
elif percentage>=70 and percentage<=79:
	print("Grade is B+")
elif percentage>=60 and percentage<=69:
	print("Grade is B")
elif percentage>=50 and percentage<=59:
	print("Grade is C")
elif percentage>=40 and percentage<=49:
	print("Grade is D")
else:
	print("Grade is F(Fail)")

	