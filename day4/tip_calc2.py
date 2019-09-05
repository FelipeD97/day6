bill = float(input('Total bill amount? '))
service = input('Level of service? ')
people = int(input('Split how many ways? '))
if service == 'good':
    print('Tip amount: ' + str('$%.2f' % (0.20 * bill)))
    print('Total amount: ' + str('$%.2f' % (bill + (0.20 * bill))))
    print('Amount per person: ' + str('$%.2f' % ((bill + (0.20 * bill)) / people)))
elif service == 'fair':
    print('Tip amount: ' + str('$%.2f' % (0.15 * bill)))
    print('Total amount: ' + str('$%.2f' % (bill + (0.15 * bill))))
    print('Amount per person: ' + str('$%.2f' % ((bill + (0.15 * bill)) / people)))
elif service == 'bad':
    print('Tip amount: ' + str('$%.2f' % (0.10 * bill)))
    print('Total amount: ' + str('$%.2f' % (bill + (0.10 * bill))))
    print('Amount per person: ' + str('$%.2f' % ((bill + (0.10 * bill)) / people)))