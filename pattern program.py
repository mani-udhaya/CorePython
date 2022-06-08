# 1.number print given pattern:
row =1
while row<=5:                      
    col =1
    while col<=row:
        print(col,end='')
        col+=1
    print()
    row+=1

print('-----------------------------')
# 2.star print given pattern:
row =5
while row>=1:
    col =1
    while col<=row:
        print('*',end='')
        col+=1
    print()
    row-=1

print('-----------------------------')
# 3.triangle print given pattern:
row =5
while row>=1:
    col =5
    col2=1
    while col2<row:
        print('  ' ,end='')
        col2+=1
    while col>=row:
        print('*',' ',end=' ')
        col-=1
    print()
    row-=1


print('-----------------------------')
# 4.) 
row =5
while row>=1:
    col =1
    while col<=row:
        print(1,end='')
        col+=1
    print()
    row-=1


print('-----------------------------')
# 5.)
row =5
while row>=1:
    col =1
    while col<=row:
        print('*',end='')
        col+=1
    print()
    row-=1

print('-----------------------------')
# 6.)
row =5
value =1
while row>=1:
    col =1
    while col<=row:
        print('-',end='')
        col+=1
    print(value,end='')
    value+=1
    print()
    row-=1
    
print('-----------------------------')
# 7.)
row =5
while row>=1:
    col =1
    while col<=row:
        print('  ' ,end='')
        col+=1
    col2=5
    while col2>=row:
        print(row,end=' ')
        col2-=1
    print()
    row-=1
    
print('-----------------------------')
# 8.)
row =5
while row>=1:
    col =5
    col2=1
    while col2<row:
        print('  ' ,end='')
        col2+=1
    while col>=row:
        print(col,' ',end=' ')
        col-=1
    print()
    row-=1

print('-----------------------------')
# 9.) 
row =5
while row>=1:
    col =5
    col2=1
    while col2<row:
        print('  ' ,end='')
        col2+=1
    while col>=row:
        print(row,' ',end=' ')
        col-=1
    print()
    row-=2
print('-----------------------------')
# 10.)   
row =5
value =1
while row>=1:
    col =1
    while col<=row:
        print('-',end='')
        col+=1
    print(value,end='')
    value+=1
    print()
    row-=1
    
