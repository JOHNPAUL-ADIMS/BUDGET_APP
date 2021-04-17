class Budget:
    
    """
    A BUDGET APP by JohnPaul Adimonyemma
    #This  contains a database for storing the information of the clients

    First one is am int, while the last one is a string
    """

    def __init__(self,category):
        self.category = category
        self.database = [

        ]

    def deposit(self, amount, description=""):

        '''
        Deposit money to the budget created
        Amount =  Deposit an amount 
        Description = Write why you are depositing 
        '''
        self.database.append({"amount": amount, "description": description})

    def withdraw(self, amount, description):
        self.database.append({"amount": -amount, "description": description})
        

    def transfer(self, amount, budgetCategory):
        self.withdraw(amount, f"Transfer to {budgetCategory.name}")
        budgetCategory.deposit(amount, f'Transfered from {self.name}')
    
    def getBalance(self):
        return  self.database

    def getDetails(self):
        total = 0
        for item in self.database:
            total += item['amount']
        return total
