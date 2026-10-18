class BankAccount:
    
    def __init__(self,owner,account_number , balance , transactions):
        
        
        self.sahebe_hesab = owner
        self.shomare_hesab = account_number
        self.balance = balance
        self.sum_daily_withdraw = 0
        self.transactions = transactions or []
        self.minimum_balance = 50000
        self.karmozd = 0.01 
        self.maximum_deposit = 100000000
        self.currency = 'toman'
        self.show_balance_karmozd = 1000
        self.maximum_withdraw_at_once = 500000
        self.maximum_sum_withdraw = 10000000
        
    def __str__(self):
        return (f"{self.sahebe_hesab},{self.shomare_hesab},{self.balance},{self.transactions}")
        
   
    def deposit(self,amount=0):
        
        if amount <0:
            raise ValueError('meghdar nemitavand manfi bashad')
            
        elif amount > self.maximum_deposit:
            raise ValueError('shoma be saghfe variz khordid')
            
            
        self.balance = self.balance + amount 
        
        
        self.transactions.append(f'+ {amount}')
        
        print('ba moafaghita anjam shod')
        print('mojodie shoma :',self.balance)
    
    
    
    def withdraw(self,amount=0):
        
        if amount < 0:
            raise ValueError('amount mitavanad fght mosbat bashad')
        
        elif amount + self.karmozd * amount +self.minimum_balance > self.balance :
            raise ValueError('Mojodi kafi nemibashad')
        
        
        elif amount > self.maximum_withdraw_at_once:
            raise ValueError('shoma ejaze ye bardahst bish az 50000 nadarid')
            
        elif self.sum_daily_withdraw + amount > self.maximum_sum_withdraw:
            raise ValueError('shoma be saghfe bardashte roozane rresidi')
            
            
        self.balance = self.balance - amount - self.karmozd * amount
        
        
        self.sum_daily_withdraw = self.sum_daily_withdraw  + amount +  self.karmozd * amount
        
        
        self.transactions.append(f'- {amount}')
        
        print('ba moafaghita anjam shod')
        print('mojodie shoma :',self.balance)
     
        
    
    def transfer(self, amount, destination_account):
        
        destination_account.deposit(amount)
        self.withdraw(amount)
    
    def show_balance(self):
        if self.balance < self.show_balance_karmozd + self.minimum_balance:
            raise ValueError('Mojodie moshahedeye mojodi kafi nist')
            
            
        self.balance = self.balance - self.show_balance_karmozd
        
        print('balance shoma hast :' , self.balance)
        
    def transaction_history(self):
        
            requested_transactions = self.transactions
        
            for transact in requested_transactions:
                
                if transact[0] == '-':
                    print(f'Bardasht {transact}')
                    
                    
                else:
                    print(f'Variz {transact}')
                    
            
        
                
        

