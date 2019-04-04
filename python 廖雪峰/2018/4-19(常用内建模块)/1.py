from datetime import datetime
now = datetime.now() # 获取当前datetime
print(now)
print(type(now))
#获得指定时间的日期
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
#timestamp和datatime互相转换
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
dt = dt.timestamp() # 把datetime转换为timestamp
print(dt)
t = 1429417200.0
print(datetime.fromtimestamp(t))
#str和datetime互相转换
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
#timestamp也可以直接被转换到UTC标准时区的时间：
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间
#datetime加减
from datetime import datetime, timedelta
now = datetime.now()
print(now)
now = now + timedelta(hours=10)
print(now)
now = now - timedelta(days=1)
print(now)
now = now + timedelta(days=2, hours=12)
print(now)
#本地时间转换为UTC时间
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)
#时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
	#str转化datetime
	dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
	#获取时区
	dtutc=int(re.match('UTC([\+\-]\d{1,2}):\d{2}',tz_str).group(1))
	#创建时区
	utctime=timezone(timedelta(hours=dtutc))
	#强制设置时区
	utcdt=dt.replace(tzinfo=utctime)
	#datetime转换为timestamp
	ts=utcdt.timestamp()
	return ts
d='2015-1-21 9:01:30'
t='UTC+5:00'
print(to_timestamp(d,t))
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')