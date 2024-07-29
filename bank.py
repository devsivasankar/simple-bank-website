
import random


balance = 0.0
def main():
        print('WELCOME TO ABC BANK')
        print('1.CREATE NEW ACCOUNT\n2.BASIC ENQUIRY')
        userinput1 = input('CHOOSE YOUR OPTION(1 or 2): ')
        if(userinput1 == '1'):
                get_name()
                get_age()
                get_district()
                get_state()
                get_number()
                verifyotp = otp()
                verify_otp(verifyotp)
        elif(userinput1 == '2'):
                while True:
                        print('1.CHECK BALANCE\n2.DEPOSITE\n3.WITHDRAW\n4.EXIT')
                        userinput2 = input('CHOOSE YOUR OPTION(1 or 2 or 3 or 4): ')
                        if(userinput2 == '1'):
                                check_balance()
                        elif(userinput2 == '2'):
                                deposit()
                        elif(userinput2 == '3'):
                                withdraw()
                        elif(userinput2 == '4'):
                                print('THANK YOU FOR CHOOSING ABC BANK')
                                return main()
        else:
                print('INVALID SELECTION')
                return main()
                
                


        
# code for creating new account

def get_name():   #getting name from user
        while True:
                name = input('ENTER YOUR NAME: ')
                if any(char.isdigit() for char in name):
                        print('ENTER VALID NAME WITHOUT NUMBER')
                else:
                        return name
                

def get_age():   #getting age from user
        age = int(input('ENTER YOUR AGE: '))

def get_district():   #getting district from user
        while True:
                district = input('ENTER YOUR DISTRICT: ')
                if any(char.isdigit() for char in district):
                        print('ENTER VALID DISTRICT NAME')
                else:
                        return district

def get_state():     #getting state from user
        while True:
                state = input('ENTER YOUR STATE NAME: ')
                if any(char.isdigit() for char in state):
                        print('ENTER VALID STATE NAME')
                else:
                        return state

def get_number():    #getting mobile number from user
        while True:
                number = input('ENTER YOUR MOBILE NUMBER: ')
                convert_str = len(number)
                if(convert_str < 10 or convert_str > 10):
                        print('ENTER VALID MOBILE NUMBER')
                else:
                        return number

def otp(): # generate otp
        otp = random.randint(100000,999999)
        print(f'YOUR OTP NUMBER IS {otp}')
        return otp

def verify_otp(verifyotp):  # otp section
        while True:
                try:
                        user_otp = int(input('ENTER OTP NUMBER: '))
                        if (verifyotp == user_otp):
                                print('YOUR ACCOUNT CREATED SUCCESSFULLY')
                                return main()
                                break
                        else:
                                print('INVALID OTP NUMBER, PLEASE TRY AGAIN')
                except ValueError:
                        print('ENTER A VALID OTP NUMBER')




# code for basic enquiry
def check_balance():
        global balance
        print(f'YOUR AVAILABLE BALANCE IS {balance:.2f}')
 
def deposit():
        global balance
        dep_amount = float(input('ENTER DEPOSIT AMOUNT: '))
        if(dep_amount <= 0):
                print('INVALID DEPOSIT AMOUNT')
        else:
                print(f'SUCCUSSFULLY AMOUNT {dep_amount} DEPOSITED')
                balance += dep_amount

def withdraw():
        global balance
        amount = float(input('ENTER AMOUNT TO WITHDRAW: '))
        if amount <= 0:
                print('ENTER A VALID AMOUNT')
        elif amount > balance:
                print('INSUFFICIENT BALANCE')
        else:
                balance -= amount
                print(f'{amount:.2f} WITHDRAWN SUCCESSFULLY')



#calling all functions
main()
