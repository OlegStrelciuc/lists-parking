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

m = 0
for i in range(len(p)):
    if p[i] == "Mercedes":
        m += 1
print("Mercedes   -", m)


b = 0
for i in range(len(p)):
    if p[i] == "BMW":
        b += 1
print("BMW        -", b)


t = 0
for i in range(len(p)):
    if p[i] == "Toyota":
        t += 1
print("Toyota     -", t)
