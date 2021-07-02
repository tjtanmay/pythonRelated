calculation_to_units = 24
name_of_unit = "hours"

#Where magic happens
def days_to_units(num_of_days):
	if num_of_days > 0:
		return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
	else:
		return "You have enterd a negative value!"

#user input and converting to int
days=int(input("enter num of days:\n"))

output_Message= days_to_units(days)
print(output_Message)