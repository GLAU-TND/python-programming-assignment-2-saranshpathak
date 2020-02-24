num=int(input())
sa=str(bin(num).replace('0b',''))
sa=sa.split('0')
max=0
for item in sa:
	if sa.len(item)>max:
		max = sa.len(item)
print(max)