from math import ceil, floor

ceries = str (input())
episode_time = float (input())
break_time = float (input())

lunch_time = break_time * 1/8
rest_time = break_time * 1/4
time_left = break_time - lunch_time - rest_time

if time_left >= episode_time:
    print (f"You have enough time to watch {ceries} and left with {ceil(time_left - episode_time)} minutes free time.")
elif time_left < episode_time:
    print (f"You don't have enough time to watch {ceries}, you need {ceil(episode_time - time_left)} more minutes.")