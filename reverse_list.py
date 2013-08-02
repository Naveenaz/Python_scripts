
#Reversing the list in Python


list_1=['n','b','c','d']

#Method 1
list_1.reverse()
print "Method 1:" , list_1

#Method 2

list_1[::-1]
print  "Method 2:" , list_1

list_1=['n','b','c','d']     #Re-defining 

print "Method 3:"
for i in range(len(list_1)-1,-1,-1):    
    print i, list_1[i]
    
print list_1