# THIS FILE IS ONLY A SANDBOX AS A TESTER FOR MY EXPERIENCES BEFORE PUTTING TO THE PROJ


import os
import json

CWD = os.path.dirname(__file__)

def checkin_save(data):
    with open(f"{CWD}/checkin.json", "w", encoding = "utf8") as file: #  "w" means write, encoding is the accents, 
        json.dump({"Reservation": data}, file, ensure_ascii=False, indent=4) 



with open(f"{CWD}/checkin.json", encoding="utf8") as file:
    checkin = json.load(file)["Reservation"]


# print(checkin)
checkin_list = []

checkin_list.append(checkin)

data = [
    {
            "name": "Nicolas Guzzetti",
            "id": "10101010",
            "roomtype": "Presidential Suite",
            "nights": "3"
        }
        ]

checkin_list.append(data)


roomtypes = {"Room": [
    {
        "Presidential Suite": 200,
        "Standard Room": 100,
        "Single Room": 50,
}
]}


# print(roomtypes["rooms"][0]["Presidential Suite"])
# for i, room_type in roomtypes(enumerate):
#     print(i, room_type)

list = []
list.append(roomtypes)
# print(list)

# for i, room in list(enumerate):
#     print(room)

for i, room in enumerate(roomtypes["Room"][0]):
    i = i + 1
    print(i, room)

# user = input("escoge")
# result = []

# result.append(roomtypes[user])

# print(result) 