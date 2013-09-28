from datetime import datetime
from datetime import timedelta
import calendar

today = datetime.today()
start = datetime(today.date().year, today.date().month, 1)
end = start + timedelta(calendar.monthrange(today.date().year, today.date().month)[1])

print "start: " + str(start)
print "end: " + str(end)
