import funcs




user = 0

while user != "q":
    funcs.menu()
    user = input("Choose: ")

    if user == "1": # Create user
        print("New reservation")
        funcs.create_reservation()

    elif user == "2": # Checkin
        reservation_id = input("Enter Guest Personal ID: ")
        booking = funcs.reservation_by_id(reservation_id, funcs.reservation)
        if booking != None:
            print(booking)
            user = input(f"Proceed with booking which ID is {booking['id']} - Name: {booking['name']}? Y/N :").lower()
            if user == "y":
                checkin_list = []
                checkin_list.append(funcs.checkin)
                checkin_list.append(booking)
                funcs.checkin_save(checkin_list)
                print("Reservation is checked in!")
            elif user == "n":
                funcs.menu()
            else:
                print("Please insert either Y/N")

    elif user == "3": # Inhouse reservations


        print("-------In House Reservations List-------")
        print(funcs.inhouse_reservations_list(funcs.checkin))


        # elif user == "2": # GET BY AUTHOR
            # key = "name"
            # user_name = input("Name: ").lower()
            # guest_list = funcs.guest_by_name(user_name, funcs.checkin, key)
            # for guest in guest_list:
            #     print(guest)
