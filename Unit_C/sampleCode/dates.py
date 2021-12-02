import datetime

t = datetime.datetime.now()
print("\nThe current time:")
print(t)

ts = 1638447563

t = datetime.datetime.fromtimestamp(ts)
print(f"\nThe timestamp {ts} represents {ts} seconds since 1970-01-01Z00:00:00")
print(t)

t=datetime.datetime.fromtimestamp(0)
print(f"\nThe date corresponding to {ts}")
print(t)
