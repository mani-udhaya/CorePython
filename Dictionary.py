# ============>> Dictionary data type <<============

# 1. Dictionary is key and value pair 
# 2. Dictionary key are not allowed to duplicate elements
# 3. Dictionary values are allowed to duplicate elements
# 4. no indexing
# 5. no slicing
# 6. no insertion order maintain
# 7. dictionary are mutuable


# dictionary creation:

d = {}
print(d)
print(type(d))

d[120] = 'abi'
d[121] = 'sanjay'
d[122] = 'jaya'
d[123] = 'kumar'
print(d)
print('---------------------------')

print(d[120])
d[122] = 'ajay'
print(d)

d[100] = 'rahul'
print(d)
# d[1111] = 'ram'    #  throw a key error 
print('---------------------------')

d = {120: 'abi', 121: 'sanjay', 122: 'ajay', 123: 'kumar',100: 'rahul'}
print(d)

# del function:

del(d[100])
print(d)

# clear function:

d.clear()
print(d)
print('--------------------')

#del d  # name error : del d is whole dictionary is delete from the code

# pop function:
d = {120: 'abi', 121: 'sanjay', 122: 'ajay', 123: 'kumar',100: 'rahul'}
# print(d)

d.pop(120)
print(d)

#d.pop(1111)         # key value error

print(len(d))
print(d.get(121))
print(d[121])
print('--------------------')

print(d.get(1111))    # none datatype is output
print(d[1111])     # throw key value error
print('----------------------------')

#  key  functions:

d = {120: 'abi', 121: 'sanjay', 122: 'ajay', 123: 'kumar', 100: 'rahul'}
print(d.keys())
print(type(d.keys()))

for key in d.keys():
    print(key)

print('-------------------------')
# values functions:

print(d.values())
print(type(d.values()))

for name in d.values():
    print(name)

print('-------------------------')

  
# items functions:

d = {120: 'abi', 121: 'sanjay', 122: 'ajay', 123: 'kumar', 100: 'rahul'}

print(d.items())
print(type(d.items()))

for item in d.items():
    print(item)             # all items are tuple format - because tuple is immutable.
print('-------------------------')
# copy function:

d = {120: 'abi', 121: 'sanjay', 122: 'ajay', 123: 'kumar', 100: 'rahul'}
d1 = d.copy()
print(d1)

