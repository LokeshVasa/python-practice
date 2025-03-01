days=int(input())
total_year=days//365
print(total_year)

rem_days=days-total_year*365
total_weeks=rem_days//7
print(total_weeks)
rem_days=rem_days -total_weeks
print(rem_days)
