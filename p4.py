"""
Moves through a series of lists
"""
__author__ = "Dane Kipp"
__date__ = "2016-10-07"

def createMenu(tmpList):
    """
    Takes tmpList and returns a numbered string
    with line breaks between each option
    """
    ct = 1
    tmpStr = ""
    for option in tmpList:
        tmpStr += "\t" + str(ct) + ". " + option + " " + "\n"
        ct += 1
    return(tmpStr)

def validChoice(lst,str):
    """
    Returns a choice that is a digit between 1 and
    the length of the lst
    """
    ch = input("Please enter your choice: ")
    while ch.isdigit() is False or int(ch) < 1 or int(ch) > len(lst):
        print(str)
        ch = input("Please enter a valid choice: ")
    return(int(ch))

def mainMenu():
    """
    Displays main menu and prompts the user for a choice
    """
    print(mainStr)
    choice = validChoice(mainList, mainStr)
    if choice == 1:
        print()
        checkingMenu()
    elif choice == 2:
        print()
        savingsMenu()       
    else:
        print()
        print("Program Ended")

def checkingMenu():
    """
    Displays checking menu and prompts the user for a choice
    """
    print(checkingStr)
    choice = validChoice(checkingList, checkingStr)
    while choice != 3:
        if choice == 1:
            print("Deposit not implemented yet")
            print()
            print(checkingStr)
            choice = validChoice(checkingList, checkingStr)
        else:
            print("Withdraw not implemented yet")
            print()
            print(checkingStr)
            choice = validChoice(checkingList, checkingStr)
    print()
    mainMenu()

def savingsMenu():
    """
    Displays savings menu and prompts the user for a choice
    """
    print(savingsStr)
    choice = validChoice(savingsList, savingsStr)
    while choice != 4:
        if choice == 1:
            print("Print Balance not implemented yet")
            print()
            print(savingsStr)
            choice = validChoice(savingsList, savingsStr)
        elif choice == 2:
            print("Calculate Interest not implemented yet")
            print()
            print(savingsStr)
            choice = validChoice(savingsList, savingsStr)
        else:
            print("Close Savings Account not implemented yet")
            print()
            print(savingsStr)
            choice = validChoice(savingsList, savingsStr)        
    mainMenu()

if __name__ == "__main__":
    mainList = ["Checkings", "Savings", "Exit"]
    checkingList = ["Deposit", "Withdraw", "Return to Main Menu"]
    savingsList = ["Print Balance", "Calculate Interest", "Close Savings Account", "Return to Main Menu"]

    mainStr = "Main Menu:" + "\n" + createMenu(mainList)
    checkingStr = "Checking:" + "\n" + createMenu(checkingList)
    savingsStr = "Savings:" + "\n" + createMenu(savingsList)
    
    mainMenu()
