from pathlib import Path
import sys

def readfileandfolder():
    path = Path(".")
    # Fixed: Check if path exists before iterating
    if not path.exists():
        print("Directory does not exist.")
        return
    
    items = list(path.iterdir()) # Convert to list to avoid exhaustion if needed multiple times
    if not items:
        print("Directory is empty.")
    
    for i, item in enumerate(items):
        print(f"{i}: {item.name} ({'Dir' if item.is_dir() else 'File'})")

def createfile():
    try:
        readfileandfolder()
        name = input("Enter file name: ")
        p = Path(name)
        if p.exists():
            print("File already exists.")
            return
            
        content = input("Enter file content: ")
        with open(p, "w") as fs:
            fs.write(content)
        print(f"File '{name}' created successfully.")
    except Exception as err:
        print(f"Error creating file: {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Enter file name to read: ")
        p = Path(name)
        
        if not p.exists():
            print("File not found.")
            return
            
        if p.is_dir():
             print("Cannot read a directory as a file.")
             return

        with open(p, "r") as fs:
            print("\n--- File Content ---")
            print(fs.read())
            print("--------------------")
    except Exception as err:
        print(f"Error reading file: {err}")

def appendfile():
    try:
        readfileandfolder()
        name = input("Enter file name to append to: ")
        p = Path(name)
        
        if not p.exists():
            print("File not found.")
            return

        content = input("Enter content to append: ")
        with open(p, "a") as fs:
            fs.write("\n" + content)
        print("Content appended successfully.")
    except Exception as err:
        print(f"Error appending to file: {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter file name to delete: ")
        p = Path(name)
        
        if not p.exists():
            print("File not found.")
            return
            
        if p.is_dir():
            print("Use 'Delete Folder' option for directories.")
            return

        p.unlink()
        print(f"File '{name}' deleted successfully.")
    except Exception as err:
        print(f"Error deleting file: {err}")

def create_folder():
    try:
        readfileandfolder()
        name = input("Enter folder name: ")
        p = Path(name)
        p.mkdir(exist_ok=True)
        print(f"Folder '{name}' created/verified.")
    except Exception as err:
        print(f"Error creating folder: {err}")

def delete_folder():
    try:
        readfileandfolder()
        name = input("Enter folder name to delete: ")
        p = Path(name)
        
        if not p.exists():
            print("Folder not found.")
            return
            
        p.rmdir() # Only works on empty directories
        print(f"Folder '{name}' deleted successfully.")
    except OSError:
        print(f"Error: Folder '{name}' is not empty or cannot be deleted.")
    except Exception as err:
        print(f"Error deleting folder: {err}")

def rename_item():
    try:
        readfileandfolder()
        old_name = input("Enter current name: ")
        p = Path(old_name)
        
        if not p.exists():
            print("Item not found.")
            return
            
        new_name = input("Enter new name: ")
        target = Path(new_name)
        
        p.rename(target)
        print(f"Renamed '{old_name}' to '{new_name}'.")
    except Exception as err:
        print(f"Error renaming item: {err}")

def main():
    while True:
        print("\n--- File Handling Menu ---")
        print("1. Create File")
        print("2. Read File")
        print("3. Append File")
        print("4. Delete File")
        print("5. Create Folder")
        print("6. Delete Folder")
        print("7. Rename Item")
        print("8. Exit")
        
        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            createfile()
        elif choice == 2:
            readfile()
        elif choice == 3:
            appendfile()
        elif choice == 4:
            deletefile()
        elif choice == 5:
            create_folder()
        elif choice == 6:
            delete_folder()
        elif choice == 7:
            rename_item()
        elif choice == 8:
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
