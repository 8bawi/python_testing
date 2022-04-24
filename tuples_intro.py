# t = "a", "b", "c"
# print(t)
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the lightning", "Metallica", 1984
albums=[
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the lightning", "Metallica", 1984),
    ]
print(len(albums))
# More efficient
for name, artist, year in albums:
    # print("Album: {}, Artist: {}, Year: {}"
    # .format(album[0],album[1],album[2]))
    # name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
    .format(name, artist,year))
# Provides Access to the tuple in the loop
for album in albums:
    # print("Album: {}, Artist: {}, Year: {}"
    # .format(album[0],album[1],album[2]))
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
    .format(name, artist,year))
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
# title, artist, year = metallica
# print(title, artist,year)

# table = ("Coffee Table", 200, 100, 75, 34.50)
# print(table[1]*table[2])

# name, length, width, height, price =table
# print(length*width)