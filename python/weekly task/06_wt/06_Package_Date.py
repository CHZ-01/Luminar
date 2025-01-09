# hw06
import datetime
from date_utils import calculations

today = datetime.datetime.today()
day = int(input("Enter day: "))

print("Days between:",calculations.days_between(today, day))
print("Added days:",calculations.add_days(today, day))