selection = 0


while selection >= 0:
    print "======================"
    print "1.Returning Customer"
    print "2.New Customer"
    print "3.Guest"
    print "======================\n"

    selection = int(raw_input("Please select your customer type: "))
    try:
        if selection < 1 or selection > 3:
            selection = int(raw_input("Please select your customer type\n Enter a number between 1 and 3 "))
        elif selection == 1:
            print "Returning Customer"
            selection = -1
        elif selection == 2:
            print "New Customer"
            selection = -1
        elif selection == 3:
            print "Guest"
            selection = -1
        else:
            print "\n\n Please enter a number\n"
    except ValueError:
        print "Please enter a number"

def returning():
    if selection == 1:
        print "Welcome back"


def new():
    if selection == 2:
        print "Welcome valued customer"


def guest():
    if selection == 3:
        print "Welcome"





