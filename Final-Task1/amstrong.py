def main():
	Number = number = int (input ("Enter the number whether it is check AMSTRONG or NOT: "))
	Sum = 0 
	while (number>0):
		Reminder = number%10;Sum = Sum + (Reminder**3)
		number = number/10
	if Number==Sum : print "It is AMSTRONG NUMBER"
	else : print "It is NOT AMSTRONG NUMBER"
if __name__ == '__main__':
	main()