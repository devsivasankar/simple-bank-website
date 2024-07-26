import random


def main():
    print('WELCOME TO XYZ BANK')
    print('1.create a new account\n2.enquiry')
    user = input('choose your option(1 or 2):  ')
    
    # if user select option one for opening new account
    if(user == '1'):
        name = input('Enter Your Name: ')
        age = int(input('Enter Your Age: '))
        while True:
            mobile_number = str(input('Enter Your Mobile Number: '))
            convert_mobile = len(mobile_number)
            if(convert_mobile < 10):
                print('enter valid mobile number')
                mobile_number = str(input('Enter Your Mobile Number: '))
            else:
                district = input('Enter Your District: ')
                state = input('Enter Your State: ')     
                otp = random.randint(9999,999999)  # generate otp
                print(otp)
                userotp = int(input('Enter OTP: '))
                if(userotp == otp):
                    print('successfully account created')
                    main()
                else:
                    print('invalid OTP')
                    userotp = int(input('Enter valid OTP: '))
                if(userotp == otp):
                    print('successfully account created')
                else:
                    print('you have enter invalid otp twice')
                main()    # if password incorrect program start again


    # if user select option two for enquiry
    elif(user == '2'):
        global balance
        balance = 0
        enquiry = True
        
        while enquiry:
            print('1.balance\n2.deposite\n3.withdraw\n4.exit')
            choice = print('Choice Your Option(1 or 2 or 3 or 4)')
            userchoice = input('Enter Your Choice: ')
            if(userchoice == '1'):
                balance_check()
            elif(userchoice == '2'):
                deposite()
            elif(userchoice == '3'):
                withdraw()
            elif(user == '4'):
                main()
                enquiry = False
            

    else:
        print('Invalid choice')




# check balance function
def balance_check():
    print(f'Your balance is {balance:.2f}')

# deposite function
def deposite():
    global balance
    print('WELCOME TO DEPOSITE PAGE')
    dep_amt = float(input('Enter Your Deposite Amount: '))
    print(dep_amt)
    if(dep_amt < 0):  # if user type negative number
        print('Invalid Amount')
    else:
        print('Amount deposited successfully')
        balance += dep_amt
    
    
# withdraw function
def withdraw():
    global balance
    print('WELCOME TO WITHDRAW PAGE')
    with_amt = float(input('Enter Withdraw Amount: '))
    if(with_amt < 0):
        print('invalid amount')
    elif(with_amt > balance):
        print('insufficiant balance to your account')
    else:
        balance -= with_amt
        print('amount withdraw successfully')


main()
