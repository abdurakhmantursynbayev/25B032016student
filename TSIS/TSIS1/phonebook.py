import csv
import json
import psycopg2

from config import load_config
from connect import connect



# DATABASE CONNECTION

def db():
    # Load database settings from database.ini
    config = load_config()

    # Connect to PostgreSQL using connect.py
    return connect(config)



# RUN SQL FILE

def run_sql_file(filename):
    # This function runs schema.sql or procedures.sql
    conn = db()
    cur = conn.cursor()

    # Read SQL file
    with open(filename, "r", encoding="utf-8") as file:
        sql = file.read()

    # Execute all SQL commands from file
    cur.execute(sql)

    # Save changes
    conn.commit()

    # Close connection
    cur.close()
    conn.close()

    print(filename, "executed successfully")



# PRINT RESULT ROWS

def print_rows(rows):
    # Simple function to print query results
    if not rows:
        print("No data found")
    else:
        for row in rows:
            print(row)



# ADD CONTACT

def add_contact():
    # Ask user for contact data
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday YYYY-MM-DD: ")
    group = input("Group: ")
    phone = input("Phone: ")
    phone_type = input("Phone type home/work/mobile: ") or "mobile"

    conn = db()
    cur = conn.cursor()

    # Insert main contact data.
    # Group and phone are inserted separately.
    cur.execute(
        "insert into contacts(name, email, birthday) values (%s, %s, %s)",
        (name, email, birthday)
    )

    # Move contact to group.
    # If group does not exist, SQL procedure creates it.
    cur.execute(
        "call move_to_group(%s, %s)",
        (name, group)
    )

    # Add phone only if user entered phone number.
    if phone:
        cur.execute(
            "call add_phone(%s, %s, %s)",
            (name, phone, phone_type)
        )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added")



# ADD PHONE

def add_phone():
    # Add another phone number to existing contact
    name = input("Name: ")
    phone = input("Phone: ")
    phone_type = input("Type home/work/mobile: ") or "mobile"

    conn = db()
    cur = conn.cursor()

    # Call SQL procedure
    cur.execute(
        "call add_phone(%s, %s, %s)",
        (name, phone, phone_type)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Phone added")



# MOVE CONTACT TO GROUP

def move_group():
    # Change contact group
    name = input("Name: ")
    group = input("New group: ")

    conn = db()
    cur = conn.cursor()

    # Call SQL procedure
    cur.execute(
        "call move_to_group(%s, %s)",
        (name, group)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact moved to group")



# SEARCH CONTACTS

def search():
    # Search by name, email, group, or phone
    query = input("Search: ")

    conn = db()
    cur = conn.cursor()

    # Call SQL function
    cur.execute(
        "select * from search_contacts(%s)",
        (query,)
    )

    rows = cur.fetchall()
    print_rows(rows)

    cur.close()
    conn.close()



# FILTER BY GROUP

def filter_group():
    # Show contacts only from selected group
    group = input("Group: ")

    conn = db()
    cur = conn.cursor()

    cur.execute("""
        select c.name, c.email, c.birthday, g.name, p.phone, p.phone_type
        from contacts c
        left join groups g on c.group_id = g.id
        left join phones p on c.id = p.contact_id
        where g.name ilike %s
        order by c.name
    """, (group,))

    rows = cur.fetchall()
    print_rows(rows)

    cur.close()
    conn.close()



# SEARCH BY EMAIL

def search_email():
    # Partial email search.
    # Example: gmail finds all contacts with gmail in email.
    email = input("Email part: ")

    conn = db()
    cur = conn.cursor()

    cur.execute("""
        select c.name, c.email, c.birthday, g.name, p.phone, p.phone_type
        from contacts c
        left join groups g on c.group_id = g.id
        left join phones p on c.id = p.contact_id
        where c.email ilike %s
        order by c.name
    """, (f"%{email}%",))

    rows = cur.fetchall()
    print_rows(rows)

    cur.close()
    conn.close()



# SORT CONTACTS

def sort_contacts():
    # User chooses sorting type
    print("Sort by:")
    print("1. Name")
    print("2. Birthday")
    print("3. Date added")

    choice = input("Choose: ")

    # We choose order_by only from safe options.
    # We do not put raw user input into SQL.
    if choice == "1":
        order_by = "c.name"
    elif choice == "2":
        order_by = "c.birthday"
    elif choice == "3":
        order_by = "c.created_at"
    else:
        print("Wrong choice")
        return

    conn = db()
    cur = conn.cursor()

    cur.execute(f"""
        select c.name, c.email, c.birthday, g.name, p.phone, p.phone_type, c.created_at
        from contacts c
        left join groups g on c.group_id = g.id
        left join phones p on c.id = p.contact_id
        order by {order_by}
    """)

    rows = cur.fetchall()
    print_rows(rows)

    cur.close()
    conn.close()



# PAGINATION

def paginate():
    # This function allows user to navigate pages:
    # next, prev, quit
    limit = 3
    offset = 0

    conn = db()
    cur = conn.cursor()

    while True:
        # Call SQL pagination function
        cur.execute(
            "select * from get_contacts_page(%s, %s)",
            (limit, offset)
        )

        rows = cur.fetchall()

        print("\nPage:", offset // limit + 1)
        print_rows(rows)

        command = input("\nnext / prev / quit: ").lower()

        if command == "next":
            offset += limit

        elif command == "prev":
            offset = max(0, offset - limit)

        elif command == "quit":
            break

        else:
            print("Unknown command")

    cur.close()
    conn.close()



# SHOW ALL CONTACTS

def show_all():
    # Show all contacts with group and phone
    conn = db()
    cur = conn.cursor()

    cur.execute("""
        select c.name, c.email, c.birthday, g.name, p.phone, p.phone_type
        from contacts c
        left join groups g on c.group_id = g.id
        left join phones p on c.id = p.contact_id
        order by c.id
    """)

    rows = cur.fetchall()
    print_rows(rows)

    cur.close()
    conn.close()



# EXPORT TO JSON

def export_json():
    # Export all contacts with phones and group to contacts.json
    conn = db()
    cur = conn.cursor()

    cur.execute("""
        select c.id, c.name, c.email, c.birthday, g.name, p.phone, p.phone_type
        from contacts c
        left join groups g on c.group_id = g.id
        left join phones p on c.id = p.contact_id
        order by c.id
    """)

    rows = cur.fetchall()

    # Dictionary is used to group many phone numbers under one contact.
    data = {}

    for contact_id, name, email, birthday, group, phone, phone_type in rows:
        # If contact is not added yet, create contact object.
        if contact_id not in data:
            data[contact_id] = {
                "name": name,
                "email": email,
                "birthday": str(birthday) if birthday else None,
                "group": group,
                "phones": []
            }

        # Add phone if contact has phone.
        if phone:
            data[contact_id]["phones"].append({
                "phone": phone,
                "phone_type": phone_type
            })

    # Write JSON file.
    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(list(data.values()), file, indent=4, ensure_ascii=False)

    cur.close()
    conn.close()

    print("Exported to contacts.json")



# DELETE CONTACT

def delete_contact(cur, name):
    # Delete contact by name.
    # Phones are deleted automatically because ON DELETE CASCADE.
    cur.execute(
        "delete from contacts where lower(name) = lower(%s)",
        (name,)
    )



# INSERT CONTACT FROM DICTIONARY

def insert_contact(cur, item):
    # This helper is used for JSON and CSV import.
    name = item["name"]
    email = item.get("email")
    birthday = item.get("birthday")
    group = item.get("group") or "Other"

    # Insert contact.
    cur.execute(
        "insert into contacts(name, email, birthday) values (%s, %s, %s)",
        (name, email, birthday)
    )

    # Add group.
    cur.execute(
        "call move_to_group(%s, %s)",
        (name, group)
    )

    # Add all phones.
    for phone_item in item.get("phones", []):
        phone = phone_item.get("phone")
        phone_type = phone_item.get("phone_type") or "mobile"

        if phone:
            cur.execute(
                "call add_phone(%s, %s, %s)",
                (name, phone, phone_type)
            )



# IMPORT FROM JSON

def import_json():
    # Read contacts from contacts.json
    with open("contacts.json", "r", encoding="utf-8") as file:
        contacts = json.load(file)

    conn = db()
    cur = conn.cursor()

    for item in contacts:
        name = item["name"]

        # Check duplicate by name.
        cur.execute(
            "select id from contacts where lower(name) = lower(%s)",
            (name,)
        )

        exists = cur.fetchone()

        if exists:
            # If duplicate exists, ask user.
            action = input(f"{name} exists. skip/overwrite: ").lower()

            if action == "skip":
                continue

            elif action == "overwrite":
                delete_contact(cur, name)

            else:
                print("Unknown action. Skipped")
                continue

        # Insert contact after duplicate check.
        insert_contact(cur, item)

    conn.commit()
    cur.close()
    conn.close()

    print("JSON imported")



# IMPORT FROM CSV

def import_csv():
    # CSV should have columns:
    # name,email,birthday,group,phone,phone_type
    conn = db()
    cur = conn.cursor()

    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Convert CSV row to same format as JSON item.
            item = {
                "name": row["name"],
                "email": row.get("email"),
                "birthday": row.get("birthday"),
                "group": row.get("group"),
                "phones": [
                    {
                        "phone": row.get("phone"),
                        "phone_type": row.get("phone_type") or "mobile"
                    }
                ]
            }

            name = item["name"]

            # Check duplicate by name.
            cur.execute(
                "select id from contacts where lower(name) = lower(%s)",
                (name,)
            )

            exists = cur.fetchone()

            if exists:
                action = input(f"{name} exists. skip/overwrite: ").lower()

                if action == "skip":
                    continue

                elif action == "overwrite":
                    delete_contact(cur, name)

                else:
                    print("Unknown action. Skipped")
                    continue

            # Insert contact after duplicate check.
            insert_contact(cur, item)

    conn.commit()
    cur.close()
    conn.close()

    print("CSV imported")



# MAIN MENU

def menu():
    while True:
        print("""
PHONEBOOK TSIS1

1. Create schema
2. Create procedures
3. Add contact
4. Add phone
5. Move contact to group
6. Search
7. Filter by group
8. Search by email
9. Sort contacts
10. Pagination
11. Export JSON
12. Import JSON
13. Import CSV
14. Show all contacts
0. Exit
""")

        choice = input("Choose: ")

        try:
            if choice == "1":
                run_sql_file("schema.sql")

            elif choice == "2":
                run_sql_file("procedures.sql")

            elif choice == "3":
                add_contact()

            elif choice == "4":
                add_phone()

            elif choice == "5":
                move_group()

            elif choice == "6":
                search()

            elif choice == "7":
                filter_group()

            elif choice == "8":
                search_email()

            elif choice == "9":
                sort_contacts()

            elif choice == "10":
                paginate()

            elif choice == "11":
                export_json()

            elif choice == "12":
                import_json()

            elif choice == "13":
                import_csv()

            elif choice == "14":
                show_all()

            elif choice == "0":
                print("Goodbye")
                break

            else:
                print("Wrong choice")

        except psycopg2.Error as error:
            print("Database error:", error)

        except FileNotFoundError:
            print("File not found")

        except json.JSONDecodeError:
            print("Invalid JSON file")

        except Exception as error:
            print("Error:", error)


# Start program.
menu()