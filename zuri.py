import random
from datetime import *

#current date and time
today = date.today()
Date = today.strftime("%b/%d/%Y")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print("Current Date: ", Date,  "       Current Time:", current_time)


Database = {}	


def initialize ():
    print('\nWelcome to DYNAMIC BANK\n')

    GotAccount = int(input('Do you have an account with us? 1 (YES), 2 (NO): '))
    
    if GotAccount == 1:
        login()
    elif GotAccount == 2:
        register()
    else:
        print('Invalid Input')
        initialize()

def login ():
    print('\n************** Login **************')
    
    EnterAccountNumber = int(input("Enter your account number: "))
    Password = input("Enter your password: ")

    for key,value in Database.items():
        if key == EnterAccountNumber:
            if value[3] == Password:
                BankOperations (value)
        else:     
            print('\nInvalid account number or password')
    login()
    
    
def register ():
    print("\nPlease fill the form below to register")
    Email = input("\nE-mail Address: \n")
    FirstName = input("\nFirst Name: \n")
    LastName = input("\nLast Name: \n")
    Password = input("\nCreate Password (Not less then 6 characters): \n")
    
    while len(Password) <6:
    	print("\nPassword cant be less than 6 characters\n")
    	Password = input("\nTry again : \n")

    AccountNumber = AccountNumGenerator()

    Database [AccountNumber] = [FirstName, LastName, Email, Password]
    #return Database
    print("Your account has been created.")
    print ('Your Account Number is: ', AccountNumber, '\n')
    login()

def AccountNumGenerator(): 
    return random.randrange(1111111111, 9999999999)
   # AccountNumGenerator()

def BankOperations (user):
    print("Welcome %s %s" % (user[0], user[1]))
    
    Option = int(input ('\nWhat whould you like to do: \n Deposit (1) \n Withdraw(2) \n Complain (3) \n Logout (4) \n Exit (5) \n'))
    
    if Option == 1:
        Deposit()
    elif Option == 2:
        Withdrawal()
    elif Option == 3:
        Complain ()
    elif Option == 4:
        Logout()
    elif Option== 5:
        exit ()
    else:
        print("\nInvalid Input!")
        BankOperations (user)

def Withdrawal ():
    print('\nHow much would you like to withdraw: \n')
    WithdrawalAmount = int(input('Withdrawal Amount: '))
    print('Please take your Cash')

def Deposit ():
    print('\nHow much would you like to Deposit: ')
    DepositAmount = int(input('Deposit Amount: '))
    print('Your current balance is: 12,000 ')

def Complain ():
    print('\nWhat issue would you like to report?')
    WithdrawlAmount = (input('Complaint(s): '))
    print('\nThank you for contacting us.')

def Logout():
    login()


initialize ()
