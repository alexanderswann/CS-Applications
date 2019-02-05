#Alexander Swann
#Monday February, 4, 2019
#CS Applications

#functionsPractice
x = int(input("enter a number "))
y = int(input("enter a number "))
numTickets = int(input("How many tickets "))
isParking = input("True or False ")

def game_cost (numTickets, isParking):
    cost =0
    if isParking == "False":
        cost = numTickets * 500
    else:
        cost = numTickets * 500 + 50
    return cost
total_cost = game_cost(numTickets, isParking)
print(total_cost)
print(isParking)

def house_area (baseLength, roofHeight):
    houseVolume = ((baseLength**2 * roofHeight)/3) + (baseLength**2)
    return houseVolume
total_volume = house_area (x,y)
print (total_volume)
