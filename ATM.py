import json
import os

USERS_FILE = "clients.json"


# ===== JSON LOAD & SAVE =====
def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


# ===== USER CLASS =====
class User:
    def __init__(self, name, surname, balance, pin):
        self.name = name
        self.surname = surname
        self.balance = balance
        self.pin = pin


# ===== ATM CLASS =====
class ATM:
    def __init__(self):
        self.users = load_users()
        self.current_user = None

    # ========================
    # LOGIN
    # ========================
    def login(self):
        print("\n=== ანგარიშში შესვლა ===")

        name = input("სახელი: ").strip()
        surname = input("გვარი: ").strip()
        pin = input("PIN კოდი: ").strip()

        for u in self.users:
            if u["name"] == name and u["surname"] == surname and str(u["pin"]) == pin:
                self.current_user = User(u["name"], u["surname"], u["balance"], u["pin"])
                print(f"\n✔ მოგესალმებით, {name} {surname}!")
                self.account_menu()
                return

        print("⚠ ასეთი მომხმარებელი არ არსებობს.")

    # ========================
    # REGISTRATION
    # ========================
    def register(self):
        print("\n=== ახალი ანგარიშის რეგისტრაცია ===")

        name = input("სახელი: ").strip()
        surname = input("გვარი: ").strip()
        pin = input("შემოიყვანეთ PIN (4 ციფრი): ").strip()

        if not pin.isdigit() or len(pin) != 4:
            print("⚠ PIN კოდი უნდა შედგებოდეს 4 ციფრისგან.")
            return

        new_user = {
            "name": name,
            "surname": surname,
            "balance": 0,
            "pin": int(pin)
        }

        self.users.append(new_user)
        save_users(self.users)

        print(f"✔ ახალი მომხმარებელი დარეგისტრირდა: {name} {surname}")

    # ========================
    # DELETE ACCOUNT
    # ========================
    def delete_account(self):
        print("\n=== ანგარიშის წაშლა ===")
        pin_check = input("გთხოვთ შეიყვანოთ PIN კოდი დადასტურებისთვის: ")

        if str(self.current_user.pin) != pin_check:
            print("⚠ PIN კოდი არასწორია. ანგარიშის წაშლა გაუქმებულია.")
            return

        self.users = [
            u for u in self.users
            if not (u["name"] == self.current_user.name and u["surname"] == self.current_user.surname)
        ]

        save_users(self.users)

        print("✔ თქვენი ანგარიში წარმატებით წაიშალა.")
        self.current_user = None

    # ========================
    # ACCOUNT MENU
    # ========================
    def account_menu(self):
        while True:
            print("\n=== ანგარიში ===")
            print(f"👤 მომხმარებელი: {self.current_user.name} {self.current_user.surname}")
            print(f"💰 ბალანსი: {self.current_user.balance} ₾")

            print("\n1. თანხის შეტანა")
            print("2. თანხის გამოტანა")
            print("3. ანგარიშის წაშლა")
            print("4. გასვლა")

            choice = input("➡ ოპერაცია: ")

            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.delete_account()
                return
            elif choice == "4":
                return
            else:
                print("⚠ არასწორი ოპერაცია.")

    # ========================
    # DEPOSIT
    # ========================
    def deposit(self):
        try:
            amount = float(input("შეიყვანეთ თანხა: "))
            if amount <= 0:
                print("⚠ თანხა უნდა იყოს 0-ზე მეტი.")
                return

            self.current_user.balance += amount

            for u in self.users:
                if u["name"] == self.current_user.name and u["surname"] == self.current_user.surname:
                    u["balance"] = self.current_user.balance

            save_users(self.users)
            print("✔ თანხა წარმატებით ჩაირიცხა.")

        except ValueError:
            print("⚠ მრავალნიშნა მონაცემები არასწორია.")

    # ========================
    # WITHDRAW
    # ========================
    def withdraw(self):
        try:
            amount = float(input("გამოსატანი თანხა: "))
            if amount <= 0:
                print("⚠ თანხა უნდა იყოს 0-ზე მეტი.")
                return

            if amount > self.current_user.balance:
                print("⚠ თქვენს ანგარიშზე არ არის საკმარისი თანხა.")
                return

            self.current_user.balance -= amount

            for u in self.users:
                if u["name"] == self.current_user.name and u["surname"] == self.current_user.surname:
                    u["balance"] = self.current_user.balance

            save_users(self.users)
            print("✔ თანხა წარმატებით გაიტანეთ.")

        except ValueError:
            print("⚠ მრავალნიშნა მონაცემები არასწორია.")

    # ========================
    # MAIN MENU
    # ========================
    def start(self):
        while True:
            print("\n=== GEO BANK ===")
            print("1. შესვლა ანგარიშში")
            print("2. ახალი ანგარიშის რეგისტრაცია")
            print("3. გამოსვლა")

            choice = input("➡ ოპერაცია: ")

            if choice == "1":
                self.login()
            elif choice == "2":
                self.register()
            elif choice == "3":
                print("მადლობა GEO BANK-ის გამოყენებისთვის!")
                break
            else:
                print("⚠ არასწორი ოპერაცია.")


# RUN
atm = ATM()
atm.start()
