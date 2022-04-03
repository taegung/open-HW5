q=[]
p=[]
t=[]
nums1=[]
nums2=[]
nums3=[]##2019038059 윤태경##
def two(a):
        if a>=2:
            b=int(a%2)
            nums1.append(b)           
        else:
            nums1.append(a)
            q=list(reversed(nums1))            
            print("".join([str(_) for _ in q]))
            del q[0:]
            del nums1[0:]
            return
         
        c=int(a/2)
        two(c)

def eight(x):
         if x>=8:
             b=int(x%8)
             nums2.append(b)
         else:
             nums2.append(x)
             p=list(reversed(nums2))
             print("".join([str(_) for _ in p]))
             del p[0:]
             del nums2[0:]
             return
         c=int(x/8)
         eight(c)

def tensix(s):
        numdict={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        if s>=16:
             b=int(s%16)
             nums3.append(b)
        else:
             nums3.append(s)
             t=list(reversed(nums3))            
             for i in range(0,len(t)):
                 if t[i] in numdict:
                     t[i]=numdict[t[i]]
                 else:
                     t[i]=str(t[i])
             print("".join([str(_) for _ in t]))           
             return
        c=int(s/16)
        tensix(c)
        
       
num=int(input('10진수 입력-->'))
print("2진수는",end=" ")
two(num)
print("8진수는",end=" ")
eight(num)
print("16진수는",end=" ")
tensix(num)
