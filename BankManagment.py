import psycopg2
import random
import string
import os
from dotenv import load_dotenv

from contextlib import contextmanager

# Load environment variables
load_dotenv()

# Database Configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT", "5432")

@contextmanager
def get_db_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        yield conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise e
    finally:
        if conn:
            conn.close()

def init_db():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS accounts (
                        accountNo VARCHAR(20) PRIMARY KEY,
                        name VARCHAR(100),
                        age INT,
                        pin INT,
                        email VARCHAR(100),
                        balance INT
                    );
                """)
                conn.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")

class Bank:
    def __init__(self):
        init_db()

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

            accountNo = Bank.__account_generate()
            email = input("Enter your email: ")
            balance = int(input("Enter initial balance: "))

            try:
                with get_db_connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute("""
                            INSERT INTO accounts (accountNo, name, age, pin, email, balance)
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """, (accountNo, name, age, pin, email, balance))
                        conn.commit()
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
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT balance FROM accounts WHERE accountNo = %s AND pin = %s", (accnumber, pin))
                    result = cur.fetchone()
                    
                    if not result:
                        print("No account found (Check PIN or Account No)")
                    else:
                        current_balance = result[0]
                        try:
                            amount = int(input("Enter amount to deposit: "))
                            if amount < 0 or amount > 100000:
                                print("Invalid amount (Limit: 0-100,000)")
                            else:
                                new_balance = current_balance + amount
                                cur.execute("UPDATE accounts SET balance = %s WHERE accountNo = %s", (new_balance, accnumber))
                                conn.commit()
                                print(f"Success! New Balance: {new_balance}")
                        except ValueError:
                            print("Amount must be a number")
        except Exception as e:
            print(f"Error during deposit: {e}")

    def withdraw_money(self):
        print("\n--- WITHDRAW ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT balance FROM accounts WHERE accountNo = %s AND pin = %s", (accnumber, pin))
                    result = cur.fetchone()

                    if not result:
                        print("No account found")
                    else:
                        current_balance = result[0]
                        try:
                            amount = int(input("Enter amount to withdraw: "))
                            if amount < 0:
                                print("Cannot withdraw negative money")
                            elif amount > current_balance:
                                print(f"Insufficient funds. Current Balance: {current_balance}")
                            else:
                                new_balance = current_balance - amount
                                cur.execute("UPDATE accounts SET balance = %s WHERE accountNo = %s", (new_balance, accnumber))
                                conn.commit()
                                print(f"Success! Remaining Balance: {new_balance}")
                        except ValueError:
                            print("Invalid amount")
        except Exception as e:
            print(f"Error during withdrawal: {e}")

    def show_details(self):
        print("\n--- DETAILS ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT name, email, balance, accountNo FROM accounts WHERE accountNo = %s AND pin = %s", (accnumber, pin))
                    result = cur.fetchone()
                    
                    if not result:
                        print("No account found")
                    else:
                        print(f"\nName: {result[0]}")
                        print(f"Email: {result[1]}")
                        print(f"Balance: {result[2]}")
                        print(f"Account No: {result[3]}")
        except Exception as e:
            print(f"Error getting account details: {e}")

    def update_details(self):
        print("\n--- UPDATE PROFILE ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT name, email, pin FROM accounts WHERE accountNo = %s AND pin = %s", (accnumber, pin))
                    result = cur.fetchone()
                    
                    if not result:
                        print("No account found")
                    else:
                        current_name, current_email, current_pin = result
                        print("Leave blank to keep current value")
                        
                        new_name = input(f"Enter new name ({current_name}): ")
                        if new_name == "":
                            new_name = current_name

                        new_email = input(f"Enter new email ({current_email}): ")
                        if new_email == "":
                            new_email = current_email

                        new_pin = current_pin
                        new_pin_str = input(f"Enter new PIN ({current_pin}): ")
                        if new_pin_str != "":
                            if len(new_pin_str) == 4 and new_pin_str.isdigit():
                                new_pin = int(new_pin_str)
                            else:
                                print("Invalid PIN format. PIN not changed.")

                        cur.execute("""
                            UPDATE accounts 
                            SET name = %s, email = %s, pin = %s 
                            WHERE accountNo = %s
                        """, (new_name, new_email, new_pin, accnumber))
                        conn.commit()
                        print("Details updated successfully!")

        except Exception as e:
            print(f"Error updating details: {e}")

    def delete_account(self):
        print("\n--- DELETE ACCOUNT ---")
        accnumber = input("Enter your account number: ")
        try:
            pin = int(input("Enter your pin: "))
        except ValueError: return

        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM accounts WHERE accountNo = %s AND pin = %s", (accnumber, pin))
                    if not cur.fetchone():
                         print("No account found")
                    else:
                        confirm = input("Are you sure? (yes/no): ")
                        if confirm.lower() == "yes":
                            cur.execute("DELETE FROM accounts WHERE accountNo = %s AND pin = %s", (accnumber, pin))
                            conn.commit()
                            print("Account deleted.")
                        else:
                            print("Operation cancelled")
        except Exception as e:
            print(f"Error deleting account: {e}")

# --- MAIN LOOP ---
if __name__ == "__main__":
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