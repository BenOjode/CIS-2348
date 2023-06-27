# ZyLab 6.17
# Benjamin Ojode
# 1663352

password = input()
edited_pass = ''

# Code to iterate through the password, changing the appropriate characters
for i in password:
    if i == 'i':
        edited_pass += '!'
    elif i == 'a':
        edited_pass += '@'
    elif i == 'm':
        edited_pass += 'M'
    elif i == 'B':
        edited_pass += '8'
    elif i == 'o':
        edited_pass += '.'
    else:
        edited_pass += i
edited_pass += 'q*s'
print(edited_pass)
