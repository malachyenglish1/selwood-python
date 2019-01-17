
####
#Set this up so there's flex whether we output the date as a string or a date
####



from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, FR

#Gets most recent prior weekday
def prev_weekday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() > 4: # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    return adate

d = prev_weekday(date.today())
print(d.strftime('%Y' '%m' '%d'))

#Gets most recent prior weekday
def prev_friday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() != 4: # Fri is 4
        adate -= timedelta(days=1)
    return adate

d = prev_friday(date.today()).strftime('%Y' '%m' '%d')
print(d)

