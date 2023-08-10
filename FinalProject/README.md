Final Project Part 1  
  Design a program that manages the inventory of an electronics store.
  
  Input CSV files include a ManufacturersList, PriceList, and ServicesDatesList

  Required output files include the following CSV files and requirements:
   
   a. FullInventory.csv -- all the items listed by row with all their information. The items
       should be sorted alphabetically by manufacturer. Each row should contain item ID,
       manufacturer name, item type, price, service date, and list if it is damaged. The item
       attributes must appear in this order.
    
   b. Item type Inventory list, i.e LaptopInventory.csv -- there should be a file for each item
       type and the item type needs to be in the file name. Each row of the file should contain
       item ID, manufacturer name, price, service date, and list if it is damaged. The items
       should be sorted by their item ID.
   
  c. PastServiceDateInventory.csv – all the items that are past the service date on the day
       the program is actually executed. Each row should contain: item ID, manufacturer
       name, item type, price, service date, and list if it is damaged. The items must appear in
       the order of service date from oldest to most recent.
   
   d. DamagedInventory.csv –all items that are damaged. Each row should contain : item ID,
       manufacturer name, item type, price, and service date. The items must appear in the
       order of most expensive to least expensive.


Final Project Part 2
  Query the user of an item by asking for manufacturer and item type with a single query.
  
i. Print a message(“No such item in inventory”) if either the manufacturer or the
   item type are not in the inventory, more that one of either type is submitted or
   the combination is not in the inventory. Ignore any other words, so “nice Apple
   computer” is treated the same as “Apple computer”.
   
ii. Print “Your item is:” with the item ID, manufacturer name, item type and price
    on one line. Do not provide items that are past their service date or damaged. If
    there is more than one item, provide the most expensive item.
    
iii. Also print “You may, also, consider:” and print information about the same item
     type from another manufacturer that closes in price to the output item. Only
     print this if the same item from another manufacturer is in the inventory and is
     not damaged nor past its service date.
     
iv.  After output for one query, query the user again. Allow ‘q’ to quit.
