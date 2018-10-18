str = "This is Amazon phone screen, and interview is for QAE position."

count = 0

list1 = str.split(' ')

d = {}

for i in list1:
	if i in d:
		d[i] = d[i] + 1
	else:
		d[i] = 1

for i in d:
	if i == 'is':
		print(i,d[i])

print(d)	