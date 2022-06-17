# Tuple functions: 
	tuple describe - () -round bracket
# basic tuple operation: 

t  = (10,20,30,40)
print(t[::2])
print(t[-1])
print(t[0])
print(t[2:5])
print('--------------')

t1 = (10,20,30,40,50)
t2 = (5,10,15)
t3 = t1+t2
print(t3)
print('--------------')

t4 = t1*2
print(t4)
print('--------------')

t5 = sorted(t3)
t6 = sorted(t3,reverse=True)
print(t5)
print(t6)
print('--------------')

print(len(t3))
print(t3.count(10))
print(t3.index(10))
print('--------------')

print(min(t5))
print(max(t5))
print(sum(t5))
print('--------------')

# tuple packing / unpacking:

a,b,c,d = 10,20,30,40
t = a,b,c,d       # packing
print(t)

p,q,r,s = t       # un packing
print(t)
print('--------------')
