table = [[str(i*j) for j in range(1,13)] for i in range(1,13)]

for i in table:
	print(''.join(map(lambda x: x.rjust(4, ' '), i)).strip())
