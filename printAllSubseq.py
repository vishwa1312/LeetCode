def sub(a,i,st,res):
	if st:
		res.add(st)
	if i==len(a):
		return
	
	sub(a,i+1,st,res)
	sub(a,i+1,st+a[i],res)

a="aabc"
res=set()
sub(a,0,"",res)

print res
