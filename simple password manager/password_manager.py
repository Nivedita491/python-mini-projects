import os
import csv
def get_user_file_path():
    def validate_directory(path):
        if not os.path.exists(os.path.dirname(path)):
            print(f"Error: Directory '{os.path.dirname(path)}' doesn't exist")
            return False
        return True
    def ensure_csv_extension(path):
        """Helper: Ensure path ends with .csv"""
        if not path.strip().lower().endswith('.csv'):
            new_path = os.path.splitext(path)[0] + '.csv'
            print(f"Note: File extension changed to .csv ({new_path})")
            return new_path
        return path
    def handle_missing_file(path):
        print(f"\nFile '{path}' not found.")
        use_default = input("Would you like to use default (passwords.csv) instead? (y/n): ").lower()
        if use_default == 'y':
            default_path = 'passwords.csv'
            if not os.path.exists(default_path):
                with open(default_path, 'w', newline='') as f:
                    csv.writer(f).writerow(['Username','Site','Password'])
                print(f"Created new default file: {default_path}")
            return default_path
        return None
    while True:
        print("\n[1] Use default existing file(passwords.csv)\n[2] Specify custom path")
        choice = input("Choice (1/2): ").strip()
        if choice == '1':
            if not os.path.exists('passwords.csv'):
                with open('passwords.csv', 'w', newline='') as f:
                    csv.writer(f).writerow(['Username','Site','Password'])
                print("Created new default passwords.csv")
            print("Using default passwords.csv")
            return 'passwords.csv'
        elif choice == '2':
            path = input("Full file path: ").strip()
            if not path:
                print("Path cannot be empty")  
                continue
            path = ensure_csv_extension(path)
            if not validate_directory(path):
                continue    
            if os.path.exists(path):
                print(f"File found: {path}")
                return path
            result = handle_missing_file(path)
            if result: return result
            print("Please try another path.")
        else:
            print("Invalid choice")
def write_password(file_path):
    print("\n--- Add New Password ---") 
    def validate_input(prompt, field_type):
        while True:
            value = input(f"{prompt}: ").strip()
            if not value:
                print(f"Error: {field_type} cannot be empty")
                continue
            if ',' in value:
                print("Warning: Commas will be automatically removed")
                value = value.replace(',', '')
           
            return value
    username = validate_input("Username", "Username")
    site = validate_input("Website/Service", "Site name")
    password = validate_input("Password", "Password")
    try:
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, site, password])
        print("\nPassword successfully saved!")
        
    except PermissionError:
        print("Error: Cannot write to file (permission denied)")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
def view_passwords(file_path):
    print("\n--- displaying your stored Passwords ---")
    def display_as_table(data):
        if not data:
            print("No passwords stored yet")
            return
        max_user = max(len(str(row[0])) for row in data)
        max_site = max(len(str(row[1])) for row in data)
        max_pass = max(len(str(row[2])) for row in data)
        max_user = max(max_user, 8)   
        max_site = max(max_site, 4)   
        max_pass = max(max_pass, 8) 
        header = (f"{'Username'.ljust(max_user)} | " 
                 f"{'Site'.ljust(max_site)} | "
                 f"{'Password'.ljust(max_pass)}")
        print("\n" + header)
        print("-" * len(header))
        for row in data:
            print(f"{row[0].ljust(max_user)} | "
                  f"{row[1].ljust(max_site)} | "
                  f"{row[2].ljust(max_pass)}")
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            try:
                if csv.Sniffer().has_header(csvfile.read(1024)):
                    csvfile.seek(0)
                    next(reader)
                csvfile.seek(0)
            except:
                pass
            passwords = list(reader)
            if not passwords:
                print("No passwords stored yet")
                return
            valid_passwords = []
            for row in passwords:
                if len(row) >= 3 and all(field.strip() for field in row[:3]):
                    valid_passwords.append(row[:3])
            display_as_table(valid_passwords)
            print(f"\nTotal passwords: {len(valid_passwords)}")
    except FileNotFoundError:
        print("Error: Password file not found (it may have been deleted)")
    except Exception as e:
        print(f"Error reading file: {str(e)}")
def search_passwords(file_path):
    print("\n--- Search Passwords ---")   
    def get_search_term():
        while True:
            term = input("Enter search term (e.g., username:admin, site:google): ").strip()
            if not term:
                print("Error: Search term cannot be empty")
                continue
            return term.lower() 
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            try:
                if csv.Sniffer().has_header(csvfile.read(1024)):
                    csvfile.seek(0)
                    next(reader)
                csvfile.seek(0)
            except:
                pass       
            passwords = [row[:3] for row in reader if len(row) >= 3 and all(field.strip() for field in row[:3])] 
            if not passwords:
                print("\nNo passwords found to search")
                return
            print("\nSearch will look through usernames, sites, and passwords")
            search_term = get_search_term()
            matches = []
            for user, site, pwd in passwords:
                if (f'username:{user.lower()}' in search_term or
                    f'site:{site.lower()}' in search_term or
                    f'password:{pwd.lower()}' in search_term):
                    matches.append((user, site, pwd)) 
            if matches:
                print("\nMatching passwords:")
                for i, (user, site, pwd) in enumerate(matches, 1):
                    print(f"{i}. Username: {user} | Site: {site} | Password: {pwd}")
                print(f"\nFound {len(matches)} matches")
            else:
                print("\nNo matches found")
    except FileNotFoundError:
        print("\nError: Password file not found")
    except Exception as e:
        print(f"\nError during search: {str(e)}")
def update_password(file_path):
    print("\n--- Update Password ---") 
    def get_matching_passwords(search_term):
        matches = []
        try:
            with open(file_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                # Skip header if exists
                try:
                    if csv.Sniffer().has_header(csvfile.read(1024)):
                        csvfile.seek(0)
                        next(reader)
                    csvfile.seek(0)
                except:
                    pass
                for row in reader:
                    if len(row) >= 3 and all(field.strip() for field in row[:3]):
                        if (search_term.lower() in row[0].lower() or  # Username
                            search_term.lower() in row[1].lower()):   # Site
                            matches.append(row[:3])
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return None
        return matches   
    def select_record(matches):
        print("\nMatching records:")
        for i, (user, site, _) in enumerate(matches, 1):
            print(f"{i}. Username: {user} | Site: {site}")
        while True:
            try:
                choice = int(input("Enter record number to update (0 to cancel): "))
                if 0 <= choice <= len(matches):
                    return choice - 1 if choice != 0 else None
                print("Invalid selection")
            except ValueError:
                print("Please enter a number")  
    def get_updated_fields(old_record):
        user, site, pwd = old_record
        print("\nLeave field blank to keep current value") 
        new_user = input(f"Username [{user}]: ").strip() or user
        new_site = input(f"Site [{site}]: ").strip() or site
        new_pwd = input("New password (required): ").strip()
        while True:
            if not new_pwd:
                new_pwd = input("Password cannot be empty. Enter new password: ").strip()
                continue
            confirm = input("Confirm new password: ").strip()
            if confirm == new_pwd:
                break
            print("Passwords don't match")
            new_pwd = input("Enter new password again: ").strip()     
        return [new_user, new_site, new_pwd]   
    def write_updated_file(all_records, updated_index, new_data):
        """Helper: Rewrite entire file with updated record"""
        try:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                # Write header if the file had one previously
                writer.writerow(['Username', 'Site', 'Password'])
                for i, record in enumerate(all_records):
                    if i == updated_index:
                        writer.writerow(new_data)
                    else:
                        writer.writerow(record)
            return True
        except Exception as e:
            print(f"Error writing file: {str(e)}")
            return False
    try:
        search_term = input("Enter username or site to search: ").strip()
        if not search_term:
            print("Search term cannot be empty")
            return      
        matches = get_matching_passwords(search_term)
        if not matches:
            print("No matching passwords found")
            return
        all_records = []
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            try:
                if csv.Sniffer().has_header(csvfile.read(1024)):
                    csvfile.seek(0)
                    next(reader)
                csvfile.seek(0)
            except:
                pass
            all_records = [row[:3] for row in reader if len(row) >= 3 and all(field.strip() for field in row[:3])]       
        selected_index = select_record(matches)
        if selected_index is None:
            print("Update cancelled")
            return
        selected_record = matches[selected_index]
        original_index = next(i for i, rec in enumerate(all_records) 
                            if rec[0] == selected_record[0] and rec[1] == selected_record[1])  
        new_data = get_updated_fields(selected_record)
        if write_updated_file(all_records, original_index, new_data):
            print("\nPassword successfully updated!") 
    except Exception as e:
        print(f"Update failed: {str(e)}")
def main_menu(file_path):
    while True:
        print("\n===== Password Manager =====")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Passwords")
        print("4. Update Password")
        print("5. Exit")
        choice = input("\nSelect option (1-5): ").strip()
        if choice == '1':
            write_password(file_path)
        elif choice == '2':
            view_passwords(file_path)
        elif choice == '3':
            search_passwords(file_path)
        elif choice == '4':
            update_password(file_path)
        elif choice == '5':
            print("\nExiting Password Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select 1-5.")
if __name__ == "__main__":
    print("=== Password Manager ===")
    selected_file = get_user_file_path()
    if selected_file:
        main_menu(selected_file)