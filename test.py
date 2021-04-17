from Budget import Budget
from time import time


'''
Creating an object of class
'''

food = Budget('Food')
clothing = Budget('Clothing')
entertainment =  Budget('Entertainment')


# food.deposit(int(input('Enter an amount  ')), str(input('Enter your description')))
food.deposit(9000, 'kdkjakj;kaof')
food.withdraw(1000, 'for food')
# food.transfer()
# food.getDetails()

clothing.deposit(10000, 'Christmas cloth')
clothing.withdraw(30000, 'for food')



print(f'You total balance is  {food.getDetails()} for  food category')
print(f'You total balance is  {clothing.getDetails()} for  clothing category')
