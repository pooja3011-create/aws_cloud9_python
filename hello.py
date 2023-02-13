"""
Your module description
"""
import copy
import csv

"""
myVehicle = {
    "vin" : None,
    "make" : None ,
    "model" : None ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print(f"{key} -> {value}")

myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    for lineCount, row in enumerate(csvReader):
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    print("====================================")
    
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")
"""

"""
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print(f"Here are {copies} copies.")
else:
    print("Thank you, please come again.")
"""

# import random
# number = random.randint(1,10)
# isGuessRight = False
# while isGuessRight != True:
#     guess = input("Guess a number between 1 and 10: ")
#     if int(guess) == number:
#         print("You guessed {}. That is correct! You win!".format(guess))
#         isGuessRight = True
#     else:
#         print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
#         print(f"correct number: {number}")

numbers = ints = [72, 97, 118, 101, 32, 121, 111, 117, 32, 115, 101, 101, 110, 32, 109, 121, 32, 99, 97, 114, 32, 107, 101, 121, 115, 63]
chars = list()
for i in ints:
    char = chr(i)
    chars.append(char)
print("".join(chars))