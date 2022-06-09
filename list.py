#==========>>  list Data type <<==========

# 1. list is one of the python datatype
# 2. list is  objects
# 3. Group of objects in a single entity
# 4. list - insertion order maintain
# 5. list - Duplicate values are allowed
# 6. list - Heterogeneous objects are allowed
# 7. list --> []
# 8. list objects are  mutuable
# 9. list - indexing are allowed (positive & Negative indexing)
# 10.  list is compound data types. 
 
l1 =[]
print(l1)
print(type(l1))

mark = [50,70,90,68,80]
print(mark)

name = "sanjay"
l=len(name)
print(l)


l2 = list(range(5))
print(l2)

s = "Happy New Year"
list3 = s.split()
for i in list3:
    print(i)
    
date = "30-12-2022"
l4 = date.split('-')
for i in l4:
    print(i)
    
marks = [60,70,86,95,77,98]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

# list is mutuable - can change index values:
l5 = [50,100,150,'abcd']
l5[1]= 250         # [50,250,150,'abcd']
print(l5)
print('------------------------------')

l1 = [10,20,30,40,50]
l2 = ['a','b','c']
l3 = (l1+l2)
ll=[l1,l2]
print(l3)
print(type(l3))
print(len(l3))

print(l3[0])
print(l3[1])

print(len(ll[0]))
print(len(ll[1]))

print(ll[0][0])
print(ll[1][0])

for x in ll:
    print(x)
print('------------------------------')

no  = 1
no2 = no+64
print(chr(no2))

no1 = 2
no3 = no1+64
print(chr(no3))


n = 'A5'
num = int(n[1])+65
print(chr(num))
print('------------------------------')

#>> 
l = [10,20,40,50,20,70,20]
count = 0
for x in l:
    if x==20:
        count+=1
print(count)

# list function :

print(l.count(20))
print('------------------------------')

# ----------- >> list append <<------------

l = [10,20,30,50,70]
l.append(100)
print(l)

l.append(500)
print(l)


l1 =[]
for x in range(1,11):
    l1.append(x)
print(l1)


l2 = []
for no in range(1,21):
    if no%2==0:
     l2.append(no)
print(l2) 

l3= []
for i in range(1,11):
    if i%2==0:
        l3.append(i*i)
print(l3)
print('------------------------------')

# ------------>> list insertion <<-----------
l = [10,20,30,40,60,80,90]
l.insert(2,300)
print(l)

l.insert(1000,100)
print(l)

l.insert(-100,-2)
print(l)

l.insert(-80,-5)
print(l)
print('------------------------------')

# -------------- >> reverse function in list <<-------------

# reverse function:
l = [10,20,30,40,50]
l.reverse()
print(l)
print('-----------------')

# reverse function logic:
l = [10,20,30,40,50]
length = len(l)-1 # len(l)=5, len(l)-1 = 4
l2 = []
while length>=0:
    l2.append(l[length])
    length-=1
print(l2)
print('-----------------')

# reverse number:

no = input("Enter a number: ")
i = len(no)-1   # len(no)-1=> 4
reverse =''
while i>=0:
    reverse = reverse+no[i]
    i-=1
print(reverse)
print('-----------------')

# reverse sentence or string:
sen = "hello python"
l = sen.split()
i=len(l)-1
#print(l)
l2=[]
while i>=0:
    l2.append(l[i])
    i-=1
print(l2)
print('-----------------')
    

# reverse string :
sen = "wish you a happy new year"
l = sen.split()
i = len(l)-1
l2 =[]

while i>=0:
    l2.append(l[i])
    i-=2
print(l2)
print('-----------------')

# string convert list:

s = "wish you a happy new year"
l =s.split()
print(l)
print('-----------------')

# complete the sentence:
input = 'Sun Mon Tues Wednes Thurs Fri'
word = input.split()
l2 =[]
#print(word)
for words in word:
    l2.append(words+'day')
#print(l2)
output = ' '.join(l2)
print(output)
print('-----------------')

# list comparing :
a = ['abi']
b = ['abi']
print(a == b) # value is same so a == b True
print(a != b)
print(a is b) # memory address is different so a is b False
print('-----------------')

# list comperhension:
l = [i*i for i in range(1,6)]
print(l)
l = [i**i for i in range(1,6)]
print(l)
print('-----------------')

no1 = [10,20,30,40,50]
no2 = [30,40,50,60,70]

for i in no1:
    if i not in no2:
        print(i)
print('-----------------')       
for i in no1:
    if i in no2:
        print(i)
print('-----------------') 
no3 = [i for i in no1 if i not in no2 ]
print(no3)

