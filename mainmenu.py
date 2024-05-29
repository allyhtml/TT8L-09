import datetime
import pytz 

dt = datetime.datetime.now(tz=pytz.UTC)

for tz in pytz.all_timezones:
    print(tz)
