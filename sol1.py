lt = list(map(str,input().split()))
lt2 = [list[0]]
for i in lt :
	for j in lt2 :
		if i[-1]==j[0]:
			if j not in k :
				k.append(j)
				break
print(lt2)