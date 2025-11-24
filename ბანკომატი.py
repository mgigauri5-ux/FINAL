print("ფინალური დავალება 3")

# 3.5 ბანკომატი 

import os

BALANCE_FILE = "balance.txt"

# ბალანსის ჩატვირთვა ფაილიდან

def load_balance():
    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "w") as file:
            file.write("0")
        return 0
    with open(BALANCE_FILE, "r") as file:
        return float(file.read())
    
    # ბალანსის შენახვა ფაილში

def save_balance(balance):
    with open(BALANCE_FILE, "w") as file:
        file.write(str(balance))

# ბალანსის შემოწმება
def check_balance(balance):
    print(f"თქვენი ბალანსია: {balance} ლარი")

# თანხის შეტანა
def deposit(balance):
    amount = float(input("შეიყვანეთ შეტანის თანხა: "))
    if amount <= 0:
        print(" თანხა უნდა იყოს დადებითი!")
        return balance
    balance += amount
    print(f" წარმატებით შეიტანეთ {amount} ლარი")
    return balance

# თანხის გატანა
def withdraw(balance):
    amount = float(input("შეიყვანეთ გასატანი თანხა: "))
    if amount <= 0:
        print(" თანხა უნდა იყოს ნულზე მეტი!")
        return balance
    if amount > balance:
        print(" ბალანსი არ არის საკმარისი!")
        return balance
    balance -= amount
    print(f" წარმატებით გამოიტანეთ {amount} ლარი")
    return balance

# მთავარი მენიუ
def atm():
    balance = load_balance()
# თუ სრულდება ყველა პირობა

    while True:
        print("\n--- ბანკომატი ---")
        print("1. ბალანსის ნახვა")
        print("2. თანხის შეტანა")
        print("3. თანხის გატანა")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ ოპერაცია ციფრი უნდა იყოს (1-4): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)
            save_balance(balance)

        elif choice == "3":
            balance = withdraw(balance)
            save_balance(balance)

        elif choice == "4":
            print("გმადლობთ ბანკომატის გამოყენებისთვის!")
            break

        else:
            print(" არასწორი ტრანზაქცია! სცადეთ თავიდან.")

# პროგრამის გაშვება
atm()    

