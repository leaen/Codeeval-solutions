import sys

# Register dictionary with all the currency and values.
register = {'PENNY': .01, 'NICKEL': .05, 'DIME': .10, 'QUARTER': .25, 'HALF DOLLAR': .50, 'ONE': 1.00, 'TWO': 2.00, 'FIVE': 5.00, 'TEN': 10.00, 'TWENTY': 20.00, 'FIFTY': 50.00, 'ONE HUNDRED': 100.00}

def solve(problem):
	cash, pp = problem.split(';')
	pp = float(pp)
	cash = float(cash)

	# Handle edge cases.
	if (cash > pp):
		return 'ERROR'
	elif (cash == pp):
		return 'ZERO'

	change_to_give = pp - cash
	change_given = []

	# Iterate through dictionary from biggest to smallest.
	for currency in sorted(register.items(), key=lambda x: (-x[1], x[0])):
		
		# If currency can fit into the change, give it.
		if currency[1] <= change_to_give:
			change_to_give -= currency[1]
			change_given += (currency[0],)

	# Return string with all the currency given.
	return ','.join(change_given)

with open(sys.argv[1]) as input_file:
	for line in input_file.readlines():
		print(solve(line))
