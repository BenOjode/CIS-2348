# ZyLab 3.19
# Benjamin Ojode
# 1663352

# Calculating the area of a wall
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))

wall_area = wall_height * wall_width

print('Wall area:', wall_area, 'square feet')

# Calculate paint needed to cover wall area
paint_gallon = 350
paint_amt = wall_area/paint_gallon

print('Paint needed: {:.2f}'.format(paint_amt), 'gallons' )

# Calculate # of gallon cans needed
cans_amt = round(paint_amt)
print('Cans needed:',cans_amt, 'can(s)\n')

# Cost of paint cans depending on color
paint_color = {'red':35,'blue':25,'green':23}

paint_select = str(input('Choose a color to paint the wall:\n'))

if paint_select in paint_color:
    paint_cost = paint_color[paint_select] * cans_amt
    print('Cost of purchasing', paint_select, 'paint: $', end = '')
    print(paint_cost)
else:
    print('Color not found')