import os
import json

#CWD = os.path.dirname(os.path.abspath(__file__))
CWD = os.path.dirname(__file__)



def menu():
    print("-------Welcome to Mini Hotel!-------")
    print("1. New reservation") #here it adds new name, ID, roomtype, nights and it will save in reservation.json 
    print("2. Checkin by ID") # checkin.json list will be for the In house reservations, so I will bring from reservation.json to Checkin list, so the guest will be checked in.
    print("3. In house reservations") #I wish to search inhouse guests by some filters.
    print("4. Bar") # I want to add some bills and consumptions from a Bar, like creating a small menu and add it to the guest bill
    print("5. Checkout") #Here it will be the guest bill which the room nights rate and also the bar bill will be all together, showing what guest needs to pay

def inhouse_menu():
    print("1. Search by name")
    print("2. Search by ID")
    print("3.All In House List")

roomtypes = {
        "Presidential Suite": 200,
        "Standard Room": 100,
        "Single Room": 50,
}



with open(f"{CWD}/reservation.json", encoding="utf8") as file: #LOAD RESERVATION JSON
    reservation = json.load(file)["Reservation"]

with open(f"{CWD}/checkin.json", encoding="utf8") as file: #LOAD CHECKIN JSON
    checkin = json.load(file)["Reservation"]


def json_save():
    with open(f"{CWD}/reservation.json", "w", encoding = "utf8") as file: #  saves in reservation
        json.dump({"Reservation": reservation}, file, ensure_ascii=False, indent=4) 

def checkin_save(data):
    with open(f"{CWD}/checkin.json", "w", encoding = "utf8") as file: #  saves in checkin
        json.dump({"Reservation": data}, file, ensure_ascii=False, indent=4) 

def create_reservation():
    dictionary = {}
    keys = list(reservation[0].keys())
    nights_max = 10
    for key in keys: # title, author
        if key == 'roomtype':
            for i, room in enumerate(roomtypes): 
                print(f"{i + 1 }. {room}")

            user_index = int(input("Choose: "))
            result = list(roomtypes)[user_index - 1]

            dictionary[key] = result 
        elif key == 'nights':
    
            
            number = int(input(f"Please insert {key}, maximum of 10 nights: "))
            if number <= 10:
                dictionary[key] = number
        

            else:
                print("Something went wrong, please choose up to 10 nights")
                nights_max = 11
                
                
        else:
                dictionary[key] = input(f"Please insert {key}: ") #here it adds new title and author
        
            
    if nights_max <= 10:
        reservation.append(dictionary)
        print("--------------------------")
        print(f" {dictionary['name']} was added to Reservations!")

        json_save()
    else:
        print("Something went wrong, going back")



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
