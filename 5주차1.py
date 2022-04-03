
b=""
a=0
ss=input("문자열을 입력 하세요:")
##2019038059 윤태경##
a=len(ss)


for i in range(0,a):
    if ss[i].isupper()==True:
        b+=ss[i].lower()
    else:
        b+=ss[i].upper()

print("대소문자 변환 결과----->%s"%b)

