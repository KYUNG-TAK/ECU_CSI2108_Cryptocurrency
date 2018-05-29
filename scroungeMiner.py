"""ECU CSI2108 Assessable Workshop - Blockchain & Cryptocurrencies."""

import time
import datetime
import hashlib


def _timestamp():
    """Return the current date and time."""
    # Calculate current date and time
    now = datetime.datetime.now()
    # Convert now into a string
    timestring = str(now)
    # Write the correctly formatted string
    return timestring


def _writeBlock(hash, index, time, data, previous, nonce):
    """Write the block to blockchain.txt & output to terminal."""
    # Set up the formatted strings
    header = "-----BEGIN HASH-----"
    hashFormat = "HASH  = " + str(hash)
    midder = "-----BEGIN BLOCK-----"
    indexFormat = "INDEX = " + str(index)
    timeFormat = "TIME  = " + time
    dataFormat = "DATA  = " + data
    previousFormat = "PREV  = " + previous
    nonceFormat = "NONCE = " + str(nonce)
    footer = "-----END BLOCK------"
    # Open the file for writing, seek to the end of the tape
    BCfile = open(blockchain, mode="a+")
    BCfile.write(header+"\n")
    BCfile.write(hashFormat+"\n")
    BCfile.write(midder+"\n")
    BCfile.write(indexFormat+"\n")
    BCfile.write(timeFormat+"\n")
    BCfile.write(dataFormat+"\n")
    BCfile.write(previousFormat+"\n")
    BCfile.write(nonceFormat+"\n")
    BCfile.write(footer+"\n\n")
    BCfile.close()
    # Print the new block to the terminal
    print(header)
    print(hashFormat)
    print(midder)
    print(indexFormat)
    print(timeFormat)
    print(dataFormat)
    print(previousFormat)
    print(nonceFormat)
    print(footer+"\n")


# Checks to see if previous blocks. If not start first block.
def _checkFirst():
    """If no blockchain exists, start a new one."""
    # Open filename, create if need be. Set stream at EOF
    BCfile = open(blockchain, mode="a+")
    # Variable outside scope of iterator through file lines
    isFirst = True
    # Beginning of block furniture to look for
    begin = "-----BEGIN HASH-----"
    BCfile.seek(0)
    firstline = BCfile.readline()
    if firstline.strip() == begin.strip():
        isFirst = False
    # If no lines contained block furniture, start from scratch
    if isFirst is True:
        isFirst is False
        print("\nNo previous blocks. Starting first block.\n")
        time = _timestamp()
        index = 0
        data = "first block"
        previous = "[none]"
        nonce = "[none]"
        dataBytes = data.encode()
        hash = hashlib.sha256(dataBytes)
        digest = hash.hexdigest()
        _writeBlock(digest, index, time, data, previous, nonce)


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


def _hashPrevBlock():
    """Return hash of the previous block sans EOL & spaces."""
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
    # Recast the lines object as a list
    lines = list(lines)
    # Trim the reversed list to just the first (last) 7 lines
    lines = lines[:7]
    # Un-reverse the order of these last 7 lines back to normal
    lines = reversed(lines)
    # Recast as list
    lines = list(lines)
    # Strip out the beginning and ending furniture
    lines = lines[1:6]
    counter = 0
    for line in lines:
        lines[counter] = line.strip()
        lines[counter] = line[8:]
        counter += 1
    # Start a new sha256 object
    hash = hashlib.sha256()
    # Iterate through this list of the last block
    for line in lines:
        # Add each line to the hash object for hashing
        hash.update(line.encode())
    # Cleanly close the file before ending this function
    blockfile.close()
    return hash


def _getNewData():
    """Return last line (new transaction) from "ledger.txt."""""
    # Open the ledger file
    Lfile = open(ledger, mode="a+")
    # Seek to the start of the tape
    Lfile.seek(0)
    # Create a new list object from the file
    lines = list(Lfile)
    # Reverse the order of the lines
    lines = reversed(lines)
    # Strip all lines of leading and trailing whitespace & EOL
    lines = (line.strip() for line in lines)
    # Remove all blank lines
    lines = (line for line in lines if line)
    # Start a counter for the for loop
    for line in lines:
        # Return the first line of the reversed list
        # i.e. the new transaction is the last line
        newTransaction = line
        # Breaking here means the for loop only happens once
        break
    return newTransaction


def _newBlock():
    """Create a new block on the blockchain."""
    nonce = 0
    # Get the last index from the blockchain filename
    index = _getNewIndex()
    # Generate a timestamp for this block
    time = _timestamp()
    # Gather the last transaction as the block data
    data = _getNewData()
    # SHA256 of previous block contents
    prevHash = _hashPrevBlock()
    prevHashString = prevHash.hexdigest()
    # First convert the index to a string (rest are strings)
    indexString = str(index)
    # Encode the strings to bytes for hashing
    indexBytes = indexString.encode()
    timeBytes = time.encode()
    dataBytes = data.encode()
    hashBytes = prevHashString.encode()
    # Create a block variable to hold the whole block
    block = indexBytes + timeBytes + dataBytes + hashBytes
    while True:
        # Reset the hash variable
        newhash = None
        # Start the hash variable
        newhash = hashlib.sha256()
        # Add the block to be hashed
        newhash.update(block)
        # Convert the nonce to a string
        nonceString = str(nonce)
        # Prepare the nonce for adding to the hash
        nonceBytes = nonceString.encode()
        # Update block by concatenating the nonceBytes
        newhash.update(nonceBytes)
        # Create a string of the hash
        digest = newhash.hexdigest()
        # Get the first 14 characters of the hash digest
        first14 = digest[0:14]
        # Fourteen zeroes for comparison
        fourteenZeros = "00000000000000"
        if (first14 == fourteenZeros):
            _writeBlock(digest, index, time, data, prevHashString, nonce)
            # Break out of the infinite while loop
            break
        # Per instructions call it quits at nonce value of 50 000
        if (nonce >= 50000):
            _writeBlock(digest, index, time, data, prevHashString, nonce)
            # Break out of the infinite while loop
            break
        nonce += 1


try:
    """Main program loop."""
    # Main runtime logic, inspired by previous assignment
    print("CSI2108 \"ScroungeCoin\" Mining Program.")
    print("Press CTRL+C to quit cleanly at any time.")
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
        time.sleep(1)
except KeyboardInterrupt:
    # Catch keyboard interrupts and close cleanly
    quit()
