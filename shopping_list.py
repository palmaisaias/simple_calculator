#I would usually note all my attempts but there would be 20 pages worth. Not perfect but it executes.
#Task 1,2,3

shopping_list = []

def add_item():
    while True:
        item = input("Enter item you want to add or enter 'end' to return to menu: ")
        if item == 'end':
            break
        else:
            shopping_list.append(item)
            print() #cosmetic
            print('Your current list:', shopping_list)  #shows user an updated list every time they add

def remove_item():
    if not shopping_list:   #checking if the list is empty
        print('There are no items in your shopping list')
        return
    while True:
        item = input("Enter item you want to remove or enter 'end' to return to menu: ")
        if item == 'end':
            break
        elif item in shopping_list:
            shopping_list.remove(item) 
            print('Your current list:', shopping_list)  #shows user an updated list everytime they remove
        else:
            print("item is not in your list")

def shopper():
    while True:
        print() #cosmetic
        choice = input("Would you like to 'add' an item, 'remove' an item, or 'stop'? ")
        if choice == 'add':
            add_item()
        elif choice == 'remove':
            remove_item()
        elif choice == 'stop':
            print() #cosmetic
            print('Here is your list!')
            print('~~~~~~~~~~~~~~~~~~') # since you mentioned the tilde in class lol
            for item in shopping_list:  #imo 'for loop' was the easiest way to format the list
                print('    ', item) #spacing is cosmetic
                print() #cosmetic
            break
        else:
            print('Please enter a valid input')

shopper()