def rmv(st,i):
	if i==len(st)-1:
		return
	if not st:
		return 
	if st[i]==st[i+1]:
		tmp=st[i]
		while(i<len(st) and st[i]==tmp):
			st.pop(i)
		if not i-1:
			rmv(st,i-1)
		else:
			rmv(st,0)
	else:
		rmv(st,i+1)
		
inp=list("acaaabbbacdddd")
rmv(inp,0)
print ''.join(inp)
