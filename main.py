from datetime import datetime
import time
import sys


def take_input(name):
    output = int(input(f"Enter the {name} in numerical form or enter -1 to stop: "))
    if output == -1:
        sys.exit()
    return output


start_times = []
end_times = []


def get_dates():
    while True:
        print("----------")
        print("Start date")
        day = take_input("day")
        month = take_input("month")
        year = take_input("year")

        date_time = datetime(year, month, day, 0, 0)

        print(f"unix {time.mktime(date_time.timetuple())}")
        start_times.append(time.mktime(date_time.timetuple()))

        print("----------")
        print("End date")

        day = take_input("day")
        month = take_input("month")
        year = take_input("year")

        date_time = datetime(year, month, day, 0, 0)
        end_times.append(time.mktime(date_time.timetuple()))

        print("---------")
        cont = int(input("Enter 1 to continue adding more dates or 0 to stop: "))
        if cont == 0:
            return


get_dates()

all_times = start_times + end_times
print(all_times)
all_times.sort()
print(all_times)

counter = 0
max_counter = 0
max_counter_date = None

for date in all_times:
    if date in start_times and date in end_times:
        print(1)
        continue
    elif date in start_times:
        print(2)
        counter += 1
    else:
        print(3)
        counter -= 1

    if counter > max_counter:
        max_counter = counter
        max_counter_date = date

print(max_counter)
if max_counter <= 1:
    print("No times could be found that suited everyone!")

else:
    print(f"The date that suits {max_counter} people is "
          f"{datetime.utcfromtimestamp(int(max_counter_date)).strftime('%Y-%m-%d')}")

