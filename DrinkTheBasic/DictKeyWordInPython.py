'''DICTIONARY : Dictionary is similar to hash or maps in other languages'''

#New dictionary declaration
d = dict()

#Add key value pair to dictionary
d['xyz'] = 123
d['abc'] = 345

#printing the whole dictionary
print(d)

#printing the keys and values alone
keys = d.keys()
values = d.values()
print(keys , " : " , values)

#Iteration in dictionary
for i in d:
    print("%s %d" %(i,d[i]))

# check if key exist
print('xyz' in d)

# delete the key-value pair
del d['xyz']

# check again
print("xyz" in d)

#another method of iteration
for index,key in enumerate(d):
    print(index,key,d[key])
#since we already deleted one

