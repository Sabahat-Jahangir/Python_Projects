# Define the menu
menu = {
    "Pizza": 15,
    "Burger": 10,
    "Fries": 5,
    "Salad": 8,
    "Pasta": 12,
    "Soup": 7,
    "Steak": 25,
    "Sushi": 18,
    "Tacos": 9,
    "Wings": 14,
    "Shrimp": 16,
    "Salmon": 20,
    "Coffee": 4,
    "Tea": 3,
    "Coke": 2
}

print("Welcome to SABGEER RESTURENT :)")
for item in menu.items():
    print(f"{item[0]}: Rs.{item[1]}")
total_price = 0
while True:
    item_name = input("Enter the name name of item you want to order :) ")
    if(item_name in menu ):
        total_price += menu[item_name]
        print(f"{item_name} has been added in your orderlist")
        print("Do you like anything else :) yes/no")
        c = input()
        if(c.lower() == "no"):
            break
    else:
        print(f"Sorry {item_name} is not avaiable in the menu ")

print(f"Your total bill is: Rs.{total_price}")