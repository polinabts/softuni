version = input().split(".")
version_as_integer = int("".join(version))
version_as_integer += 1
next_version = [digit for digit in str(version_as_integer)]
print(".".join(next_version))
