import re

number_of_lines = int(input())

text = r"^\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#$"

for _ in range(number_of_lines):
    current_line = input()

    match = re.fullmatch(text, current_line)

    if match:
        boss_name = match.group(1)
        title = match.group(2)
        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")