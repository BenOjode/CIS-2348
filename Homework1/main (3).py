# ZyLab 2.20
# Benjamin Ojode
# 1663352

lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
nectar = float(input('Enter amount of agave nectar (in cups):\n'))

servings = float(input('How many servings does this make?\n\n'))

# Lemonade Ingredients Yield
print('Lemonade ingredients - yields {:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(nectar), 'cup(s) agave nectar\n')

# Desired # of servings calculation
desired_servings = int(input('How many servings would you like to make?\n\n'))

#Calculating amt of ingredients needed for one serving
single_cup_lemon = lemon_juice/servings
single_cup_water = water/servings
single_cup_nectar = nectar/servings

#Calculating amt needed to get desired serving
lemon_desired = desired_servings * single_cup_lemon
water_desired = desired_servings * single_cup_water
nectar_desired = desired_servings * single_cup_nectar

# Display ingredients required for desired amt of servings
print('Lemonade ingredients - yields {:.2f}'.format(desired_servings), 'servings')
print('{:.2f}'.format(lemon_desired), 'cup(s) lemon juice')
print('{:.2f}'.format(water_desired), 'cup(s) water')
print('{:.2f}'.format(nectar_desired), 'cup(s) agave nectar\n')

# Ingredients conversion of #(2) from cups - gallons
lemon_gallon = lemon_desired/16
water_gallon = water_desired/16
nectar_gallon = nectar_desired/16

# Display ingredients for gallon conversion
print('Lemonade ingredients - yields {:.2f}'.format(desired_servings), 'servings')
print('{:.2f}'.format(lemon_gallon), 'gallon(s) lemon juice')
print('{:.2f}'.format(water_gallon), 'gallon(s) water')
print('{:.2f}'.format(nectar_gallon), 'gallon(s) agave nectar')
