import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    # --- 1. Safe Loading ---
    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                # FIX: json.load reads file objects directly
                data = json.load(fs)
        else:
            print("No database found. Starting fresh.")
    except Exception as err:
        print("Error loading data:", err)
    
    @classmethod
    def __update(cls):
        # FIX: json.dump writes directly. Removed fs.write()
        with open(cls.database, 'w') as fs:
            json.dump(Bank.data, fs, indent=4)

    @classmethod
    def __account_generate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=4)
        spchar = random.choices("!@#$%^&*()_+", k=1)
        
        full_id = alpha + num + spchar
        random.shuffle(full_id)
        return "".join(full_id)
    
    def create_account(self):
        print("\n--- CREATE ACCOUNT ---")
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            
            if age < 18:
                print("Sorry, you must be 18+.")
                return

            pin = int(input("Enter a 4-digit PIN: "))
            if len(str(pin)) != 4:
                print("Invalid PIN (Must be 4 digits)")
                return

            accountNo = Bank.__account_generate()
            email = input("Enter your email: ")
            balance = int(input("Enter initial balance: "))

            user_data = {
                "name": name,
                "age": age,
                "pin": pin,
                "accountNo": accountNo,
                "email": email,
                "balance": balance
            }

            Bank.data.append(user_data)
            Bank.__update()
            print("Account created successfully!")
            print(f"YOUR ACCOUNT NUMBER: {accountNo} (Save this!)")

        except ValueError:
            print("Invalid input! Use numbers for Age/PIN/Balance.")

    def deposit_money(self):
        print("\n--- DEPOSIT ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError:
            print("PIN must be a number")
            return

        # List Comprehension
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        
        # FIX: "if not userdata" handles empty lists correctly
        if not userdata:
            print("No account found (Check PIN or Account No)")
        else:
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount < 0 or amount > 100000:
                    print("Invalid amount (Limit: 0-100,000)")
                else:
                    userdata[0]['balance'] += amount
                    Bank.__update()
                    print(f"Success! New Balance: {userdata[0]['balance']}")
            except ValueError:
                print("Amount must be a number")

    def withdraw_money(self):
        print("\n--- WITHDRAW ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        
        if not userdata:
            print("No account found")
        else:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount < 0:
                    print("Cannot withdraw negative money")
                elif amount > userdata[0]['balance']:
                    print(f"Insufficient funds. Current Balance: {userdata[0]['balance']}")
                else:
                    userdata[0]['balance'] -= amount
                    Bank.__update()
                    print(f"Success! Remaining Balance: {userdata[0]['balance']}")
            except ValueError:
                print("Invalid amount")

    def show_details(self):
        print("\n--- DETAILS ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        
        if not userdata:
            print("No account found")
        else:
            print(f"\nName: {userdata[0]['name']}")
            print(f"Email: {userdata[0]['email']}")
            print(f"Balance: {userdata[0]['balance']}")
            print(f"Account No: {userdata[0]['accountNo']}")

    def update_details(self):
        print("\n--- UPDATE PROFILE ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        
        if not userdata:
            print("No account found")
        else:
            user = userdata[0] # Shortcut variable
            print("Leave blank to keep current value")
            
            new_name = input(f"Enter new name ({user['name']}): ")
            if new_name != "":
                user['name'] = new_name

            new_email = input(f"Enter new email ({user['email']}): ")
            if new_email != "":
                user['email'] = new_email

            # FIX: Handle PIN update carefully
            new_pin_str = input(f"Enter new PIN ({user['pin']}): ")
            if new_pin_str != "":
                if len(new_pin_str) == 4 and new_pin_str.isdigit():
                    user['pin'] = int(new_pin_str)
                else:
                    print("Invalid PIN format. PIN not changed.")

            Bank.__update()
            print("Details updated successfully!")

    def delete_account(self):
        print("\n--- DELETE ACCOUNT ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        
        if not userdata:
            print("No account found")
        else:
            confirm = input("Are you sure? (yes/no): ")
            if confirm.lower() == "yes":
                Bank.data.remove(userdata[0]) # Easier way to delete
                Bank.__update()
                print("Account deleted.")
            else:
                print("Operation cancelled")

# --- MAIN LOOP ---
user = Bank()

while True:
    print("\n--- BANK MENU ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Details")
    print("5. Update Details")
    print("6. Delete Account")
    print("7. Exit")

    try:
        check = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if check == 1:
        user.create_account()
    elif check == 2:
        user.deposit_money()
    elif check == 3:
        user.withdraw_money()
    elif check == 4:
        user.show_details()
    elif check == 5:
        user.update_details()
    elif check == 6:
        user.delete_account()
    elif check == 7:
        print("Goodbye!")
        break
    else:
        print("Invalid choice")