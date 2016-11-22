def get_data():
    # get first name, make sure it is not empty
    fn = raw_input("First Name: ")
    while len(fn) < 1:      # Make sure they give me at least 1 character
        fn = raw_input("First name is required. Please re-enter: ")
    # Do the same for the last name
    ln = raw_input("Last Name: ")
    while len(ln) < 1:      # Make sure they give me at least 1 character
        ln = raw_input("Last name is required. Please re-enter: ")
    # Get a phone number next
    # Just make sure they type 10 characters
    ph = raw_input("Enter a 10 digit phone number: ")
    while len(ph) < 10:
        ph = raw_input("Phone is required. Please re-enter 10 digits: ")
        # All data entered and not empty
    return fn, ln, ph

# ------------ MAIN PROGRAM ---------------

# create an empty customer list
customer_list = []
print ("Welcome to the customer database: ")
print ('\nPlease choose from the following menu items: ')

menu_choice = 0 # Initialize the menu choice
# Display the menu and get a valid choice
while menu_choice != 4:             # 3 means done
    print ("   1. New Customer ")
    print ("   2. Returning Customer")
    print ("   3. Guest ")

    choice = raw_input("Choose. ")

    # I need to test to see if they gave me a valid choice
    # If I try to convert bad data into an integer my program will crash (Error)
    # So I'm going to test the string
    # First, I'm taking off the whitespace
    if choice.strip() not in ['1','2','3']:         # Testing for good values in string
        print ("Invalid choice: ")
    else:
        menu_choice = int(choice)           # If it's good convert it to an integer

    # now I need to handle the good choices of 1 or 2
    if menu_choice == 1:
        # call my get data and put the tuple into my customer list
        customer_list.append(get_data())
    elif menu_choice == 2:
        # Loop through the list and display each customer
        for (first, last, phone) in customer_list:
            print (last + ", " + first + "  " + phone  )
        print ""