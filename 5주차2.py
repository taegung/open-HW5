import operator
onemoon='''
내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다
내가 그의 이름을 불러주었을때,그는 내게로 와 꽃이 되었다
내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오.
그에게로 가서 나도 그의 꽃이 되고싶다
우리들은 모두 무엇이 되고 싶다.
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다.'''

##2019038059 윤태경##
onedic={}
onelist=[]


for ch in onemoon:
    if'ㄱ'<=ch and ch <='힣':
        if ch in onedic:
            onedic[ch]+=1
        else:
            onedic[ch]=1
       
onelist=sorted(onedic.items(),key=lambda x:-x[1])

print('원문\n',onemoon)
print('--------------')
print('문자\t빈도수')
print('--------------')

for i in range(0,len(onelist)):
    print(onelist[i][0],'\t',onelist[i][1])
        

