def loading_bar(some_percent: int) -> str:

    if some_percent == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        percents = int(some_percent / 10)
        dots = 10 - percents
        return f"{some_percent}% [{percents * '%'}{dots * '.'}]\nStill loading..."



number = int(input())
print(loading_bar(number))