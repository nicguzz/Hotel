import os
import json
import classes
import config
import pickle


CWD = os.path.dirname(__file__)

# ------------JSON-----------

with open(f"{CWD}/reservation.json", encoding="utf8") as file: #LOAD RESERVATION JSON
    reservation = json.load(file)["Reservation"]

with open(f"{CWD}/checkin.json", encoding="utf8") as file: #LOAD CHECKIN JSON
    checkin = json.load(file)["Reservation"]


try:                                                                #LOAD BILLS.PKL
    with open(f"{CWD}/bills.pkl", "rb") as file_pkl: 
        bill_checkin = pickle.load(file_pkl)
except Exception as e:
    print("No bill dict")
    print(e)
    bill_checkin = {} 


def json_save():
    with open(f"{CWD}/reservation.json", "w", encoding = "utf8") as file: # SAVE RESERVATION JSON
        json.dump({"Reservation": reservation}, file, ensure_ascii=False, indent=4) 

def checkin_save(data):
    
    with open(f"{CWD}/checkin.json", "w", encoding = "utf8") as file: #   SAVE CHECKIN JSON
        json.dump({"Reservation": data}, file, ensure_ascii=False, indent=4) 

def save_bills_pkl(bills_pkl): # SAVE BILLS PKL
    file = open("bills.pkl", "wb")
    pickle.dump(bills_pkl, file)

# ----------------------------

def menu():
    print("-------Welcome to Mini Hotel!-------")
    print("1. New reservation") #here it adds new name, ID, roomtype, nights and it will save in reservation.json 
    print("2. Checkin by ID") # checkin.json list will be for the In house reservations, so I will bring from reservation.json to Checkin list, so the guest will be checked in.
    print("3. In house reservations") #I wish to search inhouse guests by some filters.
    print("4. Bar") # I want to add some bills and consumptions from a Bar, like creating a small menu and add it to the guest bill
    print("5. Checkout") #Here it will be the guest bill which the room nights rate and also the bar bill will be all together, showing what guest needs to pay, after this we will remove the profile from the checkin list.

def inhouse_menu():
    print("1. Search by name")
    print("2. Search by ID")
    print("3.All In House List")

def create_reservation():                   # CREATE RESERVATION

    dictionary = {}
    keys = list(reservation[0].keys())
    count = 1
    for key in keys: # first name, last name, id, roomnights
        if count <= 6:
            if key == 'roomtype':
                for i, room in enumerate(config.roomtypes): 
                    print(f"{i + 1 }. {room}")

                user_index = int(input("Choose room: "))
                result = list(config.roomtypes)[user_index - 1]

                dictionary[key] = result 
                count = count + 1


            elif key == 'nights':
        
                try:
                    night_number = int(input(f"Please insert {key}, maximum of 10 nights: "))
                    if night_number <= 10:
                        dictionary[key] = night_number
                        count = count + 1
                    else:
                        print("Something went wrong, please choose up to 10 nights")
                        count = 0

                except ValueError:
                    print("Please insert number of nights, not strings")
                    

            elif key == 'id':
                user_id = input("Input your ID Nr. : ")
                
                if user_id.strip().isdigit():

                    for i, id in enumerate(reservation):
                        if id["id"] == user_id:
                            print(f"It already exists that ID! Loading {id['name']} profile")
                            dictionary['name'] = id["name"]
                            dictionary['last name'] = id["last name"]
                            print(dictionary)
                            del reservation[i]
                    else:
                        dictionary[key] = user_id.capitalize()

                else:
                    print("Please insert numbers, not strings")
                    break

                count = count + 1

                    
            else:
                try:
                    dictionary[key] = input(f"Please insert {key}: ") #here it adds new title and name
                    int(dictionary[key])
                    print("Please type correctly, not integers allowed")
                    # count = count + 1
                    break
                except Exception:
                    count = count + 1
                

        else:
            print("Something went wrong, going back")
            return


    if count == 6:
        reservation.append(dictionary)
        print("--------------------------")
        print(f" {dictionary['name']} was added to Reservations!")
        json_save()

    else:
        print("Something went wrong, going back")



def reservation_by_id(id_reservation, data):                #SEARCH RESA BY ID
    id_reservation_str = str(id_reservation)
    for resa in data:
        if resa["id"] == id_reservation_str:
        
            print(f"Name : {resa['name']}\nLast name: {resa['last name']}\nID: {resa['id']}\nRoomtype: {resa['roomtype']}\nNights: {resa['nights']}")
            break
    else:
        resa = None
    
    return resa

def guest_by_name(search_term, list, key):                  #SEARCH BY NAME
    result = []
    
    if search_term.strip().isdigit():
        print("Please insert a name correctly.")
    else:
        for guest in list:

            guest_lower = guest[key].lower()
            search_term_lower = search_term.lower()

            if guest_lower.find(search_term_lower) >= 0:      
                
                result.append(guest)

                print(f"Name : {result[0]['name']}\nLast name: {result[0]['last name']}\nID: {result[0]['id']}\nRoomtype: {result[0]['roomtype']}\nNights: {result[0]['nights']}")   
                break
        else:
            print("Name not in the list")


def inhouse_reservations_list(list):                #CHECKIN LIST RESERVATIONS ENUMERATED
    for i, rsv in enumerate(list):
        print(f"[{i + 1}]\nName: {rsv['name']}\nLast name: {rsv['last name']}\nID: {rsv['id']}\nRoomtype: {rsv['roomtype']}\nNights: {rsv['nights']}\n\n")



def bar():              #CHOOSE ID AND ADD SOME BAR CONSUMPTIONS
    inhouse_reservations_list(checkin)
    
    room_bill = int(input("Choose ID: "))

    try:
        billing = bill_checkin[int(room_bill)]
        print("Found")
    except:
        print("Not Found")
        billing = classes.Bill(room_bill)

    print("Bar Menu:")

    count = 1

    while count != "q":
        for i, p in enumerate(config.menu):
            print(i+1, p)



        print("Q. Save and Quit.")
        user_selection = input("Choose: ")       
    

        if user_selection == "q".lower():
            print("Bye")
            count = "q".lower()
        
        else:
            user_selection_int = int(user_selection)
            billing.add_product(config.menu[user_selection_int -1].name, config.menu[user_selection_int -1].price)
            print(billing)
            print(billing.final_bill())
            bill_dict = billing.to_dict()
    
    bill_checkin[int(room_bill)] = billing
    save_bills_pkl(bill_checkin)

def checkout(user_id):                      # TOTALIZE BAR AND ROOMNIGHTS, AND THEN CHECKOUT(REMOVE) FROM CHECKIN LIST

    bar_bill = []
    for room in checkin:
        if int(room["id"]) == user_id:
            nights = room["nights"]
            room_type = room["roomtype"]
    rate = config.roomtypes[room_type]

    try:
        for menu in bill_checkin[user_id].consum_products:

            bar_bill.append(menu.price)
        print(f"-----Checkout-----\nUser: {user_id}\nRoomtype: {room_type}\nNights: {nights}\nRate: {rate} €\nBar: {sum(bar_bill)} €\nTotal rate is: {(rate * nights) + sum(bar_bill)} €")
        
    except KeyError:
        print(f"-----Checkout-----\nUser: {user_id}\nRoomtype: {room_type}\nNights: {nights}\nRate: {rate} €\nTotal rate is: {(rate * nights)} €")
