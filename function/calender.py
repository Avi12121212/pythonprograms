import calendar
# year= 2022
# month= 4
# print(calendar.month(2022,5))
# check for leap year, find days in a given month and year
#  int daysInMonth(month,year) 1,2022n= 31, 4,2022 = 30, 2,2020 = 29

def leap_yr(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    # return 0


print(leap_yr(2002))
