import time
import re
from datetime import datetime
def today():
    return time.strftime('%Y/%m/%d', time.localtime(time.time()))

##2019038059 윤태경##


ss=input('시작날짜 (연/월/일)입력==>')  
a=re.sub('/','',ss)
now = datetime.now()
past = datetime.strptime(a, "%Y%m%d")
diff =  now - past
print(ss,"부터 오늘",today(),"까지는",diff.days,"일이 지났습니다")
date=today().replace('/','-')
datetime_date=datetime.strptime(date,'%Y-%m-%d')
datedict={0:'월요일',1:'화요일',2:'수요일',3:'목요일',4:'금요일',5:'토요일',6:'일요일'}
datedict[datetime_date.weekday()]
print('그리고 오늘은 ',datedict[datetime_date.weekday()],'입니다')




