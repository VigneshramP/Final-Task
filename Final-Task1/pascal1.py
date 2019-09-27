def main():
	Row = int (input("Enter the Number of Rows"))
	list = [1]
	for i in range (Row):
		print list
		newlist=[]
		newlist.append (list [0])
		for i in range(len(list)-1):
			newlist.append(list[i]+list[i+1])
		newlist.append(list[-1])
		list=newlist
if __name__ == '__main__':
	main()