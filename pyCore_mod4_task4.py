def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts.update({name : phone})
        return f"Contact {name} updated with {phone} as new phone"
    else:
        return "Invalid contact name"

def print_phone(args, contacts):
    name = args[0]
    phone = contacts[name]
    if name in contacts.keys():
        return phone
    else:
        return "Invalid contact name"
    
def print_all_contacts(contacts):
    if len(contacts) == 0:
        return "No saved contacts"
    else:
        contacts_output = ""
        for name, phone in contacts.items():
            contacts_output += f"Contact Name: {name}, Phone Number: {phone}\n"
        return contacts_output


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(print_phone(args, contacts))
        elif command == "all":
            print(print_all_contacts(contacts))
        else:
            print("Invalid command")


main()