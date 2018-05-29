# ECU 2018 CSI2108 Assessable Workshop 3
Rudimentary Python-based cryptocurrency system with separate transaction and mining programs
# Introduction
This documentation accompanies the author’s submission to CSI2108 – Cryptographic Concepts Workshop 6 in 2018 (the workshop). The task for the workshop was to implement a cryptocurrency in Python to operate on a single computer. This is in support of learning about how hash functions and blockchains operate. The task was to write two programs, each of which manages a particular file. A transaction-recording program takes user input and adds it to a ledger file. A mining program monitors the ledger for changes, and creates a new block with the new transaction. The author named this cryptocurrency “scroungeCoin.”
# Requirements
- Python 3.6.5+
- Windows 10
- Write access to program directory
# Assumptions
- “blockchain.txt” and “ledger.txt” created and modified only by this program
- This program has write access to the folder in which it is executing
# Instructions
1. Execute scroungeMiner.py, leave it running to monitor “ledger.txt” for changes
2. Execute scroungeLedger.py
3. Type “yes” to add a transaction to “ledger.txt”
4. Press enter
5. Type a name for the sender
  a. Must be letters only
  b. Must not exceed 10 letters
  c. If blank, scroungeLedger.py generates 10 random letters for you
6. Press enter
7. Type a name for the recipient
  a. Must be letters only
  b. Must not exceed 10 letters
  c. If blank, scroungeLedger.py generates 10 random letters for you
8. Press enter
9. Type an amount
  a. Must be numbers only
  b. Must not exceed 10 digits
  c. If blank, scroungeLEdger.py generates 10 random numbers for you
10. Press enter
11. Repeat steps 3-10 as required to add new transactions
12. View the new block, either in “blockchain.txt” or the terminal running scroungeMiner.py
13. Press CTRL+C to cleanly exit each of scroungeMiner.py and scroungeLedger.py
# Documentation
scroungeCoin contains two main program parts. This documentation explains each below.
## scroungeLedger.py
scroungeLedger.py is the transaction recording system of this cryptocurrency. It works with a file called “ledger.txt.” Below shows the basic flow of user interaction with this program.
1. Start Program
2. Type "yes" to add a transaction
  - Case insensetive
  - Must be whole word
3. Enter sender (from)
  - Letters only
  - No numbers
  - Convers to lower case
  - If empty, generates random
4. Enter recipient (to)
  - Letters only
  - Convers to lower case
  - If empty, generates random
5. Enter amount
  - Numbers only
  - If empty, generates random
6. CTRL+C to Exit
scroungeLedger.py uses the following functions to support the main program logic.
### _randomGen
- Helper function generates 10 character random string for easy prototyping
- If parameter “c”, generates random 10 letter name for use on ledger
- If parameter “n”, generates random 10 digit number for use on ledger
### _addTransaction
- Asks for user input for Sender and Recipient
-   If input received, checks to make sure it’s all letters
- If no input, calls _randomGen to make a random name
  - Sanitises input to lower case letters
- Asks for user input for Amount
  - If input received, checks to make sure it’s all numbers
  - If no input, calls _randomGen to make a random number
- Tries to open “ledger.txt” and gives a descriptive error if it fails
- Writes the transaction to “ledger.txt” in the following prescribed format:
```
|FROM:| qtxqoqmygo |TO:| gdwzxwuked |AMOUNT:| 4261606285
```
## scroungeMiner.py
scroungeMiner.py is the mining system for this cryptocurrency. It works with a file called “blockchain.txt” and reads from “ledger.txt.” It will create one or both of these files as required. This program does not require any direct user input.
1. [Start Program]
2. Ledger Change Detected
3. Check if a previous block exists
  - If not, write the first block
4. Start a new block
  - Increment index
  - Get timestamp
  - Read new data
  - Hash previous block
  - Start a nonce
5. Try for a Nonce
  - Increment nonce
  - See if hash has 14 leading zeroes
6. Stop Finding Nonce
  - If hash has 14 leading zeroes
  - Or nonce hits 50000
7. Write block
8. CTRL+C to Exit
scroungeMiner.py uses the following functions to support the main program logic.
### _timestamp
- Wrapper function for datetime object creation using datetime Python library
### _writeBlock
- Converts the parameter strings (and index integer) to the correctly formatted layouts
- Writes the formatted layout to “blockchain.txt”
- Prints the layout to the terminal
- Uses the following prescribed format for all writing to file and terminal
```
-----BEGIN HASH-----
2AF7909CA08F18FACC556624B02E1A5C683BB0F557137B1EF7E0028FC457715C
-----BEGIN BLOCK-----
INDEX = 0
TIME  = 2018-05-29 01:02:123456
DATA  = |FROM:| qtxqoqmygo |TO:| gdwzxwuked |AMOUNT:| 4261606285
PREV  = [none]
NONCE = [none]
-----END BLOCK-----
```
### _checkFirst
- Opens “blockchain.txt” and checks if the first line reads “-----BEGIN HASH-----“
  - If yes, does nothing
  - If no, writes the arbitrary first block to “blockchain.txt”
### _ledgerHash
- Opens “ledger.txt”
- Reads “ledger.txt” in 64kb chunks
- Adds those chunks to a SHA256 object
- Returns the SHA256 of the total contents of the file
### _getNewIndex
- Assumes _checkFirst has already been completed
- Opens “blockchain.txt”
- Reads the 6th from last line, which should be the last index used
- Converts it to an integer
- Increments it
- Returns the incremented integer
### _hashPrevBlock
- Opens “blockchain.txt”
- Reads the last block excluding
  - Its hash value
  - The formatting around the fields
- Creates a SHA256 object
- Adds the fields to that SHA256 object
- Returns the hash as bytes
### _getNewData
- Opens “ledger.txt”
- Strips out any blank lines and whitespace
- Reads the last populated line, which it assumes to be the new data
- Returns the line as a string
### _newBlock
- Starts a nonce at 0
- Calls
  - _getNewIndex
  - _timestamp()
  - _getNewData()
  - _hashPrevBlock
- Creates a hash object of the new block and adds the nonce value to the hash object
- If the total hash has 14 leading zeroes, write the block and its hash to “blockchain.txt”
- If the nonce value hits 50 000, write the block and its hash to “blockchain.txt”
- If not, increment the nonce value by 1

