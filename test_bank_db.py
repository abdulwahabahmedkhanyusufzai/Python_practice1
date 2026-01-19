import psycopg2
import sys
from io import StringIO
from unittest.mock import patch
from BankManagment import Bank, DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT

# Setup connection
def get_test_conn():
    return psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT
    )
    
def verify_migration():
    print("1. Testing Database Connection...")
    try:
        with get_test_conn() as conn:
            with conn.cursor() as cur:
                print("   [PASS] Connected to PostgreSQL.")
    except Exception as e:
        print(f"   [FAIL] Could not connect: {e}")
        return

    print("2. Testing Table Creation...")
    try:
        # Bank() init calls init_db()
        bank = Bank()
        with get_test_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT to_regclass('public.accounts');")
                if cur.fetchone()[0]:
                     print("   [PASS] Table 'accounts' exists.")
                else:
                     print("   [FAIL] Table 'accounts' not found.")
                     return
    except Exception as e:
        print(f"   [FAIL] Error initializing Bank: {e}")
        return

    print("3. Testing Create Account (Mocked)...")
    inputs = [
        "Test User", "25", "1234", "test@example.com", "5000"
    ]
    
    with patch('builtins.input', side_effect=inputs):
        try:
            captured_output = StringIO()
            sys.stdout = captured_output
            bank.create_account()
            sys.stdout = sys.__stdout__
            
            with get_test_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM accounts WHERE email = 'test@example.com'")
                    user = cur.fetchone()
                    if user:
                         print(f"   [PASS] User created: {user[1]} (Balance: {user[5]})")
                    else:
                         print("   [FAIL] User not found in DB.")
        except Exception as e:
            sys.stdout = sys.__stdout__
            print(f"   [FAIL] Error creating account: {e}")

    print("4. Testing Deposit (Mocked)...")
    with get_test_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT accountNo FROM accounts WHERE email = 'test@example.com'")
            res = cur.fetchone()
            acc_no = res[0] if res else None

    if not acc_no:
        print("   [FAIL] Could not retrieve account number for deposit test.")
    else:    
        inputs_deposit = [
            acc_no, "1234", "1000"
        ]
        with patch('builtins.input', side_effect=inputs_deposit):
            try:
                captured_output = StringIO()
                sys.stdout = captured_output
                bank.deposit_money()
                sys.stdout = sys.__stdout__
                
                with get_test_conn() as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT balance FROM accounts WHERE accountNo = %s", (acc_no,))
                        new_bal = cur.fetchone()[0]
                        if new_bal == 6000:
                            print(f"   [PASS] Deposit successful. New Balance: {new_bal}")
                        else:
                            print(f"   [FAIL] Balance mismatch. Expected 6000, got {new_bal}")
            except Exception as e:
                 sys.stdout = sys.__stdout__
                 print(f"   [FAIL] Error depositing: {e}")

    # Cleanup
    print("5. Cleaning up test data...")
    with get_test_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM accounts WHERE email = 'test@example.com'")
            conn.commit()
    print("   [PASS] Cleanup done.")

if __name__ == "__main__":
    verify_migration()
