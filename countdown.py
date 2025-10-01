# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science

import time

my_time = int(input("Enter the time in second: "))

for i in reversed(range(0, my_time)): # you can also use the (start:end:step) like (my_time, 0, -1) to reversed the iteration
    second = i % 60
    minutes = int(i /60) % 60
    hours = int(i/3600) # %24 for counting the day as well
    days = int(i/86400) # in days
    print(f"{days:02}:{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)

print("Wake up")