import os
import csv
def get_default_path():
    return "password.csv"
def get_file_path():
    choice = input("1. Do you want to specify the file path?\n"
                   "2. Or should we use a default file?\n"
                   "Enter your choice (1 or 2): ")
    while choice not in ('1', '2'):
        choice = input("Invalid input. Please enter 1 or 2: ")
    if choice == '1':
        path = input("Enter full file name (e.g., my_passwords.csv): ").strip()
        if not path.endswith(".csv"):
            path += ".csv"
    else:
        path = get_default_path()
    return path
def write():
    print("\n[Store Password]")
    path = get_file_path()  
    file_exists = os.path.exists(path)  
    with open(path, "a", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        if not file_exists:
            writer.writerow(['Username', 'Site', 'Password'])
        try:
            N = int(input("How many records do you want to add? "))
        except ValueError:
            print("Invalid number.")
            return
        for _ in range(N):
            try:
                username = int(input("Enter customer number (username): "))
            except ValueError:
                print("Username should be a number. Skipping this record.")
                continue

            site = input("Enter site name: ").strip().replace(",", "") 
            password = input("Enter password: ").strip().replace(",", "")
            if not site or not password:
                print("Site and password cannot be empty. Skipping.")
                continue
            writer.writerow([username, site, password])
    print("Passwords saved successfully!")
def read():
    print("\n[View Passwords]")
    path = get_default_path()  
    if not os.path.exists(path):
        print("No password file found. Please add data first.")
        return
    with open(path, 'r') as f:
        reader = csv.reader(f)
        try:
            headers = next(reader) 
        except StopIteration:
            print("File is empty.")
            return
        print("Your saved passwords are:")
        for row in reader:
            if len(row) >= 3:
                print(f"Username: {row[0]}, Site: {row[1]}, Password: {row[2]}")
def search():
    print("\n[Search Password]")
    path = get_default_path()
    if not os.path.exists(path):
        print("No password file found. Please store your data first.")
        return
    print("Search by:\n1. Username\n2. Site\n3. Password")
    choice = input("Enter your choice (1/2/3): ").strip()
    keyword = input("Enter keyword to search: ").strip().lower()
    with open(path, 'r') as f:
        reader = csv.reader(f)
        try:
            next(reader) 
        except StopIteration:
            print("File is empty.")
            return
        results = []
        for row in reader:
            if len(row) < 3:
                continue
            if choice == "1" and keyword in row[0].lower():
                results.append(row)
            elif choice == "2" and keyword in row[1].lower():
                results.append(row)
            elif choice == "3" and keyword in row[2].lower():
                results.append(row)
    if results:
        print("\nSearch Results:")
        for i, res in enumerate(results):
            print(f"{i+1}. Username: {res[0]}, Site: {res[1]}, Password: {res[2]}")
    else:
        print("No matching entries found.")
def update():
    print("\n[Update Password]")
    path = get_default_path()
    if not os.path.exists(path):
        print("No password file found. Please store your data first.")
        return
    keyword = input("Enter the username or site you want to update: ").strip().lower()
    with open(path, 'r') as f:
        rows = list(csv.reader(f)) 
        if not rows:
            print("File is empty.")
            return
        headers = rows[0]  
        data_rows = rows[1:]  
    matches = []
    for i, row in enumerate(data_rows):
        if len(row) < 3:
            continue
        username, site, password = row
        if keyword in username.lower() or keyword in site.lower():
            matches.append((i, row))
    if not matches:
        print("No matching record found to update.")
        return
    print("\nMatching Records:")
    for idx, (i, row) in enumerate(matches):
        print(f"{idx + 1}. Username: {row[0]}, Site: {row[1]}, Password: {row[2]}")
    try:
        choice = int(input("Which record number would you like to update? "))
        if choice < 1 or choice > len(matches):
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        return
    new_password = input("Enter new password: ").strip().replace(",", "")
    if not new_password:
        print("Password cannot be empty.")
        return
    record_index = matches[choice - 1][0]
    data_rows[record_index][2] = new_password
    with open(path, 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
        writer.writerows(data_rows)
    print("Password updated successfully.")
def menu():
    while True:
        print("\n--- Password Manager Menu ---")
        print("1. Store your password")
        print("2. View your passwords")
        print("3. Search a password")
        print("4. Update a password")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == 1:
            write()
        elif choice == 2:
            read()
        elif choice == 3:
            search()
        elif choice == 4:
            update()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
menu()
