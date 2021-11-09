import re

def moneyAppleCalculator():
    while True:
        money1 = input('How much money do you have? ')
        if money1.isalpha():
            print('Write numbers only!')
        if money1.isdigit():
            break       
    while True:
        applePrice1 = input('How much is the apple? ')
        if applePrice1.isalpha():
            print('Write numbers only!')
        elif applePrice1.isdigit():
            break
    money = int(money1) 
    applePrice = int(applePrice1)
    maxNumApple1 = money//applePrice
    remainMoney1 = money % applePrice
    return money, applePrice, maxNumApple1, remainMoney1


def display(money, applePrice, maxNumApple1, remainMoney1):    
    if money >= applePrice:
        print(f'You can buy {maxNumApple1} apple/s and your change is {remainMoney1} peso/s.')
    elif money < applePrice:
        insufficiency = applePrice-money
        print('Your money is insufficient.')
        while True:
            insufficiencyVal = input('Do you want to know the insufficiency? Y/N: ')
            if re.match("[a-m, o-x, z, A-M, O-X, Z 0-9,]*$", insufficiencyVal):
                print('Only write "Y/y or N/n"')
            elif re.match("[y, n, Y, N]*$", insufficiencyVal):
                if insufficiencyVal.upper() == 'Y':
                    print(f'You need {insufficiency} peso/s more to buy one apple.')
                    break
                elif insufficiencyVal.upper() == 'N':
                    print('Have a nice day!')
                    break

#MONEYAPPLECALCULATOR FUNCTION
#Requests input for the number of money.
#Requests input for the price of the apple.
#Calculates the total apple that can be bought.
#Calculates the remaining money/ change.
money, applePrice, maxNumApple, remainMoney = moneyAppleCalculator()

#DISPLAY FUNCTION
#Displays the maximum number of apple you can buy and the remaining money you have.
#Displays if you have insufficient money.
#Displays if you want to know the insufficiency.
display(money, applePrice, maxNumApple, remainMoney)
