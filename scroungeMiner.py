"""ECU CSI2108 Assessable Workshop - Blockchain & Cryptocurrencies."""

import time
import datetime
import hashlib


def _timestamp():
    """Return the current date and time in blockchain format."""
    # Calculate current date and time
    now = datetime.datetime.now()
    # Convert now into a string
    timestring = str(now)
    # Create a string correctly formatted for the file
    stamp = "TIME  = " + timestring
    # Write the correctly formatted string
    return stamp


# Checks to see if previous blocks. If not start first block.
def _checkFirst():
    """If no blockchain exists, start a new one."""
    # Open filename, create if need be. Set stream at EOF
    BCfile = open(blockchain, mode="a+")
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
        timestamp = _timestamp()
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
        hashString = "PREV  = " + hashDigest
        BCfile.write(hashString + "\n")
        print(hashString)
        nonceString = "NONCE = 0"
        BCfile.write(nonceString + "\n")
        print(nonceString)
        # End of block furniture
        end = "-----END BLOCK-----\n\n"
        BCfile.write(end)
        print(end)
    # Regardless of new file or not. Close at the end.
    BCfile.close()


def _ledgerHash():
    """Return a SHA256 of "ledger.txt"."""
    # Open the ledger file, creating it if needed
    Lfile = open(ledger, mode="a+")
    # Start reading the file from the Start
    Lfile.seek(0)
    # Start a hash object
    hash = hashlib.sha256()
    # Set a 64kb buffer in case file is huge!
    bufferSize = 65536
    # Infinite loop through file broken if no data is read
    while True:
        # Read the buffer
        chunk = Lfile.read(bufferSize)
        if not chunk:
            break
        # Update the hash with the chunk as bytes
        hash.update(chunk.encode())
    # Close the file when done
    Lfile.close()
    # Return the hash of the ledger file
    return hash


def _getNewIndex():
    """Return the last known index from the blockchain file."""
    # Open the blockchain file
    blockfile = open(blockchain, mode="a+")
    # Seek to the start of the file
    blockfile.seek(0)
    # Convert the file into a list of lines
    lines = list(blockfile)
    # Reverse the order of the lines
    lines = reversed(lines)
    # Strip all lines of leading and trailing whitespace & EOL
    lines = (line.strip() for line in lines)
    # Remove all blank lines
    lines = (line for line in lines if line)
    # Start a counter for the for loop
    counter = 0
    # Iterate through the lines
    for line in lines:
        # Increment the counter each time
        counter += 1
        # At the sixth line, do the following
        if counter == 6:
            # Return an integer conversion of the number
            # Take all characters including and after the 8th
            # This accounts for multi-digit numbers
            lastIndex = int(line[8:])
            # Increment the existing index to get the new index
            return lastIndex + 1
            # Stop the for loop
            break
    # Cleanly close the file before ending this function
    blockfile.close()


def _getLastHash():
    """Return the hash of the previous block."""
    # Open the blockchain file
    blockfile = open(blockchain, mode="a+")
    # Seek to the start of the file
    blockfile.seek(0)
    # Convert the file into a list of lines
    lines = list(blockfile)
    # Reverse the order of the lines
    lines = reversed(lines)
    # Strip all lines of leading and trailing whitespace & EOL
    lines = (line.strip() for line in lines)
    # Remove all blank lines
    lines = (line for line in lines if line)
    # Start a counter for the for loop
    counter = 0
    hash = hashlib.sha256()
    # Iterate through the lines
    for line in lines:
        # At the sixth line, do the following
        if counter < 8:
            # Add each line to be hashed
            hash.update(line.encode())
        # Increment the counter each time
        counter += 1
    return hash
    # Cleanly close the file before ending this function
    blockfile.close()


def _getData():
    """Return last line (new transaction) from "ledger.txt."""""
    # Open the ledger file
    Lfile = open(ledger, mode="a+")
    # Seek to the start of the tape
    Lfile.seek(0)
    lines = list(Lfile)
    # Reverse the order of the lines
    lines = reversed(lines)
    # Strip all lines of leading and trailing whitespace & EOL
    lines = (line.strip() for line in lines)
    # Remove all blank lines
    lines = (line for line in lines if line)
    # Start a counter for the for loop
    for line in lines:
        return line
        break


def _newBlock():
    """Create a new block on the blockchain."""
    print("-----BEGIN BLOCK-----")
    # Get the last index from the blockchain filename
    index = _getNewIndex()
    print("INDEX = " + str(index))
    # Generate a timestamp for this block
    time = _timestamp()
    print("TIME  = " + time)
    # Gather the last transaction as the block data
    data = _getData()
    print("DATA  = " + data)
    lastHash = _getLastHash()
    print("PREV  = " + lastHash.hexdigest())


try:
    """Main program loop."""
    # Main runtime logic, inspired by previous assignment
    print("\n")
    print("CSI2108 \"ScroungeCoin\" Mining Program.")
    print("Press CTRL+C to quit the program cleanly at any time.")
    print("This program works alongside \"scroungeLedger.py\".")
    print("This program checks \"ledger.txt\" for transactions.")
    print("This program adds blocks to \"blockchain.txt\".")
    # Set filename as a variable for easy change if needed
    blockchain = "blockchain.txt"
    ledger = "ledger.txt"
    # Maintain state of ledger file in this variable
    lastLedger = _ledgerHash()
    # Infinite loop unless KeyboardInterrupt
    while True:
        # Check if a previous block exists in the blockchain file
        _checkFirst()
        # Update the state of the ledger with current state
        currentLedger = _ledgerHash()
        # Let the user know the current state of the ledger
        if (currentLedger.hexdigest() != lastLedger.hexdigest()):
            _newBlock()
        # Update the last known ledger state to the one used
        lastLedger = currentLedger
        # Wait for fives seconds before repeating infinite loop
        time.sleep(5)
except KeyboardInterrupt:
    # Catch keyboard interrupts and close cleanly
    quit()
