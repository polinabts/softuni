record_seconds = float (input())
distance_m = float (input())
time_sec_m = float (input())
time_needed = distance_m * time_sec_m

slowing_sectors = distance_m // 15

slowing_time = slowing_sectors * 12.5
time_needed_total = time_needed + slowing_time

if time_needed_total < record_seconds:
    print (f"Yes, he succeeded! The new world record is {time_needed_total:.2f} seconds.")
else:
    time_difference = time_needed_total - record_seconds
    print (f"No, he failed! He was {time_difference:.2f} seconds slower.")