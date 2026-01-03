import datetime

dt = datetime.datetime.strptime("2016-04-12T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)

dt2 = datetime.datetime(2016, 4, 12, 12)
print(dt2)