# 1.	Рекордът в секунди – реално число;
# 2.	Разстоянието в метри – реално число;
# 3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.
record_seconds = float (input())
distance_m = float (input())
time_sec_m = float (input())
time_needed = distance_m * time_sec_m

# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
slowing_sectors = distance_m // 15
# Когато се изчислява колко пъти Иван ще се забави, в резултат на съпротивлението на водата,
# резултатът трябва да се закръгли надолу до най-близкото цяло число.
slowing_time = slowing_sectors * 12.5
time_needed_total = time_needed + slowing_time

# •	Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
# o	" Yes, he succeeded! The new world record is {времето на Иван} seconds."
# •	Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
# o	"No, he failed! He was {недостигащите секунди} seconds slower."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.
if time_needed_total < record_seconds:
    print (f"Yes, he succeeded! The new world record is {time_needed_total:.2f} seconds.")
else:
    time_difference = time_needed_total - record_seconds
    print (f"No, he failed! He was {time_difference:.2f} seconds slower.")