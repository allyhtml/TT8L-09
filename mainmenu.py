import datetime
import pytz 

dt_mst = datetime.datetime.now(tz=pytz.timezone('MST'))
print(dt_mst.strftime('%B %d, %Y'))
