import classes


#ROOMTYPES 

roomtypes = {
        "Presidential Suite": 200,
        "Standard Room": 100,
        "Single Room": 50,
}

#BAR MENU

product_1 = classes.BarProduct('Cheeseburger', 10)
product_2 = classes.BarProduct('Beer', 2.5)
product_3 = classes.BarProduct('Water', 1.5)
product_4 = classes.BarProduct('Snacks', 2)
product_5 = classes.BarProduct('Spa massage 1 hour for 1 pax', 45)
product_6 = classes.BarProduct('Spa Massage 30 min for 1 pax', 30)
product_7 = classes.BarProduct('Spa Massage 30 min for 2 pax', 50)

#MENU LIST

menu = []

menu.append(product_1)
menu.append(product_2)
menu.append(product_3)
menu.append(product_4)
menu.append(product_5)
menu.append(product_6)
menu.append(product_7)

