#===========>> Set data type  <<=============

# set no duplicate values allowed
# no order is maintain
# set object are mutable
# set is no index value
# set ---> { } 

# set creation:
s = {}        # this is not a empty set - its dictionary
s1 = {10,20,30,40} 
print(s)
print(s1)
print(type(s1))
print('--------------------')

s = {10,20,30,40}
l = list(s)
print(l)
print(type(l))
print('----------------')

l = [10,20,30,40,10,20,30]
s = set(l)
print(s)         # set not allowed to duplicate values
print(type(s))
print('----------------')

# empty set creation :
s = set()
print(s)
print(type(s))
s1 = {}
print(type(s1))
print('----------------')

t = 10,20,30,40,50
s = set(t)
print(s)
print('----------------')

s = set(range(6))
print(s)
print('----------------')
t = tuple()
print(type(t))
print('----------------')

s = {10,20,30}
t = (5,15,25)
l = [2,4,6,8]
s.update(l,t)
print(s)
print('----------------')

s1 = {10,20,30,40}
s1.update(range(4))
print(s1)
print('----------------')

# set copy function:

s = {10,20,30,40}
print(s)
s1 = s.copy()
print(s1)
print('---------------------')

# set pop function:

s = {10,20,30,40,50}
s.pop()
print(s)       #  delete random values because set no index values
print('---------------------')
# set discard function:

s = {100,200,300,400}
s.discard(200)   # discard function delete the perticular values
print(s)
#s.discard(1111)   # dont throw the keyerror
print(s)
print('---------------------')

# remove function:

s = {100,200,300,400,500}
s.remove(400)
print(s)

#s.remove(1111)   # throw key error
print('---------------------')

s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

print(s1.union(s2))
print(s1 | s2)      # union function in set
print('----------------')

print(s1 - s2)       # difference in set
print(s2 - s1) 
print('----------------')
print(s1 & s2)       # insertion in set
print(s2 & s1)
print('----------------')

# frozenset --> immutable set
s = {10,20,30,40,50}
f = frozenset(s)
print(f)
print(type(f))
