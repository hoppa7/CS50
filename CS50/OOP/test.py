from datetime import datetime
import math
import inflect

p = inflect.engine()
date_format = "%Y-%m-%d"
now = datetime.now()
print(now)
date_obj3 = datetime.strftime(now, date_format)
print(date_obj3)
date = "2025-03-07"
date2 = "1999-03-07"
date_obj = datetime.strptime(date, date_format)
date_obj2 = datetime.strptime(date2, date_format)
print(date_obj)

minutes_diff = round((date_obj - date_obj2).total_seconds() / 60)
print(f"{minutes_diff:,}")

ordinal_word = p.number_to_words(minutes_diff)
print(ordinal_word)

print(now)

midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)

print(midnight)