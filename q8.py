l1=[1,2,3,4,5]
l2=["a","b","c","d","e"]

d={l1[i]:l2[i] for i in range(len(l1))}
print(d)