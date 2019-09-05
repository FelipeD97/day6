bill = float(input('Total bill amount? '))
service = input('Level of service? ')
if service == 'good':
    print('Tip amount: ' + str('$%.2f' % (0.20 * bill)))
    print('Total amount: ' + str('$%.2f' % (bill + (0.20 * bill))))
elif service == 'fair':
    print('Tip amount: ' + str('$%.2f' % (0.15 * bill)))
    print('Total amount: ' + str('$%.2f' % (bill + (0.15 * bill))))
elif service == 'bad':
    print('Tip amount: ' + str('$%.2f' % (0.10 * bill)))
    print('Total amount: ' + str('$%.2f' % (bill + (0.10 * bill))))
