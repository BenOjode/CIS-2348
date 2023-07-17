# ZyLabs 11.27
# Benjamin Ojode
# 1663352

roster = {}

for i in range(5):
    jersey_num = int(input("Enter player {}'s jersey number:\n".format(i+1)))
    rating = int(input("Enter player {}'s rating:\n".format(i+1)))
    print()
    roster[jersey_num] = rating

sorted_roster = sorted(roster.items())
print("ROSTER")
for jersey_num, rating in sorted_roster:
    print("Jersey number: {}, Rating: {}".format(jersey_num, rating))

menu = """
MENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit
"""

while True:
    print(menu)
    option = input("Choose an option:\n")
    if option == "o":
        print("\nROSTER")
        for jersey_num, rating in sorted_roster:
            print("Jersey number: {}, Rating: {}".format(jersey_num, rating))
    elif option == "a":
        jersey_num = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        roster[jersey_num] = rating
        sorted_roster = sorted(roster.items())
    elif option == "d":
        jersey_num = int(input("Enter a jersey number:\n"))
        if jersey_num in roster:
            del roster[jersey_num]
            sorted_roster = sorted(roster.items())
    elif option == "u":
        jersey_num = int(input("Enter a jersey number:\n"))
        if jersey_num in roster:
            rating = int(input("Enter a new rating for player:\n"))
            roster[jersey_num] = rating
            sorted_roster = sorted(roster.items())
    elif option == "r":
        rating_limit = int(input("Enter a rating:\n"))
        print("\nABOVE {}".format(rating_limit))
        for jersey_num, rating in sorted_roster:
            if rating > rating_limit:
                print("Jersey number: {}, Rating: {}".format(jersey_num, rating))
    elif option == "q":

        break