# def is_leap(year):
#     leap = False
#
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         return leap
#     else:
#         leap = True
#         return leap
#
#
# year = int(input())
#
# if is_leap(year):
#     print('True')
# else:
#     print('False')
def is_leap(year):
    leap = True

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return leap
    else:
        return False

year = int(input())
print(is_leap(year))