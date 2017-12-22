from datetime import datetime, timedelta, timezone
dt = datetime.strptime('2015-1-21 9:01:30', '%Y-%m-%d %H:%M:%S')
utc_dt = dt.replace(tzinfo=timezone.utc)
t_dt = utc_dt.astimezone(timezone(timedelta(hours=5)))
t_dt.timestamp() # 把datetime转换为timestamp
print(t_dt.timestamp())