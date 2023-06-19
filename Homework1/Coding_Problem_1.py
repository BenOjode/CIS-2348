# Coding Problem 1
# Benjamin Ojode
# 1663352
print('Birthday Calculator')
print('Current day')

current_month = int(input("Month: "))
current_day = int(input('Day: '))
current_year = int(input('Year: '))
print('Birthday')
birthday_month = int(input('Month: '))
birthday_day = int(input('Day: '))
birthday_year = int(input('Year: '))

user_age = current_year - birthday_year - 1

if birthday_month < current_month:
    user_age += 1
elif current_month == birthday_month:
    if birthday_day < current_day:
        user_age += 1
if (current_month == birthday_month) and (current_day == birthday_day):
    print('Happy Birthday!')
print('You are', user_age, 'years old.')