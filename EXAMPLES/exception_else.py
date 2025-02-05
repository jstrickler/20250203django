numpairs = [(5, 1), (1, 5), (5, 0), (0, 5)]

total = 0

for x, y in numpairs:
    try:
        quotient = x / y
    except ZeroDivisionError as err:
        # 1. log the error and
        #    a. keep going
        #    b. clean up and exit
        print(f"uh-oh, when y = {y}, {err}")
    else:
        total += quotient  # Only if no exceptions were raised
print(total)
