#Jacob Fishel
#9/11/2024
# Function implementations for handling contacts

def print_list(contact_list):
    #Displays all contacts in a contact list
        i = 0
        for contact in contact_list:
            print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}') 
            i += 1
        print("\n")


def add_contact(contact_list, first_name, last_name):
      #Adds a new contact to the contact list


      newContact = [first_name, last_name]

      contact_list.append(newContact)
      print("\n")

      return contact_list


def modify_contact(contact_list, first_name, last_name, index):
    #Modifies a contact from the contact list
    size = len(contact_list)

    if index >= size:
        print("Invalid index number.")
        return False
         
    else:
        contact_list[index] = [first_name, last_name]
        return True
            

def delete_contact(contact_list, index):
    #Deteles a contact from the contact list
    size = len(contact_list)

    if index >= size:
        print("Invalid index number.")
        return False


    else:
        item = contact_list[index]
        contact_list.remove(item)
        return True


def sort_contacts(contact_list, column):
    #Sorts contacts from the contct list
    return contact_list.sort(key= lambda element: element[column])     


