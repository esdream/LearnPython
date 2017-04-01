from datetime import datetime, timedelta, timezone
import re
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2017, 4, 5, 10, 00)
timedstamp_dt = dt.timestamp()  # 创建时间戳
print(timedstamp_dt)

cday = datetime.strptime('2017-5-5 12:23:34', '%Y-%m-%d %H:%M:%S')
print(cday)

def to_timestamp(dt_str, tz_str):
    # str转换成datetime对象
    dt_time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 匹配时区
    utc_dt = re.match(r'^(UTC)([\+\-]\d+):(\d{2})$', tz_str)
    # print(utc.groups())
    # 转换时区
    tz_utc = timezone(timedelta(hours=int(utc_dt.group(2))))
    dt_time = dt_time.replace(tzinfo=tz_utc)
    return dt_time.timestamp()

# 测试
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
