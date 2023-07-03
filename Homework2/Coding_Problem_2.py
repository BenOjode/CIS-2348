# Coding Problem 2
# Benjamin Ojode
# 1663352

#Part A
# Dates listed out for parsing
def date_dict(dated):
    months_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
               'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
# Get the date information in the proper format
    year = dated[dated.find(',') + 2:]
    month, day = dated[:dated.find(',')].split(" ")
    month = months_dict[month.title()]
    return '{}/{}/{}'.format(month, day, year)
# Part B: Read date from inputDates text file
with open("inputDates.txt", 'r') as file:
    dates = [date_dict(date) for date in file]
# Part C: Write Dates to parsedDates text file
with open("parsedDates.txt", 'w') as file:
    file.write(''.join(dates))

