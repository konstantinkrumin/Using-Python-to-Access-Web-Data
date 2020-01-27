import re

finput = input("Enter the file name: ")
fhand = open(finput, "r")
totalsum = 0

for line in fhand:
	numlist = re.findall('[0-9]+', line)
	if len(numlist) > 0:
		for item in numlist:
			totalsum = totalsum + int(item)
	
print(totalsum)

