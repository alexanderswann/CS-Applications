#boolean practice
#tax bracket

income = 500000

if income >= 0 and income <= 9525:
    tax=.10*income

if income >= 9526 and income <= 38700:
    tax=952.50 + .12*(income - 9525)

if income >= 38701 and income <= 82500:
    tax= 4453.50 + .22*(income - 38700)

if income > 82501:
    tax= 14089.50 + .24*(income - 82500)

print ('tax is $' + str(tax))
