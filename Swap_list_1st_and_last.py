number_list=[12,2,3,65,21]

#Swap function
def swap_list(listParam):
	size=len(listParam)
	
	temp=listParam[0]
	listParam[0] = listParam[size-1]
	listParam[size-1] = temp
	retrun listParam

#call Swap function

print(swap_list(number_list))