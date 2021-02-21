
a = 'Fa0/2, Fa0/4, Fa0/6, Fa0/26, Fa0/41, Fa0/43'
a = a.split(',')

b = []
c = []
d = []

for index_a in a :
    b.append(index_a.split('/'))
    
for index_b  in b:
                         
    for index_c in index_b:                       
        c.append(index_c) 
        
print(c[1::2])

