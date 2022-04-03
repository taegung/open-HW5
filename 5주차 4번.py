
import random
import re
##2019038059 윤태경##
data=[]
numbers=[]
i,k=0,0
for i in range(0,5):
    tmp=hex(random.randrange(0,10000))
    data.append(tmp)
print("정렬 전 데이터",end=" ")
print(data)
for k in range(0,len(data)):
    numbers.append(re.sub(r'[^0-9]','',data[k]))

for i in range(0,len(data)-1):
    for k in range(i+1,len(data)):
        if int(numbers[i])>int(numbers[k]):
            tmp=numbers[i]
            numbers[i]=numbers[k]
            numbers[k]=tmp
            dmp=data[i]
            data[i]=data[k]
            data[k]=dmp
            
        
    

print("정렬 후 데이터",end=" ")
print(data)



