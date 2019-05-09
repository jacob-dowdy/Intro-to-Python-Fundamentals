# program that takes user input and either adds the item to the list or deletes it.

animals = ["goat","pig","duck"]

def list_o_matic():
    # making sure the provided list isn't empty
    while animals:
        print("Look at all the animals",animals)
        item = input("Enter the name of an animal to add it to the list or remove an existing animal from the list: ")
        if item.lower() == "quit":
          break
        elif item.lower() in str(animals).lower():
            animals.remove(item)
        elif item.lower() not in str(animals).lower():
            animals.append(item)
            print(item,"added to the list")
        # empty strings should remove the last item from the list
        elif item == " ":
            animals.pop()
            print(item,"removed from the list")
    # exit statement access either by entering "quit" or clearing out the list
    print("Goodbye!")
list_o_matic()
