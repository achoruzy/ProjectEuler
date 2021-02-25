# You are given the following information, but you may prefer to do some research for yourself.

#     1 Jan 1900 was a Monday.
#     Thirty days has September, April, June and November.
#     All the rest have thirty-one,
#     Saving February alone, Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from itertools import chain, cycle


days = ['Monday', 'Thuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
day_cycle = cycle(days)


def next_day():
    return next(day_cycle)


def month_31():
    '''
    For months: Jan, Mar, May, Jul, Aug, Nov, Dec
    '''
    for i in range(1, 32):
        yield i


def month_30():
    '''
    For months: Apr, Jun, Sep, Oct
    '''
    for i in range(1, 31):
        yield i


def month_29():
    '''
    February only in leap years, so if:
    1. year % 4 == 0 and year % 100 != 0 eg. 1900 was not a leap year
    2. year % 400 == 0 eg. 2000 was a leap year
    '''
    for i in range(1, 30):
        yield i


def month_28():
    '''
    For February only in non leap years
    '''
    for i in range(1, 29):
        yield i


def normal_year_days():
    '''
    Days of month in year generator for a leap year
    1. year % 4 == 0 and year % 100 != 0 eg. 1900 was not a leap year
    2. year % 400 == 0 eg. 2000 was a leap year
    '''
    for day in chain(month_31(),  # Jan
                     month_28(),   # Feb
                     month_31(),   # Mar
                     month_30(),   # Apr
                     month_31(),   # May
                     month_30(),   # Jun
                     month_31(),   # Jul
                     month_31(),   # Aug
                     month_30(),   # Sep
                     month_31(),   # Nov
                     month_30(),   # Oct
                     month_31()):   # Dec
        yield day


def leap_year_days():
    '''
    Days of month in year generator for a leap year
    1. year % 4 == 0 and year % 100 != 0 eg. 1900 was not a leap year
    2. year % 400 == 0 eg. 2000 was a leap year
    '''
    for day in chain(month_31(),  # Jan
                     month_29(),   # Feb
                     month_31(),   # Mar
                     month_30(),   # Apr
                     month_31(),   # May
                     month_30(),   # Jun
                     month_31(),   # Jul
                     month_31(),   # Aug
                     month_30(),   # Sep
                     month_31(),   # Nov
                     month_30(),   # Oct
                     month_31()):   # Dec
        yield day


# Help variables
day_num = 0
counter = -2    # as checked, in 1900 were 2 Sundays on 1st


for year in range(1900, 2001):
    print(year)
    # Leap year check
    if year % 4 == 0 and year % 100 != 0:
        day_num_gen = leap_year_days()
    else:
        day_num_gen = normal_year_days()
    # Sunday counter
    for i in day_num_gen:
        day_num = i
        weekday = next_day()
        if weekday == 'Sunday' and i == 1:
            counter += 1

print(counter)
