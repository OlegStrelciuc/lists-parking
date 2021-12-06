def car_brand(brand):
    b = 0
    for i in range(len(p)):
        if p[i] == brand:
            b += 1
    print("",brand,"   -", b)


# parkit lot
p = ["Mercedes", None, "BMW", None, None, "Toyota", "BMW"] # list of None type
# index 0,    1,     2,    3,    4,        5,     6


user_car_brand  = input("Name your brand:?")
user_park_index = int(input("What place:?"))
if p[user_park_index] == None:
    print("Ok, you can park there!!!")
    p[user_park_index] = user_car_brand
else:
    print("This place is occupied!!!")
# free / total
total = len( p )
free = 0
for i in range(len(p)):
    if p[i] == None:
        free+= 1
print("Parking (free/total):", free, "/", total, "places")

for i in range(len(p)):
    print(i, p[i])

car_brand("Mercedes")
car_brand("BMW")
car_brand("Toyota")

