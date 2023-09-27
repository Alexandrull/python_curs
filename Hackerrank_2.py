if __name__ == '__main__':

    # Leap years excercise
    # The year can be evenly divided by 4, is a leap year, unless:
    # The year can be evenly divided by 100, it is NOT a leap year, unless:
    # The year is also evenly divisible by 400. Then it is a leap year.

    year = ""

    def is_leap(year):
        leap = False

        if (1900 <= year <= 100000):
            if year % 400 == 0:
                leap = True
            elif year % 100 == 0:
                leap = False
            elif year % 4 == 0:
                leap = True

        return leap

    while year != 0000:
        year = int(input(">"))
        print(is_leap(year))
    else:
        print("CLosing...")
