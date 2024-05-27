# Vending Machine Program

# Menu of drinks and snacks
menu = {
    "Drinks": {
        "1": {"name": "Karak Chai                     (Spiced tea made with black tea, milk, sugar, and cardamom.)", "price": 1.50},
        "2": {"name": "Jellab                         (Grape molasses, rose water, and sugar)", "price": 9.50},
        "3": {"name": "Qamardeen                      (Apricot-flavored drink made from dried apricot paste)", "price": 5.25},
        "4": {"name": "Laban                          (A fermented milk drink, similar to yogurt)", "price": 4.00}
    },
    "Snacks": {
        "5": {"name": "Falafel Sandwich               (Falafel, hummus, vegetables with pita bread)", "price": 5.50},
        "6": {"name": "Club Sandwich                  (Breast chicken, lettuce, tomato, bacon)", "price": 7.50},
        "7": {"name": "Kunafa                         (semolina dough, Sweet cheese, Sugar syrup, pistachios for garnish)", "price": 2.00},
        "8": {"name": "Baklava                        (Phyllo dough, Chopped nuts, Lemon juice, Honey or sugar syrup)", "price": 3.00}
    }
}

# Function to display menu
def display_menu():
    print("     ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪")
    print("     • Cheering to the Vending Machine! •")
    print("     ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪")
    print("")
    print("                  ──●◎●──")
    print("                   Drinks:")
    print("                  ──●◎●──")
    print("")
    for code, item in menu["Drinks"].items():
        print(f"{code}. {item['name']} - AED {item['price']:.2f}")
    print("                  ──●◎●──")
    print("                   Snacks:")
    print("                  ──●◎●──")
    for code, item in menu["Snacks"].items():
        print(f"{code}. {item['name']} - AED{item['price']:.2f}")
    print("")
    print("        ✦•···········•✦•···········•✦")
    print("")
# Function to get user input
def get_user_input():
    selections = []
    while True:
        code = input("Enter the code of your selection (or 'done' to finish): ")
        if code.lower() == 'done':
            break
        elif code in menu["Drinks"] or code in menu["Snacks"]:
            selections.append(code)
        else:
            print("Invalid code. Please try again.")
    return selections

# Function to manage money
def manage_money(total_price):
    while True:
        money_inserted = float(input("Insert money: AED"))
        if money_inserted >= total_price:
            change = money_inserted - total_price
            return change
        else:
            print("Not enough money. Please insert more.")

# Function to dispense item
def dispense_item(code):
    if code in menu["Drinks"]:
        item_name = menu["Drinks"][code]["name"]
    else:
        item_name = menu["Snacks"][code]["name"]
    print(f"Dispensing {item_name}...")
    print(f"Enjoy your {item_name}!")

# Main program
while True:
    display_menu()
    selections = get_user_input()
    total_price = 0
    for code in selections:
        if code in menu["Drinks"]:
            total_price += menu["Drinks"][code]["price"]
        else:
            total_price += menu["Snacks"][code]["price"]
    print(f"Total price: AED {total_price:.2f}")
    change = manage_money(total_price)
    for code in selections:
        dispense_item(code)
    print(f"Your change is: AED {change:.2f}")
    print("")
    print(" ◇●○◇●○◆○●◇●○◇●○◆○●◇●○◆○●◇◇●○◆○●◇●○◆○●◇")
    print(" 《Thank you for using the vending machine!》")
    print(" ◇●○◇●○◆○●◇●○◇●○◆○●◇●○◆○●◇◇●○◆○●◇●○◆○●◇")