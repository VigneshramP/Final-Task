# Basic Calculator Programming  
# Using Function And Return Value
def Addition(x,y):return x+y	
def Subtraction(x,y):return x-y
def Division(x,y):
	if x>=y:
		return x/y
	else :
		return y/x
def Modulus(x,y):
	if x>=y:
		return x%y
	else :
		return y%x
def Factorial(x):
	if x==1:
		return x
	else:
		return x*Factorial(x-1)
def main():
	# User Input Details 
	print "Choice your Mathematical Operation: "
	print "1.Addition"
	print "2.Subtraction"
	print "3.Division"
	print "4.Modulus"
	print "5.Factorial"

	Choice = int (input("Enter Your Choice : (1/2/3/4/5): "))

	if Choice <6:

		number1=int (input ("Enter First Number :"))
		number2=int (input ("Enter Second Number :"))
		
		if Choice==1:
			print "Addition of Two Numbers is :",Addition(number1,number2)

		elif Choice==2:
			print "Subtraction of Two Numbers is :",Subtraction(number1,number2)

		elif Choice==3:
			print "Division of Two Numbers is :",Division(number1,number2)

		elif Choice==4:
			print "Modulus of Two Numbers is :",Modulus(number1,number2)

		elif Choice ==5:
			print "Factorial of First Number is: ",Factorial(number1)

	else :
		print " "
		print "Choice Correct Option"
		main()
if __name__ == '__main__':
	main()