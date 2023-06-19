# ZyLab 5.22
# Benjamin Ojode
# 1663352

# Service Menu
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

serv_dict = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}

# Service Selection
service_1 = str(input('Select first service:\n'))
service_2 = str(input('Select second service:\n\n'))

# Invoice for services selected
print("Davy's auto shop invoice\n")

serv_cost = 0
if service_1 in serv_dict:
    print('Service 1: {0}, ${1}'.format(service_1, serv_dict[service_1]))
    serv_cost += serv_dict[service_1]
else:
    print('Service 1: No service')

if service_2 in serv_dict:
    print('Service 2: {0}, ${1}'.format(service_2, serv_dict[service_2]))
    serv_cost += serv_dict[service_2]
else:
    print('Service 2: No service')
print()
print('Total: $', end='')
print(serv_cost)