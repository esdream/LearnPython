from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2017, 4, 5, 10, 00)
timedstamp_dt = dt.timestamp()  # 创建时间戳
print(timedstamp_dt)

cday = datetime.strptime('2017-5-5 12:23:34', '%Y-%m-%d %H:%M:%S')
print(cday)

def to_timestamp(dt_str, tz_str):
    dt_time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    
