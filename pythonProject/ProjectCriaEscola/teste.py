from datetime import date, timedelta
from random import choice , randint

current_date = date.today()

print("CURRENT DAY : ", current_date)
n = 6000 + randint(1,5000)
print("OLD Date : ", current_date - timedelta(n))