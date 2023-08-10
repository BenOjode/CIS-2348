# Final Project Part 2
# Benjamin Ojode
# 1663352

import csv
import datetime


def date_change(date: str):
    date1 = [int(i) for i in date.split(sep='/')]

    return [date1[2], date1[0], date1[1]]


# Item Class for storing item information
class Item:

    # Item Parameters declared
    def __init__(self, item_id=0, item_manufacturer='none', item_type='none', item_price=0, item_date='00-00-0000',
                 item_damaged=''):
        self.id = item_id
        self.manufacturer = item_manufacturer
        self.type = item_type
        self.price = item_price
        self.date = item_date
        self.damaged = item_damaged

    def __str__(self):
        return f'{self.id}, {self.manufacturer}, {self.type}, {self.price}, {self.date}, {self.damaged}'


# Inventory class for storing data
class Inventory:

    def __init__(self):
        self.items = []

    # Inventory for FullInventory
    def fullinventory(self):
        # Sort inventory by manufacturer
        def sort(i_sort: Item):
            return i_sort.manufacturer

        manufacturer_sorted_items = sorted(self.items, key=sort)

        # Write data to fullinventory.csv
        with open('FullInventory.csv', 'w', newline='') as fullinventory_update:
            fullinventory_write = csv.writer(fullinventory_update)

            for manufacturer_item in manufacturer_sorted_items:
                fullinventory_write.writerow((manufacturer_item.id, manufacturer_item.manufacturer,
                                             manufacturer_item.type, manufacturer_item.price, manufacturer_item.date,
                                             manufacturer_item.damaged))

    # Inventory for LaptopInventory
    def inventorytype(self):
        inventory_types = []
        for i in self.items:
            if i.type not in inventory_types:
                inventory_types.append(i.type)

        # Sort inventory by ID
        def sort(id_sort: Item):
            return id_sort.id
        id_sorted_items = sorted(self.items, key=sort)

        # Write each type into LaptopInventory.csv
        for typer in inventory_types:
            # Uses file name with the Type and ending 'Inventory.csv'
            with open(f'{typer.capitalize()}Inventory.csv', 'w', newline='') as inv_type:
                writeto_inv = csv.writer(inv_type)

                for i_item in id_sorted_items:
                    if i_item.type == typer:
                        writeto_inv.writerow((i_item.id, i_item.manufacturer, i_item.price,
                                              i_item.date, i_item.damaged))

    # Inventory for PastServiceDateInventory
    def pastsdinventory(self):
        # Retrieve the current date
        current_date = [datetime.date.today().year, datetime.date.today().month, datetime.date.today().day]

        # Sort inventory by dates
        def sort(date_sort: Item):
            return date_change(date_sort.date)

        date_sorted_items = sorted(self.items, key=sort)

        # Write data to PastServiceDateInventory.csv
        with open('PastServiceDateInventory.csv', 'w', newline='') as past_sd_inv:
            writeto_past = csv.writer(past_sd_inv)
            for item_date in date_sorted_items:
                # Check to see if the date is past the due date
                if date_change(item_date.date) < current_date:
                    writeto_past.writerow((item_date.id, item_date.manufacturer, item_date.type,
                                           item_date.price, item_date.date, item_date.damaged))

    # Inventory for DamagedInventory
    def damagedinventory(self):
        # Have inventory items pre-sorted by price
        def sort(damaged_inv_sort: Item):
            return damaged_inv_sort.price
        # Change the sort list order from high to low
        sorted_inv_price = sorted(self.items, key=sort, reverse=True)

        # Write to DamagedInventory.csv
        with open('DamagedInventory.csv', 'w', newline='') as damaged_inv:
            writeto_damaged = csv.writer(damaged_inv)
            # Damaged items will be written to the file
            for item_price in sorted_inv_price:
                if item_price.damaged == 'damaged':
                    writeto_damaged.writerow((item_price.id, item_price.manufacturer, item_price.type,
                                              item_price.price, item_price.date))

    # View inventory data
    def view_inv(self):
        for item in self.items:
            print(item)
        print()

# Interactive Inventory Query
def inventory_query(inv: Inventory):
    current_date = [datetime.date.today().year, datetime.date.today().month, datetime.date.today().day]

    # List for all item types
    item_types = []
    for multitems in inv.items:
        if multitems.type not in item_types:
            item_types.append(multitems.type)

    # List for all manufacturers
    manufacturers = []
    for manufacs in inv.items:
        if manufacs.manufacturer.strip() not in manufacturers:
            manufacturers.append(manufacs.manufacturer.strip())

    # Retrieve User Input, searching with query selection and counting type and manufacturer
    user_query = input('Enter a manufacturer and an item type \nType q to quit')
    while user_query.lower != 'q':
        query_search = user_query.split()
        type_num = 0

        for query_type in query_search:
            if query_type in item_types:
                type_num += 1
        manufac_num = 0

        for manufac_query in query_search:
            if manufac_query in manufacturers:
                manufac_num += 1

        if (type_num == 1) and (manufac_num == 1):

            # Look for query in inventory indicating whether damaged or outdated items
            type_item = []
            item_wanted = []
            for item_query in inv.items:
                if item_query.type in query_search:
                    if item_query.id not in [i.id for i in type_item]:
                        if item_query.damaged != 'damaged':
                            if date_change(item_query.date) > current_date:
                                type_item.append(item_query)

            # Check if item matches query type
            if type_item:
                for item_query in type_item:
                    if item_query.manufacturer.strip() in query_search:
                        item_wanted.append(item_query)

                # Retrieves the priciest item
                if item_wanted:
                    wanted_item = item_wanted[0]
                    for pricey_item in item_wanted:
                        if pricey_item.price > wanted_item.price:
                            wanted_item = pricey_item

                    print(f'\nYour item is: {wanted_item.id},{wanted_item.manufacturer},'
                          f'{wanted_item.type},{wanted_item.price}')

                    # Take out wanted items
                    for eliminate_item in item_wanted:
                        type_item.remove(eliminate_item)

                    # Check for any other items
                    if type_item:
                        other_item = type_item[0]

                        # Retrieve similar items to the wanted item
                        for type_items in type_item:
                            item_sim = abs(wanted_item.price - other_item.price)
                            item_type_sim = abs(wanted_item.price - type_items.price)

                            if item_type_sim < item_sim:
                                other_item = type_items

                        print(f'You may also consider: {other_item.id},{other_item.manufacturer},'
                              f'{other_item.type},{other_item.price}')

                else:
                    print('\nNo such item in inventory')
            else:
                print('\nNo such item in inventory')
        else:
            print('\nNo such item in inventory')

        item_query = input('\nEnter a manufacturer and an item type:')


inv = Inventory()

with open('ManufacturerList.csv', 'r') as mf_list:
    mf_list_read = csv.reader(mf_list)

    for row in mf_list_read:
        inv.items.append(Item(int(row[0]), row[1], row[2], item_damaged=row[3]))

# Read the Price List
with open('PriceList.csv', 'r') as pl:
    price_list = csv.reader(pl)

    for row in price_list:
        # Item search by ID
        for select_item in inv.items:
            if int(row[0]) == select_item.id:
                select_item.price = int(row[1])
                break

# Read the Service Dates List
with open('ServiceDatesList.csv', 'r') as sdl:
    service_dl = csv.reader(sdl)

    for row in service_dl:
        for select_item in inv.items:
            if int(row[0]) == select_item.id:
                select_item.date = row[1]
                break

inv.fullinventory()
inv.inventorytype()
inv.pastsdinventory()
inv.damagedinventory()

inventory_query(inv)
