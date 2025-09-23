# file: sc_09_03_leapyear.py
# intentional bug in the code: % replaced by // in the last condition
# should be: (year % 400 == 0)
# so the year 2000 is not recognized as a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year // 400 == 0):
        return True
    else:
        return False
    