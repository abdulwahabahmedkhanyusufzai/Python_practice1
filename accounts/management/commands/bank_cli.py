from django.core.management.base import BaseCommand
from accounts.models import Account
import random
import string

class Command(BaseCommand):
    help = 'Runs the Bank Management CLI'

    def handle(self, *args, **kwargs):
        self.main_loop()

    def main_loop(self):
        bank = BankController()
        while True:
            print("\n--- BANK MENU (DJANGO) ---")
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
                bank.create_account()
            elif check == 2:
                bank.deposit_money()
            elif check == 3:
                bank.withdraw_money()
            elif check == 4:
                bank.show_details()
            elif check == 5:
                bank.update_details()
            elif check == 6:
                bank.delete_account()
            elif check == 7:
                print("Goodbye!")
                break
            else:
                print("Invalid choice")

class BankController:
    @staticmethod
    def __account_generate():
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

            email = input("Enter your email: ")
            balance = int(input("Enter initial balance: "))
            accountNo = self.__account_generate()

            try:
                Account.objects.create(
                    account_no=accountNo,
                    name=name,
                    age=age,
                    pin=pin,
                    email=email,
                    balance=balance
                )
                print("Account created successfully!")
                print(f"YOUR ACCOUNT NUMBER: {accountNo} (Save this!)")
            except Exception as e:
                print(f"Error creating account: {e}")

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

        try:
            user = Account.objects.get(account_no=accnumber, pin=pin)
            amount = int(input("Enter amount to deposit: "))
            if amount < 0 or amount > 100000:
                print("Invalid amount (Limit: 0-100,000)")
            else:
                user.balance += amount
                user.save()
                print(f"Success! New Balance: {user.balance}")
        except Account.DoesNotExist:
             print("No account found (Check PIN or Account No)")
        except ValueError:
            print("Amount must be a number")

    def withdraw_money(self):
        print("\n--- WITHDRAW ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        try:
            user = Account.objects.get(account_no=accnumber, pin=pin)
            amount = int(input("Enter amount to withdraw: "))
            if amount < 0:
                print("Cannot withdraw negative money")
            elif amount > user.balance:
                print(f"Insufficient funds. Current Balance: {user.balance}")
            else:
                user.balance -= amount
                user.save()
                print(f"Success! Remaining Balance: {user.balance}")
        except Account.DoesNotExist:
             print("No account found (Check PIN or Account No)")
        except ValueError:
            print("Invalid amount")

    def show_details(self):
        print("\n--- DETAILS ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        try:
            user = Account.objects.get(account_no=accnumber, pin=pin)
            print(f"\nName: {user.name}")
            print(f"Email: {user.email}")
            print(f"Balance: {user.balance}")
            print(f"Account No: {user.account_no}")
        except Account.DoesNotExist:
             print("No account found")

    def update_details(self):
        print("\n--- UPDATE PROFILE ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        try:
            user = Account.objects.get(account_no=accnumber, pin=pin)
            print("Leave blank to keep current value")
            
            new_name = input(f"Enter new name ({user.name}): ")
            if new_name != "":
                user.name = new_name

            new_email = input(f"Enter new email ({user.email}): ")
            if new_email != "":
                user.email = new_email

            new_pin_str = input(f"Enter new PIN ({user.pin}): ")
            if new_pin_str != "":
                if len(new_pin_str) == 4 and new_pin_str.isdigit():
                   user.pin = int(new_pin_str)
                else:
                    print("Invalid PIN format. PIN not changed.")
            
            user.save()
            print("Details updated successfully!")
        except Account.DoesNotExist:
             print("No account found")

    def delete_account(self):
        print("\n--- DELETE ACCOUNT ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        try:
            user = Account.objects.get(account_no=accnumber, pin=pin)
            confirm = input("Are you sure? (yes/no): ")
            if confirm.lower() == "yes":
                user.delete()
                print("Account deleted.")
            else:
                print("Operation cancelled")
        except Account.DoesNotExist:
             print("No account found")
