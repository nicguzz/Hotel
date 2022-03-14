import funcs

user = 0

while user != "q":
    funcs.menu()
    user = input("Choose: ")

    if user == "1": # Create user - make new reservation, goes to reservation.json list
        print("New reservation")
        funcs.create_reservation()

    elif user == "2": # Checkin - here it adds to checkin.json list the reservation

        try:
            reservation_id = int(input("Enter Guest Personal ID: "))
            booking = funcs.reservation_by_id(reservation_id, funcs.reservation)
            if booking != None:
                user = input(f"Proceed with booking which ID is {booking['id']} - Name: {booking['name']}? Y/N :").lower()
                if user == "y":
                    checkin_list = []
                    checkin_list.append(funcs.checkin)
                    checkin_list[0].append(booking)
                    funcs.checkin_save(checkin_list[0])
                    print("Reservation is checked in!")
                elif user == "n":
                    funcs.menu()
                else:
                    print("Please insert either Y/N")
            else:
                print(f"User ID: {reservation_id} was not found in Reservation List, please try again")

        except ValueError:
            print("Please insert a valid ID Number")


    elif user == "3": # Inhouse reservations - < Search checkin list by ID, name and see all list.
        print("-------In House Reservations List-------")
        funcs.inhouse_menu()
        user_option = input("Choose: ")
        if user_option == "1":
            key = "name"
            user_name = input("Search by name: ")
            funcs.guest_by_name(user_name, funcs.checkin, key)
        elif user_option == "2":
            try:
                id_reservation = int(input("Enter Guest Personal ID: "))
                booking2 = funcs.reservation_by_id(id_reservation, funcs.checkin)
                if booking2 == None:
                    print("Reservation not found under such ID Nr. ")

            except ValueError:
                print("Please insert a correct ID Nr. ")
                
        elif user_option == "3":
            funcs.inhouse_reservations_list(funcs.checkin)

    elif user == "4": # Bar - Let user add some bar consumptions to billing account        
        funcs.bar()


    elif user == "5": # Checkout by ID - Gets the total to be paid by ID and after it removes profile from checkin list
        checkout_list = []
        checkout_list.append(funcs.checkin)
        funcs.inhouse_reservations_list(funcs.checkin)
        room_id = input("Choose ID: ")
        try:
            funcs.checkout(int(room_id))
            print("--------")
            booking = funcs.reservation_by_id(room_id, funcs.reservation)
            checkout_question = input(f"Proceed with checkout which ID is {booking['id']} - Name: {booking['name']}? Y/N :").lower()

            if checkout_question == "y":
                checkout_list[0].remove(booking)
                funcs.checkin_save(checkout_list[0])

                print(f"{booking['name']} is checked out successfully!")
            else:
                break

        except KeyError:
            print("Bill not found under such ID Nr. ")
        except Exception:
            print("Please insert a valid nr")

    elif user.lower() == "q": # QUIT
            user = user.lower()
            print("Bye!")