# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 08:15:23 2022

@author: Ahmad Lutfi 

this version is prefered, to continue to work on, & further develop: 
    it recognizes the
    1 bank as a credit account 
    2 cash as a Debit accound 
    *(other minor issues may exist, accordingly)* 
    
"""
import numpy as np
"""
from datetime import date, time, timedelta  # fixes
from pytz import timezone
import pytz
from time import strftime, gmtime, localtime
import datetime as dt
from enum import Enum  # , unique

import time
import logging 
"""
intCounter = 0 # experimental: an auto-Increment feature for an account 


"""
let's define when an amoount is considered `Invalid`. In python we can initialy 
think of at least `3 ` conditions that make an amount `Invalid`, which are:
    1. amount is Nullable (Nil, or None)
    2. amount 
    3. amount is Negative 
    
    Note: A transaction can be `negative`, of course, as a normal form of balancing
    things between accounts.
    However, an amount can Never be Negative, itself.
    

"""
# @unique
class Account:
 #   id
 #   Name
    # pass
    #The following Naming attributes solves "inherited child does not have this attribute" AttributeError   
    Dr = None
    Cr = None
    
    amountIsNullable =  lambda _ : _ == None 
    amountIsEmptyString = lambda _  : _ == ""
    amountIsNegative = lambda _ : _ < 0.0 

   # total

    def __init__(self, Name="N/A", total=0.0):

        self.Name = Name
        #self.Dr = None
        #self.Cr = None
        self.total = np.round(total, 2)

    """
    def __init__(self):
        self.id == None

        self.Name = "N/A"
        self.Dr = None
        self.Cr = None
        self.total = np.round(0.0, 2)

    
    def __init__(self, Counter=intCounter):
        if self.id == None:
            self.id = Counter
            self.Name = "N/A"
            self.Dr = None
            self.Cr = None
            self.total = np.round(0.0, 2)


        def __init__(self, Name="N/A"):
    
            self.Name = Name
            self.Dr = None
            self.Cr = None
            self.total = np.round(0.0, 2)
    

    def __init__(self, Name="N/A", Counter=intCounter):
        if self.id == None:
            self.id = Counter
            self.Name = Name
            self.Dr = None
            self.Cr = None
            self.total = np.round(0.0, 2)
  
    def __init__(self, Name="N/A", Counter=intCounter):
        if self.id == None:
            self.id = Counter
            self.Name = Name
            self.Dr = None
            self.Cr = None
            self.total = np.round(0.0, 2)

    def __init__(self, Name="N/A", total=0.0, Counter=intCounter):
        if self.id == None:
            self.id = Counter
            self.Name = Name
            self.Dr = None
            self.Cr = None
            self.total = np.round(total, 2)
    """

    def incrementId(self):

        if self.Id != None:
            self.Id += 1

    """
    def increment(total, amount=0.0):
         tmp = total + amount
         # total += amount
         # Check Failure Condition
         if tmp >= 0 and amount > 0:
             total = tmp
         return total
     """
    def checkAmountValid(amount=0.0): 
        amountIsNullable =  amount == None 
        amountIsEmptyString = amount == ""
        amountIsNegative = amount < 0.0 
        
        if   amountIsNullable or amountIsEmptyString or amountIsNegative: 
            return False
        
        elif not  amountIsNullable and not amountIsEmptyString and not amountIsNegative: # 0 is also a valid number, indeed
            return True #True 
        
        
    def increment(self,amount=0.0):
        """ increments an an account, by a value """
        if not  amount == None and not amount == "" and amount >=0.0: # 0 is also a valid number, indeed
        
            tmp = self.total + amount # store value temprarily 
             # total += amount
             # Check Failure Condition
            if tmp >= 0 and amount > 0:   
                 total = tmp
            return total
    
    def decrement(self, amount=0.0):
        self.total = self.total - amount
        tmp = self.total
        # total -= amount
             # Check Failure Condition
        if amount >= 0:
            total = tmp
        return total

    """
    def decrement(total, amount=0.0):
         tmp = total - amount
         # total -= amount
         # Check Failure Condition
         if tmp >= 0:
             total = tmp
         return total
     """

    # set Credit Debit 
    def setCredit(self):
                self.Cr = 1 
                self.Dr = None
                
    def setDebit(self):
                self.Dr = 1 
                self.Cr = None 
            
    def debit(self,amount):#):
        self.setDebit()
        
        #pass

    def credit(self,amount):  
        self.setCredit()
        #if self.__account 
        # pass
    #TODO: add here

"""The code will do the same thing. This is because in python instance.method(args) 
is just shorthand for Class.method(instance, args). 
If you want use super you need to make sure that you specify object as 
the base class for Person as I have done in my code.

The python documentation has more information about how to use the super keyword. 
The important thing in this case is that it tells python to look for 
the method __init__ in a superclass of self that is not a `DebitAccount`

Note: that if you are using Python 2.x, you must explicitly list object as a base class
of Person in order to use super(). 
Otherwise, you have to use the Account.__init__ form.

docs.python.org/library/functions.html#super indicates that super() is only supported on new-style classes, which in Python 2.x are those that inherit from object
@chepner Thanks. I did not realize python classes do not automatically inherit from a common base class the way they do in Java. I have fixed my code.
"""

class DebitAccount(Account): # inherits Account (corrrect)
    # Enum manipulation
    # Dr = 1 # dr ==1
    # Cr = None
    
        """
        def __init__(self, Name, total):

        #super().__init__(Name=Name, total=total)
        #super(DebitAccount, self).__init__(Name=Name, total=total)
        Account.__init__(Name=Name, total=total)
        self.Dr = 1 
        """
        def __init1__(self, *args, **kwargs): #same 
                #self.website=kwargs.pop('website')
                # the thing Dr is not given directly thru the  parameter
                #  self.Dr=kwargs.pop('Dr') # pop the required attribute 
                
                super(DebitAccount, self).__init__(*args, **kwargs)
                #super().Dr = 1  #N.D
                #self.Cr = 1 # assign it 
                self.Dr = 1 #True #1 # assign it  #N.D   
                self.Cr = None
                #super.Dr = 1
                print("Debit Finished")
                
                
        def __init__(self,Name, total): # same 
        
                
                #super().Dr = 1      #N.D
                super(DebitAccount,self).__init__(Name, total)
                self.Dr = 1        #N.D
                self.Cr = None
            
                print("Debit(2) Finished")
        def setCredit(self):
            self.Cr = 1 
            self.Dr = None
            
        def setDebit(self):
            self.Dr = 1 
            self.Cr = None 

        def credit(self, amount=100): #0.0): # same 
            self.setCredit()
            if self.Cr == 1:
                if amount > 0:
                   # self.cr
                   super(DebitAccount,self).decrement( amount)
                       
                   """
                    if self.Dr == 1:
                        self.decrement(amount)
        
                    elif self.Cr == 1:
                        self.increment(amount)
                    """
        
            else:
                raise Exception("ERROR: `amount` must be positive")

        def debit(self, amount=100): #0.0): # same 
            super().setDebit()
            if self.Dr == 1:  # problem self.Dr == None (not 1 [Expected ])
                if amount > 0:
                        # self.decrement(amount)
                    super(DebitAccount,self).increment( amount) 
                """
                    if self.Cr == 1:
                        self.increment(amount)
                    elif self.Dr == 1:
                        self.decrement(amount)
                """
                
            else:
                raise Exception("ERROR: `amount` must be positive") #<----------
            #else: # 
            #    raise  Exception("ERROR: `amount` must be positive")

        """
        def debit(amount):
           #fetches total, increments it by amount, returns updated total
            tmp = self.total +amount
            if ampunt >0 and tmp>0:
                self.total = tmp
            return self.total
    
    
        def credit(amount):
                #fetches total, decrements it by amount, returns updated total
                # super().debit(amount)
                tmp = self.total - amount
                if ampunt >0 and tmp>0:
                    self.total = tmp
                return self.total
    
        """

        def checkDrCondition(self, amount: float):
    
            if self.Dr == 1:
                # increment , if Dr (Debit)
                #super.increment(self.total, amount)
                super(DebitAccount,self).increment(amount)
    
            elif self.Cr == 1:
                # decrement , if Cr (Credit)
                #super.decrement(self.total, amount)
               super(DebitAccount,self).decrement(amount)
            elif self.Dr == None and self.Cr == None: # (potential 2-faced loophole)
                pass
            else:
                raise Exception(
                    "Unexpected Error Occured , please try again later")

        """
        def __init__(self, amount: float):
            super().__init__(amount)  # call the default function
            checkDrCondition(amount)
       

        def __init__(self, Name: str, total: float):
            super(DebitAccount,self).__init__(Name, total)  # call the default function

        
        def __init__(self, Name="N/A",  amount=0.0):
    
            super().__init__(Name, total, amount)  # call the default function
            checkDrCondition(amount)
    
    
        """

        def increment(self, amount):
            if self.Dr == 1:
    
                # increment , if Cr (Credit)
                super(DebitAccount,self).increment(amount) #<-----------
    
                #     elif Dr  ==1:
                # decrement , if Dr (Debit)
                #        decrement(self.total, amount)
    
            elif self.Dr == None and self.Cr == None:
                pass
    
            else:
                raise Exception(
                    "Unexpected Error Occured , please try again later")
        """
    
        def increment(self, amount=0.0):
            if self.Dr == 1:
                #super.increment(self.total, amount)
                super.increment(amount)
    
        def decrement(self, amount=0.0):
            if.:
                # super.decrement(self.total, amount)
                super.decrement(amount)
    
        """
        
        def decrement(self, amount):
            if self.Cr == 1:
    
                # increment , if Cr (Credit)
                
                super(DebitAccount,self).decrement(self.total, amount)
    
                #     elif Dr  ==1:
                # decrement , if Dr (Debit)
                #        decrement(self.total, amount)
    
            #Evaluate the passing condition (both bool flags are equal to None )
            elif self.Dr == None and self.Cr == None:
                pass
            #otherwise, something unexpected Occured
            else:
                raise Exception(
                    "Unexpected Error Occured , please try again later")


class CreditAccount(Account): #, Enum):
    # Enum manipulation
    #   Cr = 1
    #   Dr = None
    #""
    def __init__(self, *args, **kwargs):
            #self.website=kwargs.pop('website')
            # the thing Dr is not given directly thru the  parameter
            #  self.Dr=kwargs.pop('Dr') # pop the required attribute 
            super(CreditAccount, self).__init__(*args, **kwargs)
            #self.Cr = 1 # assign it 
            self.Cr = 1 #True #1 # assign it 
            #super.Dr = 1
            print("Credit Finished")
            
    def __init(self, Name, total):
            super(CreditAccount,self).__init__(Name, total)
            
    #Domain functions: 
        
    def checkCrCondition(self, amount: float):
        #if Dr value is set to 1 
        if self.Dr == 1:
            # increment , if Dr (Debit)
            #super.increment(self.total, amount)
            super(CreditAccount,self).decrement(amount)

        elif self.Cr == 1:
            # decrement , if Cr (Credit)
            #super.decrement(self.total, amount)
            super(CreditAccount,self).increment(amount)
        elif self.Dr == None and self.Cr == None:
            pass
        else:
            raise Exception(
                "Unexpected Error Occured , please try again later")
            

    def credit(self, amount=100): #0.0):
        if self.Cr == 1:
            if amount > 0:
                   # self.cr
                   super(CreditAccount,self).increment( amount)
                       
                   """
                    if self.Dr == 1:
                        self.decrement(amount)
        
                    elif self.Cr == 1:
                        self.increment(amount)
                    """
        
            else:
                raise Exception("ERROR: `amount` must be positive")

    def debit(self, amount=100): #0.0):
        if self.Dr == 1:
            if amount > 0:
                # self.decrement(amount)
                super(CreditAccount,self).decrement( amount)
                """
                    if self.Cr == 1:
                        self.increment(amount)
                    elif self.Dr == 1:
                        self.decrement(amount)
                """
        else:
            raise Exception("ERROR: `amount` must be positive")

    #The end # Correct function implementation 

#Credit Accounts 
# Liability : CreditAccount 
class Liability(CreditAccount): 
    
    def __init__(self, Name, total):
        super(Liability,self).__init__(Name, total)
        self.tag = "Liability"
    
# Revenue [Statement of Comprehensive Income (SOCI ) object ]
class  Revenue(CreditAccount):
    
    def __init__(self, Name, total):
        super(Revenue,self).__init__(Name, total)
        self.tag = "Revenue"
        
# Debit Accounts
# Idea to ponder Upon (Meditate): notice the opposing force, between the `Asset` & the `Expense`,
# despite both of them derived being of the same type, `DebitAccount`, each 
# has it's own behavior. for the `Asset` * acts as a **Resource**, displays a `Value Storing Behavior` that is able to store Value *
# it is a viable object, belongs to the `Balance Sheet` account object, essential to be tracked, every month
# Meanwhile, the Expense Account , shows a `Value Outflow Behavior`, hence displaying a behavior of value spent 
# on exogeneous entities 
# Expense has a direct relationship with an `Accrued Expense` account, which, in turns , has a direct relationship with 
 
## Asset : DebitAccount
class Asset(DebitAccount):
    """ an asset, is an object, that stores value , at a given period of time """ 
    
    def __init__(self, Name, total):
        super(Asset,self).__init__(Name, total)
        self.tag = "Asset"
 
##  Expense : DebitAccount 

class  Expense(DebitAccount):
    """ an Expense shows a `Value Outflow` of an account, for a given period of time """ 
    
    def __init__(self, Name, total):
        super(Expense,self).__init__(Name, total)
        self.tag = "Expense"
 
# Experimental part - transaction 

class transaction():
    """set dr for debit side, cr for cr side , then nullify flags after transaction's finished """ 
    
    def __init__(self, Acc1: Account, Acc2: Account, amount: float):
        # Assignment
        self.firstAccount = Acc1
        self.secondAccount = Acc2         
        # q. do we need enforce a decorator or wrapper?
        # Condition check
        self.amount = round(amount, 2)
        # DebitAccount.Dr = 1 and CreditAccount == 1 
        #TODO: Specify all possible combination of Accounts 
        
        if Acc1.Dr == 1 and Acc2.Cr == 1: #<-----------
            Acc1.__class__ = DebitAccount(Acc1.Name, Acc1.total)
            Acc2.__class__ = CreditAccount(Acc2.Name, Acc2.total)
            print("Transaction:\ntype(Acc1) = ", type(Acc1), " type(Acc2) = ", type(Acc2))

            # Acc1 = (Debit) Acc1
            # Acc2 = (Credit) Acc2

            # self.Acc1 = Acc1
            # self.Acc2 = Acc2
            Acc1.credit(amount)
            Acc2.debit(amount)
            
        elif Acc1.Cr == 1 and Acc2.Dr == 1:

            # Acc2 =(Debit) Acc2
            # Acc1 = (Credit) Acc1

            Acc1.__class__ = CreditAccount(Acc1.Name, Acc1.total)
            Acc2.__class__ = DebitAccount(Acc2.Name, Acc2.total)
            Acc1.debit(amount)
            Acc2.credit(amount)
        """
        elif Acc1.Cr == 1 and Acc2.Cr == 1:

                    # Acc2 =(Debit) Acc2
                    # Acc1 = (Credit) Acc1

                Acc1.__class__ = Credit
                Acc2.__class__ = Credit
        
        elif Acc1.Dr == 1 and Acc2.Dr == 1:

                # Acc2 =(Debit) Acc2
                #Acc1 = (Credit) Acc1
    
                Acc1.__class__ = Debit
                Acc2.__class__ = Debit
        """
        print("type(Acc1) = ", type(Acc1), "type(Acc2) = ", type(Acc2))
        self.Acc1 = Acc1
        self.Acc2 = Acc2
        
#initialize Account 
# Compiles
#Transaction simulation:  
# 1 Transaction of Incrementation:
    
cash = DebitAccount("cash", 1000) #DebitAccount  # correcrt #comment: increments a debitAccount, `Asset` ,  `cash`, 
bank = CreditAccount("bank", 1000) #CreditAccount # correct #comment: increments a creditAccount, `Asset` ,  `cash`, 

#_dr(bank,100)
#_cr(cash,100)
print("cash = ",cash)
print("bank = ", bank)

print("cash.total = ",cash.total, " bank.total = ",bank.total)

# returns type(Acc1) =  <class 'enum.EnumMeta'> type(Acc2) =  <class 'enum.EnumMeta'>
transaction(DebitAccount, CreditAccount, 100) #Transaction(Account1, Account2 , amount)

print("cash.total = ",cash.total, " bank.total = ",bank.total)


#Increment 
## try 1 : (not functioning) #TODO
print("try 1:")
cash.debit(100) 
bank.credit(100)

print("cash's total = ",cash.total)
print("Bank's total = ",bank.total)


## try 2 : (not functioning) # TODO 
print("try 2:")
cash.increment(100)
bank.increment(100)

print("cash's total = ",cash.total)
print("Bank's total = ",bank.total)
