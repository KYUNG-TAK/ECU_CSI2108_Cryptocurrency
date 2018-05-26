"""ECU CSI2108 Assessable Workshop - Blockchain & Cryptocurrencies."""

import time
import datetime
import hashlib


# Checks to see if previous blocks. If not start first block.
def _checkFirst():
    # Variable outside scope of iterator through file lines
    isFirst = True
    # Beginning of block furniture to look for
    begin = "-----BEGIN BLOCK-----"
    BCfile.seek(0)
    firstline = BCfile.readline()
    if firstline.strip() == begin.strip():
        isFirst = False
    # If no lines contained block furniture, start from scratch
    if isFirst is True:
        isFirst is False
        print("\nNo previous blocks. Starting first block.\n")
        # Write the beginning of block furniture
        BCfile.write(begin + "\n")
        # Write the beginning of block furniture
        print(begin)
        # Set up the index string for writing and printing
        index = "INDEX = 0"
        # Write the index string
        BCfile.write(index + "\n")
        # Print the index string
        print(index)
        # Calculate current date and time
        now = datetime.datetime.now()
        # Convert now into a string
        timestring = str(now)
        # Create a string correctly formatted for the file
        timestamp = "TIME  = " + timestring
        # Write the correctly formatted string
        BCfile.write(timestamp + "\n")
        # Print the correctly formatted string
        print(timestamp)
        # The specified arbitrary data of the first block
        data = "first block"
        # The data formatted correctly for the file
        dataString = "DATA  = " + data
        # Write the correctly formatted string to file
        BCfile.write(dataString + "\n")
        # Print the correctly formatted string
        print(dataString)
        dataBytes = data.encode()
        # Hash the data
        hash = hashlib.sha256(dataBytes)
        # Convert the hash from binary to a string
        hashDigest = hash.hexdigest()
        # Set up a correctly formatted string using the digest
        hashString = "HASH  = " + hashDigest
        BCfile.write(hashString + "\n")
        print(hashString)
        nonceString = "NONCE = 0"
        BCfile.write(nonceString + "\n")
        print(nonceString)
        # End of block furniture
        end = "-----END BLOCK-----\n\n"
        BCfile.write(end)
        print(end)


# Main program loop
try:
    # Main runtime logic, inspired by previous assignment
    print("\n")
    print("CSI2108 \"ScroungeCoin\" Mining Program.")
    print("Press CTRL+C to quit the program cleanly at any time.")
    print("This program works alongside \"scroungeLedger.py\".")
    print("This program checks \"ledger.txt\" for transactions.")
    print("This program adds blocks to \"blockchain.txt\".")
    # Infinite loop unless "no" or KeyboardInterrupt
    while True:
        # Set filename as a variable for easy change if needed
        filename = "blockchain.txt"
        # Open filename, create if need be. Set stream at EOF
        BCfile = open(filename, mode="a+")
        _checkFirst()
        BCfile.close()
        time.sleep(5)
except KeyboardInterrupt:
    # Catch keyboard interrupts and close cleanly
    BCfile.close()
    quit()
