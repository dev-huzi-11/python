import time

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# Getting current time
local_time = time.localtime()
print(local_time)

# Getting the Formatted Time
format_time = time.asctime(time.localtime(time.time()))
print(format_time)

import calendar

# Getting calendar
cal = calendar.month(2025, 4)
print(cal)