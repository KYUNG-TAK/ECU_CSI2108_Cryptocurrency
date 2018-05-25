"""ECU CSI2108 Assessable Workshop - Blockchain & Cryptocurrencies."""


def _addTransaction():
    # Spawn sender variable outside scope of below while loop
    sender = ""
    # Keep asking for input until it is 100% letters
    while (sender.isalpha() is False):
        sender = input("From (max 10, letters only): ")
    # Sanitise input
    sender = sender.strip()
    # Lower case only
    sender = sender.casefold()
    # Use only the first 10 characters of the input
    sender = sender[0:10]
    # Confirm the stripped, trimmed input to the user
    print("Sending from: " + sender)
    # Spawn recipient variable outside scope of below while loop
    recipient = ""
    # Keep asking for input until it is 100% letters
    while (recipient.isalpha() is False):
        recipient = input("To (max 10, letters only): ")
    # Sanitise input
    recipient = recipient.strip()
    # Lower case only
    recipient = recipient.casefold()
    # Use only the first 10 characters of the input
    recipient = recipient[0:10]
    # Confirm the stripped, trimmed input to the user
    print("Sending to: " + recipient)
    # Spawn amount variable outside scope of below while loop
    amount = ""
    while (amount.isdigit() is False):
        amount = input("Amount (max 10, digits only): ")
    # Sanitise input
    recipient = recipient.strip()
    # Use only the first 10 characters of the input
    amount = amount[0:10]
    print("Amount is: " + amount)
    try:
        # The ledger file, stored as a variable for easier changes
        filename = "ledger.txt"
        # Open the file for appending, or create if it does not already exist
        ledger = open(filename, mode='a+')
        # Pad the sender name to 10 characters with whitespace for formatting
        sender10 = sender.ljust(10)
        # Write the padded sender to the ledger with the set formatting
        ledger.write("|FROM:| " + sender10)
        # Pad the recipient to 10 characters with whitespace for formatting
        recipient10 = recipient.ljust(10)
        # Write the padded recipient to the ledger with the set formatting
        ledger.write(" |TO:| " + recipient10)
        # Write the amount to the ledger witht he set formatting
        ledger.write(" |AMOUNT:| " + amount + "\n")
    # Watch out for errors opening the file for writing
    except (FileNotFoundError, PermissionError) as e:
        # Inform the user that there was an IO error
        print("Unable to open " + filename + " for writing. Quitting program.")
        # Exit the program, no facility to correct this error
        quit()


try:
    # Main runtime logic, inspired by previous assignment
    print("\n")
    print("CSI2108 \"ScroungeCoin\" Cryptocurrency Ledger System.")
    print("Press CTRL+C to quit the program cleanly at any time.")
    print("This file adds transactions to \"ledger.txt\".")
    # Infinite loop unless "no" or KeyboardInterrupt
    while True:
        # Start an input variable outside scope of below while loop
        choice = ""
        while (choice != "yes") and (choice != "no"):
            choice = input("New transaction? \"yes\" to add: ")
            # Basic input sanitising
            choice = choice.strip()
            # Aggressively convert input to lower case
            choice = choice.casefold()
        if (choice == "yes"):
            _addTransaction()
        if (choice == "no"):
            quit()
except KeyboardInterrupt:
    # Catch keyboard interrupts and close cleanly
    quit()
