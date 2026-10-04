def days_in_month(month, year):
    days_in_month = [31,28,31,30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = (year % 4 ==0 and year %100!=0) or (year %400 ==0)
    if month == 2 and is_leap:
        return 29
    return days_in_month[month -1]
