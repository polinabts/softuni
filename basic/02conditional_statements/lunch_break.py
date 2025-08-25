from math import ceil, floor
# 1.	Име на сериал – текст
# 2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
# 3.	Продължителност на почивката  – цяло число в диапазона [10… 120]
ceries = str (input())
episode_time = float (input())
break_time = float (input())

# Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
lunch_time = break_time * 1/8
rest_time = break_time * 1/4
time_left = break_time - lunch_time - rest_time

# •	Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
# •	Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
# Времето в двете изходни съобщения да се закръгли до най-близкото цяло число нагоре.
if time_left >= episode_time:
    print (f"You have enough time to watch {ceries} and left with {ceil(time_left - episode_time)} minutes free time.")
elif time_left < episode_time:
    print (f"You don't have enough time to watch {ceries}, you need {ceil(episode_time - time_left)} more minutes.")