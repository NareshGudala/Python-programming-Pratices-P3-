import calendar
# yy = 2025
# mm = 11

yy = int(input("Enter the Year:"))
mm = int(input("Enter the month:"))
dd = int(input("Enetr the Day:"))

# display the calendar
print(calendar.month(yy,mm,dd))