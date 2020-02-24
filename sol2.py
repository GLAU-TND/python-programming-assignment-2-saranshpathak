from itertools import permutations
lt = list(map(str,input().split()))
b=permutation(lt)
lt2=[]
for i in list(b):
	a=''
	for j in i:
		s=s+j
	list2.append(int(a))
print(max(lt2))