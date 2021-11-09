def appleOrangeTotal():
    print('The apples are 20 pesos,')
    while True:
        apple1 = (input('How many apples do you want to buy? '))
        if apple1.isalpha():
            print('Only input numeral characters.')
        elif apple1.isdigit():
            break
    print('The oranges are 25 pesos,')
    while True:
        orange1 = (input('How many oranges do you want to buy? '))
        if orange1.isalpha():
            print('Only input numeral characters.')
        elif orange1.isdigit():
            break
    apple2 = int(apple1)
    orange2 = int(orange1)
    totalAmount2 = apple2*20 + orange2*25
    return totalAmount2

def display(totalAmount1):
    print(f'The total amount is {totalAmount1} pesos.')


#TOTALAMOUNT FUNTION
#Request input for the number of apples to be bought.
#Request input for the number of oranges to be bought.
#Calculates the total price.
totalAmount = appleOrangeTotal()

#DISPLAY FUNCTION
#Displays the total amount.
display(totalAmount)





