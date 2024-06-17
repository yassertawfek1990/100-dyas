import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

birthday = dt.datetime(year= 2024, month= 5, day= 26)
birthday_with_hour = dt.datetime(year= 2024, month= 5, day= 26, hour=12,minute=12)

print(year)
print(month)
print(day)
print(day_of_week)
print(birthday)
print(birthday_with_hour)
