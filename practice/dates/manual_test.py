from julian_date import JulianDate
from gregorian_date import GregorianDate
from days_of_week import DaysOfWeek

print (JulianDate(0).to_gregorian().day_of_week())

print(GregorianDate(1987, 6, 24).to_julian())

print(GregorianDate(2012, 1, 1).to_julian())

print(JulianDate(2446971).to_gregorian())

monday = DaysOfWeek.Monday

print(str(monday.name))
