#sps=[]
#sps1=[]

#l = [1, 2, 3, 4, 5, 6, 7]
 
#for i in range(0, len(l),3):
    
    #sps1=(l[i:i+3])
    #sps.append(l[i:i+3])
#print(sps)


lst=[[100,'100    01bb.c580.7000         Gi0/1'], [1000,'1000    0a4b.c380.7c00         Gi0/2'], [10,'10    a2ab.c5a0.700e         Gi0/3'], [1001,'1001    a2ab.c5a0.700e         Gi0/3']]

a=[]
for i in lst:
    a.append(i)
    a.sort()
    
    
#print(a)
for ff in a:
    print(ff[1])
    
