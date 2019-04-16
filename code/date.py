import datetime

d=datetime.datetime.today()
today=datetime.datetime.date(datetime.datetime.now())
last_month=(d.replace(day=1) - datetime.timedelta(days=1)).replace(day=d.day)

print(today)
print(last_month)