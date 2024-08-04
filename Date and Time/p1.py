import datetime

gvr = datetime.date(1956,1,31)

print(gvr.year,gvr.month,gvr.day)

mill=datetime.date(2000,1,1)

dt=datetime.timedelta(100)

print(mill+dt)

#Day-name ,month name day number,year
#Case Sensitive

print(gvr.strftime('%A ,%B %d, %Y'))

message = "GVR was born on {:%A,%B %d,%Y}"
print(message.format(gvr))

#Today's date
now = datetime.datetime.today()
print(now)
print(now.microsecond)
print(now.second)

#MavenTech / TCS: What is strptime()?

moon_landing="7/20/1969"
moon_landing_datetime=datetime.datetime.strptime(moon_landing,"%m/%d/%Y")
print(type(moon_landing_datetime))
print(moon_landing_datetime)


