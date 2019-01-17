
####
# Outputs the requested date as a datetime.date
####



from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, FR

# gets most recent prior weekday
def prev_weekday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() > 4: # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    adate -= timedelta(days=1)
    return adate

# gets most recent prior Friday
def prev_friday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() != 4: # Fri is 4
        adate -= timedelta(days=1)
    return adate
