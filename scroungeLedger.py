"""ECU CSI2108 Assessable Workshop - Blockchain & Cryptocurrencies."""

import string
import random


def _randomGen(category):
    """Generate 10 random letters or numbers."""
    length = 10
    chars = string.ascii_lowercase
    digits = string.digits
    if category == "c":
        result = ""
        counter = 0
        while counter < length:
            result += random.choice(chars)
            counter += 1
        return result
    if category == "n":
        result = ""
        counter = 0
        while counter < length:
            result += random.choice(digits)
            counter += 1
        return result


def _addTransaction():
    """Add the transaction to "ledger.txt"."""
    # Spawn sender variable outside scope of below while loop
    sender = ""
    # Keep asking for input until it is 100% letters
    while (sender.isalpha() is False):
        sender = input("From (max 10, letters only): ")
        if sender == "":
            sender = _randomGen("c")
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
        if recipient == "":
            recipient = _randomGen("c")
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
    # Make sure the input is a number greater than 1
    while (amount.isdigit() is False) or (int(amount) < 1):
        amount = input("Amount (max 10, digits only): ")
        if amount == "":
            amount = _randomGen("n")
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
    """Main program logic."""
    # Main runtime logic, inspired by previous assignment
    print("CSI2108 \"ScroungeCoin\" Ledger Program.")
    print("Press CTRL+C to quit cleanly at any time.")
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
