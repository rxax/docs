## Datetime operations

Get a timestamp (good for appending to urls, string record crud dates, etc):

```python
import calendar
import time
gmt = time.gmtime()
ts = calendar.timegm(gmt) #number
ts = str(ts) # string
```

Get the current date and time:

```python
from datetime import datetime
# current time
date = datetime.now()
print(date)
```

Output:

> 2022-01-12 17:20:44.795380
> 

Datetime properties:

```python
date = datetime.now()

print('year', date.year)
print('month', date.month)
print('day', date.day)
print('hour', date.hour)
print('weekday', date.weekday()) # 0 = Monday
print('minute', date.minute)
print('second', date.second)
print('microsecond', date.microsecond)
```

Output:

> year 2022 
> 
> month 1 
> 
> day 12 
> 
> hour 17 
> 
> weekday 2 
> 
> minute 20 
> 
> second 44 
> 
> microsecond 795380

Convert string to datetime:

```python
datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
```

Convert datetime to string:

```python
# Create datetime object
print(datetime_object.strftime('%b %d %Y %I:%M%p'))
```

Output:

> Jun 01 2018 12:00AM

Difference between two dates, as duration:

```python
ts_start=datetime(2020, 12, 1, 3, 9, 45)
ts_end=datetime.now()

ts_diff=ts_end-ts_start
secs=ts_diff.total_seconds()
days,secs=divmod(secs,secs_per_day:=60*60*24)
hrs,secs=divmod(secs,secs_per_hr:=60*60)
mins,secs=divmod(secs,secs_per_min:=60)
secs=round(secs, 2)
answer='Duration={} days, {} hrs, {} mins and {} secs'.format(int(days),int(hrs),int(mins),secs)
print(answer)
```

Output:

> Duration=404 days, 11 hrs, 10 mins and 31.58 secs

Difference between two dates, in years:

```python
from datetime import datetime
from calendar import isleap
start_date = datetime(2005,4,28,12,33)
end_date = datetime(2010,5,5,23,14)
diffyears = end_date.year - start_date.year

# Check leap year
difference = end_date - start_date.replace(end_date.year)
days_in_year = isleap(end_date.year) and 366 or 365
difference_in_years = diffyears + (difference.days + difference.seconds/86400.0)/days_in_year
print(int(difference_in_years), "years")
```

Output:

>  5 years

**References** [Datetime format codes](https://www.w3schools.com/python/python_datetime.asp)
