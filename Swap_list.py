print("Select type of swap in the list you want")
choice = int(input("1 for swaping last and first element \n 2 for swaping as per position"))


number_list=[12,2,3,65,21]

#Swap function for last and first element 
def swap_list(listParam):
	size=len(listParam)
	
	temp=listParam[0]
	listParam[0] = listParam[size-1]
	listParam[size-1] = temp
	return listParam

#Swap function for last and first element 
def swap_list_pos(listParam, pos1, pos2):
	listParam[pos1], listParam[pos2] = listParam[pos2], listParam[pos1]

	return listParam

#call Swap function
if choice == 1:
	print(swap_list(number_list))
elif choice == 2:
	pos1=int(input("input 1st postion:\n"))
	pos2=int(input("input 2nd postion:\n"))
	print(swap_list_pos(number_list, pos1, pos2))
else:
	print("Unexpected input")