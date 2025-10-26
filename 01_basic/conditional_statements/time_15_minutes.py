hour = int (input())
minutes = int (input())

minutes_new = minutes + 15

if minutes_new >= 60:
    hour += 1
    minutes_new -= 60

if hour == 24:
    hour = 0

print (f"{hour}:{minutes_new:02d}")

