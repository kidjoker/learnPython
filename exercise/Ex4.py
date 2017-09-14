def triangle(n):
	listNew = [1]
	i = 1

	if(n > 1):
		listOld = triangle(n-1)
	while(i < n):
		if(n == 2):
			listNew.append(listOld[i-1] + listOld[i-1])
		else:
			listNew.append(listOld[i-1] + listOld[i])
		i = i + 1
	if(n > 1):
		listNew.append(1)
	return listNew

def triangles(m):
	i = 1
	while(i < m):
		yield triangle(i)
		i = i + 1

for n in triangles(10):
	print(n)
