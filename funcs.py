import os
import json

#CWD = os.path.dirname(os.path.abspath(__file__))
CWD = os.path.dirname(__file__)



def menu():
    print("-------Welcome to Mini Hotel!-------")
    print("1. New reservation")
    print("2. Checkin by ID")
    print("3. In house reservations")
    print("4. Bar")
    print("5. Checkout")

roomtypes = {
        "Presidential Suite": 200,
        "Standard Room": 100,
        "Single Room": 50,
}



with open(f"{CWD}/reservation.json", encoding="utf8") as file:
    reservation = json.load(file)["Reservation"]

with open(f"{CWD}/checkin.json", encoding="utf8") as file:
    checkin = json.load(file)["Reservation"]


def json_save():
    with open(f"{CWD}/reservation.json", "w", encoding = "utf8") as file: #  "w" means write, encoding is the accents, 
        json.dump({"Reservation": reservation}, file, ensure_ascii=False, indent=4) 

def checkin_save(data):
    with open(f"{CWD}/checkin.json", "w", encoding = "utf8") as file: #  "w" means write, encoding is the accents, 
        json.dump({"Reservation": data}, file, ensure_ascii=False, indent=4) 

def create_reservation():

    dictionary = {}
    keys = list(reservation[0].keys())
    for key in keys: # title, author
        if key == 'roomtype':
            for i, room in enumerate(roomtypes): 
                print(f"{i + 1 }. {room}")

            user_index = int(input("Choose: "))
            print(roomtypes[user_index - 1])
            # return dictionary[key]
                #WE NEED TO ADD ROOMTYPE THAT USER CHOOSES(1,2,3) TO THE NEW DICTIONARY BEFORE COMPLETING RESA
        else:
            dictionary[key] = input(f"Please insert {key}: ") #here it adds new title and author

        # dictionary[key] = input(f"Please insert {key}: ") #here it adds new title and author
        
    reservation.append(dictionary)
    json_save()


def reservation_by_id(id_reservation, data):
    for resa in data:
        if resa["id"] == id_reservation:
            return resa


def guest_by_name(search_term, list, key):
    result = []
    for guest in list:
        if guest[key].lower().find(search_term.lower()) >= 0:      
            result.append(guest)
    return result

def inhouse_reservations_list(list):
    for rsv in list:
        print(f"\n{rsv}")





# class Reservation:

#     #dictionary = {}

#     def __init__(self, name, id, roomtype, nights):
#     #  id, roomtype, nights, extras):
#         # if type(json_name) != str:
#         #     raise ValueError("The path must be a str")
        
#         # self.json_name = json_name
#         self.name = name
#         self.id = id
#         self.roomtype = roomtype
#         self.nights = nights
#         # self.roomtype = roomtype
#         # self.nights = nights
#         # self. extras = extras
    
#     def create_reservation(name, id, roomtype, nights): #, roomType, nights, extras):
#         #reservation = Reservation(name)
#     #    print(f"reservation: " + name)

#         dicionary = {}

#         for var in ["name", "id"]:
#             dicionary[var] = eval(var)

#             write_json(dicionary, "hotel.json")

#         return dicionary


# def read_json(json_name):
#     with open(f"{CWD}/{json_name}.json", encoding="utf8") as file:
#         return json.load(file)

# def write_json(dict, json_name):

#     with open(f"{CWD}/{json_name}", "w", encoding="utf8") as file:
#         #json.dump(reservation, file, ensure_ascii=False, indent=4)
#         json.dump({f"Reservation": dict}, file, ensure_ascii=False, indent=4)

# user = 0

# while user != "q":
#     funcs.menu()
#     user = input("Choose: ")

#     if user == "1": # Create user
#         print("New reservation")
#         name = input("Name: ")
#         id = input("ID: ")

#         reservation = Reservation.create_reservation(name, id)

#     elif (user != "q"):
#         print("Input not valid")
    
        
# with open(f"{CWD}/{json_file}", "w", encoding="utf8") as file:
#         json.dump(users, file, ensure_ascii=False, indent=4)