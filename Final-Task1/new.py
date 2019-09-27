import calcnew as Calculator
import pascal1 as Pascal
import amstrong as Amstrong
def st():
	print "Choice Your Operation : "
	print "1.Calculator"
	print "2.Pascal"
	print "3.Amstrong"
	Choice = int (input("Your Choice (1/2/3): "))
	if Choice == 1:
		Calculator.main()
	elif Choice==2:
		Pascal.main()
	elif Choice==3:
		Amstrong.main()
	else :
		print "Enter the Correct Value"
if __name__ == '__main__':
	st()
