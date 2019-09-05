day = int(input('Day (0-6)? '))
if day >= 1 and day <= 5:
    print('Go to work')
elif day == 0 or 6:
    print('Sleep in')