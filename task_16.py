def month_calendar(start_weekday, days):
    result = []
    row = [" "] * start_weekday
    for day in range(1, days+1):
        row.append(f"{day:2}")
        if len(row) == 7:
            result.append(" ".join(row))
            row = []
        if row:
            result.append(" ".join(row).rstrip())
        return "/n".join(result)
