import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    return isleap(year)

# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    else:
        return 28

def calculate_age_days(name, age):
    localtime = time.localtime(time.time())
    year = int(age)
    month = year * 12 + localtime.tm_mon
    day = 0

    begin_year = localtime.tm_year - year
    end_year = begin_year + year

    # calculate the days
    for y in range(begin_year, end_year):
        day += 366 if judge_leap_year(y) else 365

    leap_year = judge_leap_year(localtime.tm_year)
    for m in range(1, localtime.tm_mon):
        day += month_days(m, leap_year)

    day += localtime.tm_mday

    print(f"{name}'s age is {year} years or {month} months or {day} days")

if __name__ == "__main__":
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    calculate_age_days(name, age)
