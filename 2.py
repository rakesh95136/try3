str = "This is Amazon phone screen, and interview is for QAE position."

count = 0

list1 = str.split(' ')

for i in list1:
	if i == 'is':
		count += 1

print(count)