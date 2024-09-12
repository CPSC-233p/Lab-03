#Jacob Fishel
#9/11/2024
#Main file to print prompt screen and use functions to make a contact list

import contacts

contact_list = []

while True:
    print("       *** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Print list:")
    print("2. Add contact:")
    print("3. Modify contact:")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit program:\n")

    menuChoice = int(input("Enter menu choice: "))
    
    match menuChoice:
        case 1:
            contacts.print_list(contact_list)

        case 2:
            firstName = input("Please enter the first name: ")
            lastName = input("Please enter the last name: ")

            contact_list = contacts.add_contact(contact_list, first_name=firstName, last_name=lastName)

        case 3:
            index = int(input("Please enter the index: "))

            if index >= len(contact_list):
                print("Invalid index")
                continue

            firstName = input("Please enter the first name: ")
            lastName = input("Please enter the last name: ")

            contacts.modify_contact(contact_list, first_name=firstName, last_name=lastName, index=index)

        case 4:
            index = int(input("Please enter the index: "))
            contacts.delete_contact(contact_list, index=index)

        case 5:
            contact_list = contacts.sort_contacts(contact_list, column=0)

        case 6:
            contact_list = contacts.sort_contacts(contact_list, column=1)
            
        case 7:
            break
        case _:
            break