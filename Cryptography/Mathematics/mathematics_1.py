p = 29
list = []
ints = [14,6,11]
for j in range(p):
	x =  j**2%p
	if x in ints:
		list.append(j)
print(min(list))
