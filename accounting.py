# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 08:15:23 2022

@author: Ahmad Lutfi 

this version is prefered, to continue to work on, & further develop: 
    it recognizes the
    1 bank as a credit account 
    2 cash as a Debit accound 
    *(other minor issues may exist, accordingly)* 
    
    3 account transaction is functioning as expected
    (Correction: transation returns total instead of self.total)
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
intCounter = 0  # experimental: an auto-Increment feature for an account


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
# Static Functions

#================================================================================
# Amount Functions


def amountIsNullable(amount):
    """ amount value is Truly nullable if its value is equal to None, 
    otherwise it is definitely Not """
    if amount == None:
        return True
    elif amount != None:
        return False


def amountIsEmptyString(amount):
    if amount == "":
        return True
    elif amount != "":
        return False


def amountIsNegative(amount):
    if amount < 0:
        return True
    elif amount >= 0:
        return False


def amountIsPositive(amount):
    if amount >= 0:
        return True
    elif amount < 0:
        return False

#   def amountIsNegative(amount):

#      return  amount < 0


print("Is `None` Nullable? ", amountIsNullable(None))  # True


#===============================================================================
# AccountTypeCheck

    # valid
def notNullorEmptyPositive(amount):
    if not amountIsNullable(amount) and not amountIsEmptyString(amount) and not amountIsNegative(amount):
        return True
    elif amountIsNullable(amount) or amountIsEmptyString(amount) or amountIsNegative(amount):
        return False

    #Invalid
def NullorEmptyorNegative(amount):
    if amountIsNullable(amount) or amountIsEmptyString(amount) or amountIsNegative(amount):
        return True

    elif not amountIsNullable(amount) and not amountIsEmptyString(amount) and not amountIsNegative(amount):
        return False

#===============================================================================
# Account Class 


class Account:
    """
        an account class 
         any account can be 
         1. stateful: when value flows (from an account, in-flow our out of account , out-flow )
         two states:
             1. Debit
             2. Credit 
             
         1.1. debited (Dr)
 
         1.2. Credited (Cr)


        2. stateless:
            has a reset feature
            it has to be called, after each transaction
            
        after each transaction, the account returns back to its natural state of being 
        Into a state of `None`
        
       Note: the intent of this behavior is that 
        the account would only behave in an expected manner :
            when there is a flow: then it's either a debit 
        
        
        
    """

    # pass
    # The following Naming attributes solves "inherited child does not have this attribute" AttributeError
    # iniitally, an account has as neutral Nullable state (Dr or Cr) set 
   
    # stateful-actions:
    Dr = None
    Cr = None
    
    #state-less action 
    def resetAccountState(self):
        """
        after having an action, account, should return to `None`

        Returns
        -------
        None.

        """
        self.Dr = None
        self.Cr = None 
        
    def __init__(self, Name="N/A", total=0.0 ):
        
        """

        Parameters
        ----------
        Name : TYPE, optional
            the Account's Name . The default is "N/A".
            
            
        total : TYPE, optional
            the Account's value. The default is 0.0 : float.

        Returns
        -------
        None. # TODO: return an inflow (or outflow), or None 

        """

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
    #depreciate 
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

    # amount condition specification

    # amount Is Negative
    """ #applying deMorgans law for logic (and ->or , or -> and) (inverting and to or, not or without (to be or not to be ))"""
    
    def calcFlow(self,amount, operator):
        if operator == self.Cr:
            pass
            #check accountType 
        elif operator == self.Dr:
            pass 
        elif operator == None :
            pass 
        
    def amountIsNegative(amount):
        # NullorEmptyorNegative(amount) or amountIsEmptyString(amount) or amountIsNegative(amount): #amountIsNullable or amountIsEmptyString or amountIsNegative:
        if NullorEmptyorNegative(amount):
            return True
        # not NullorEmptyorNegative(amount): #  amountIsNullable(amount) and not amountIsEmptyString(amount) and not amountIsNegative(amount):
        elif notNullorEmptyPositive(amount):
            return False

    # amount Is Negative

    def checkAmountIsValid(amount):
        # not  amountIsNullable(amount) and not amountIsEmptyString(amount) and not amountIsNegative(amount):
        if notNullorEmptyPositive(amount):
            return True

        # NullorEmptyorNegative(amount): #amountIsNullable(amount) or amountIsEmptyString(amount) or NullorEmptyorNegative(amount):   #amountIsNullable or  amountIsEmptyString or  amountIsNegative:
        elif NullorEmptyorNegative(amount):
            return False

    def amountIsPositive(amount=0.0):
        # amountIsNullable(amount) and  amountIsEmptyString(amount) and  amountIsNegative(amount) = amount < 0.0 :
        if amountIsPositive(amount):
            # = amount == "" # =  if amount == None
            return True
        elif not amount < 0:  # amountIsPositive(amount): #<0 :
            return False

        # amountIsNullable or amountIsEmptyString or amountIsNegative:
        elif amountIsNegative(amount):
            return False

      #  elif not  amountIsNullable and not amountIsEmptyString and not amountIsNegative: # 0 is also a valid number, indeed
        #    return True #True
        else:
            raise Exception("an unknown error Occured ")

    def increment(self, amount=0.0):
        """ increments an an account, by a value """
        # if not  amount == None and not amount == "" and amount >=0.0: # 0 is also a valid number, indeed
        total = 0.0
        
        # 1 check amount not amountIsNullable(amount) and not amountIsEmptyString(amount) and :
        if notNullorEmptyPositive(amount):

            tmp = self.total + amount  # store value temprarily
            # total += amount
            # Check Failure Condition
            if tmp >= 0:  # and amount > 0: # amount already is positive
                self.total = tmp
        return total

    def decrement(self, amount=0.0):
        """ decrements an amount, by a value """
        total = 0.0

        if notNullorEmptyPositive(amount):

            self.total = self.total - amount
            tmp = self.total
            # total -= amount
            # Check Failure Condition
            if amount >= 0:
                self.total = tmp
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

    def debit(self, amount):  # ):
        self.setDebit()

        # pass

    def credit(self, amount):
        self.setCredit()
        # if self.__account
        # pass
    # TODO: add here


"""stackoverflow 
The inheritance of attributes using __init__
https://stackoverflow.com/questions/8853966/the-inheritance-of-attributes-using-init

The code will do the same thing. This is because in python `instance.method(args)`
is just shorthand for Class.method(instance, args). 
If you want use super you need to make sure that you specify object as 
    `the base class for Person as I have done in my code.`

The python documentation has more information about how to use the super keyword. 
The important thing in this case is that it tells python to look for 
the method __init__ in a superclass of self that is not a `DebitAccount`

Note: that if you are using `Python 2.x`, you must explicitly list object as a `base class`
of Person in order to use `super()`
Otherwise, you have to use the Account.__init__ form.

docs.python.org/library/functions.html#super indicates that super() is only supported on new-style classes, which in Python 2.x are those that inherit from object
`@chepner` Thanks. I did not realize 
  *`python classes do not automatically inherit from a common base class` the way they do in Java. I have fixed my code.*
"""


class DebitAccount(Account):  # inherits Account (corrrect)
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
    """
    def __init1__(self, *args, **kwargs):  # same
        # self.website=kwargs.pop('website')
        # the thing Dr is not given directly thru the  parameter
        #  self.Dr=kwargs.pop('Dr') # pop the required attribute
        
        
        super(DebitAccount, self).__init__(*args, **kwargs)
        # super().Dr = 1  #N.D
        # self.Cr = 1 # assign it
       # self.Dr = 1  # True #1 # assign it  #N.D
        #self.Cr = None
        #super.Dr = 1
        print("Debit Finished")
    """
    
    def __init__(self, Name, total):  # same

        # super().Dr = 1      #N.D
        super(DebitAccount, self).__init__(Name, total) # sets account w
      #  self.Dr = 1  # N.D
      #  self.Cr = None
        self.setDebit() # sets account to be a DebitAccount 

        print("Debit(2) Finished")

        #now reset account's state
        self.resetAccountState()
        
    def setCredit(self):
        self.Cr = 1
        self.Dr = None

    def setDebit(self):
        self.Dr = 1
        self.Cr = None
        
    
    def finalize(self):
        self.resetAccountState()
       
    def calculateFlow(self,amount): #  se:
        # 1 checks if amount is valid 
            self.checkAmountIsValid(amount)
                
            #TODO: 
                
       #self.total -  
        #pass
        
    
    # Stateful- Actions: debit , credit     
    
    def credit(self, amount=100):  # 0.0): # same
       
        self.calculateFlow(amount) # TODO <---------
        
        self.setCredit()    # set a credit state 
        if self.Cr == 1: # checks if credit operation 
            #if amount > 0:
                # self.cr
            super(DebitAccount, self).decrement(amount)
            self.resetAccountState()
            
            """
                    if self.Dr == 1:
                        self.decrement(amount)
        
                    elif self.Cr == 1:
                        self.increment(amount)
                    """

        else:
            raise Exception("ERROR: `amount` must be positive")

    def debit(self, amount=100):  # 0.0): # same
        super().setDebit()
        if self.Dr == 1:  # problem self.Dr == None (not 1 [Expected ])
            if amount > 0:
                # self.decrement(amount)
                super(DebitAccount, self).increment(amount)
                self.resetAccountState()
            """
                    if self.Cr == 1:
                        self.increment(amount)
                    elif self.Dr == 1:
                        self.decrement(amount)
                """

        else:
            raise Exception("ERROR: `amount` must be positive")  # <----------
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
        """checks current Dr Condition """ 
        
        if self.Dr == 1:
            # increment , if Dr (Debit)
            #super.increment(self.total, amount)
            super(DebitAccount, self).increment(amount)
            
            self.finalize()
        elif self.Cr == 1:
            # decrement , if Cr (Credit)
            #super.decrement(self.total, amount)
            super(DebitAccount, self).decrement(amount)
            self.finalize()
            
        # (potential 2-faced loophole)
        elif self.Dr == None and self.Cr == None:
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
        """
            increments by an amount 

        Parameters
        ----------
        amount : float 
            DESCRIPTION.

        Raises
        ------
        Exception
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if self.Dr == 1:

            # increment , if Cr (Credit)
            super(DebitAccount, self).increment(amount)  # <-----------

            #     elif Dr  ==1:
            # decrement , if Dr (Debit)
            #        decrement(self.total, amount)

        #Otherwise, if nothing is set, then do Nothing
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

            super(DebitAccount, self).decrement(self.total, amount)

            #     elif Dr  ==1:
            # decrement , if Dr (Debit)
            #        decrement(self.total, amount)

        # Evaluate the passing condition (both bool flags are equal to None )
        elif self.Dr == None and self.Cr == None:
            pass
        # otherwise, something unexpected Occured
        else:
            raise Exception(
                "Unexpected Error Occured , please try again later")

# ==============================================================================


class CreditAccount(Account):  # , Enum):
    # Enum manipulation
    #   Cr = 1
    #   Dr = None
    # ""
    def __init__(self, *args, **kwargs):
        # self.website=kwargs.pop('website')
        # the thing Dr is not given directly thru the  parameter
        #  self.Dr=kwargs.pop('Dr') # pop the required attribute
       
        super(CreditAccount, self).__init__(*args, **kwargs)
        self.resetAccountState()
        # self.Cr = 1 # assign it
        #self.Cr = 1  # True #1 # assign it
        #super.Dr = 1
        print("Credit Finished")

    def __init(self, Name, total):
        super(CreditAccount, self).__init__(Name, total)

    # Domain functions:

    def checkCrCondition(self, amount: float):
        # if Dr value is set to 1
        if self.Dr == 1:
            # increment , if Dr (Debit)
            #super.increment(self.total, amount)
            super(CreditAccount, self).decrement(amount) # Account decrements
            self.resetAccountState() # followed by a reset state, back to `None`
        elif self.Cr == 1:
            # decrement , if Cr (Credit)
            #super.decrement(self.total, amount)
            super(CreditAccount, self).increment(amount)
            self.resetAccountState() # followed by a reset state, back to `None`
        elif self.Dr == None and self.Cr == None:
            pass
        else:
            raise Exception(
                "Unexpected Error Occured , please try again later")

    def credit(self, amount=100):  # 0.0): # # cr CreditAccount [+] 
        if self.Cr == 1: # 
            if amount > 0:
                # self.cr
                super(CreditAccount, self).increment(amount)
                self.resetAccountState() # reset state, back to `None`
                """
                    if self.Dr == 1:
                        self.decrement(amount)
        
                    elif self.Cr == 1:
                        self.increment(amount)
                    """

            else:
                raise Exception("ERROR: `amount` must be positive")

    def debit(self, amount=100):  # 0.0): # dr CreditAccount [-] 
        if self.Dr == 1:
            if amount > 0:
                # self.decrement(amount)
                super(CreditAccount, self).decrement(amount)
                self.resetAccountState() # reset state
                """
                    if self.Cr == 1:
                        self.increment(amount)
                    elif self.Dr == 1:
                        self.decrement(amount)
                """
        else:
            raise Exception("ERROR: `amount` must be positive")

    # The end # Correct function implementation


# Credit Accounts
# Liability : CreditAccount
class Liability(CreditAccount):

    def __init__(self, Name, total):
        super(Liability, self).__init__(Name, total)
        self.tag = "Liability"

# ===============================================================================

# Revenue [Statement of Comprehensive Income (SOCI ) object ]


class Revenue(CreditAccount):

    def __init__(self, Name, total):
        super(Revenue, self).__init__(Name, total)
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
        super(Asset, self).__init__(Name, total)
        self.tag = "Asset"

##  Expense : DebitAccount


class Expense(DebitAccount):
    """ an Expense shows a `Value Outflow` of an account, for a given period of time """

    def __init__(self, Name, total):
        super(Expense, self).__init__(Name, total)
        self.tag = "Expense"

# ==============================================================
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
        # TODO: Specify all possible combination of Accounts

        if Acc1.Dr == 1 and Acc2.Cr == 1:  # <-----------
            Acc1.__class__ = DebitAccount(Acc1.Name, Acc1.total)
            Acc2.__class__ = CreditAccount(Acc2.Name, Acc2.total)
            print("Transaction:\ntype(Acc1) = ", type(
                Acc1), " type(Acc2) = ", type(Acc2))

            # Acc1 = (Debit) Acc1
            # Acc2 = (Credit) Acc2

            # self.Acc1 = Acc1
            # self.Acc2 = Acc2
            Acc1.debit(amount)
            Acc2.credit(amount)
            
            Acc1.credit(amount) # 
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

# initialize Account
# Compiles
# Transaction simulation:
    """the following simulates a Transaction with:
    A DebitAccount (Cash) [Tangible: Phyiscal, also, real ]
    
    A CreditAccount(Bank) [InTangible: non-Physical, abstract]
note: this transacrtion increases both sides 
can call it by an `Incremental Transaction`
Rationale: increases both sides: `cash` & `Bank` (by 1000)
where, both accounts increase, in value 

<there is an in-flow: on both sides> 
Recall: DebitAccount increases by Debit(Dr operator)
      CreditAccount increases by Credit(cr operator)
        
=============================================== 
    Dr Cash 1000 
            Cr Bank  1000
===============================================            
footnote: cash increases +1000 , Bank Increases +1000 
both transactions 
[Asset] (on Right Side) = [Capital] CreditAccount (on LeftSide )

"""
# 1 Transaction of Incrementation:

# DebitAccount  # correcrt #comment: increments a debitAccount, `DebitAccount` ,  `cash`,
cash = DebitAccount("cash", 1000)
# CreditAccount # correct #comment: increments a creditAccount, `CreduitAccount` ,  `bank`,
bank = CreditAccount("bank", 1000)
#===============================================    

# _dr(bank,100)
# _cr(cash,100)
print("cash = ", cash)
print("bank = ", bank)

print("cash.total = ", cash.total, " bank.total = ", bank.total)

# returns type(Acc1) =  <class 'enum.EnumMeta'> type(Acc2) =  <class 'enum.EnumMeta'>
# Transaction(Account1, Account2 , amount)
transaction(DebitAccount, CreditAccount, 100)

print("cash.total = ", cash.total, " bank.total = ", bank.total)


# Increment
# try 1 : ( functioning)
print("try 1:")
cash.debit(100)
bank.credit(100)

print("cash's total = ", cash.total)
print("Bank's total = ", bank.total)


# try 2 : ( functioning)
print("try 2:")
cash.increment(100)
bank.increment(100)

print("cash's total = ", cash.total)
print("Bank's total = ", bank.total)


"""pip's Debt is am expense for pip i.e. he has topay for it  ( in turn of serice rendered i.e. the liquor at 
Barnett's Inn)

mean While Barnett's Inn is the Account Payable'
it is a liability on pip, it surely is , thus it's a Liability Account 
(Liability is an account of burden on the account owner, that sooner pr later pip has to pay back 
 )
timing: there are 2 types of a Liability : 
    
    Short-Term : within 1 year (this account belings to, as it's of a small sum, for the dew beers offered )
    Long-Term Liability : returnable  with a period of more than 1 year 
    
    
    Liabilities normally have a `fee` (for carrying the liability)
    (in which is a crucial feature: has to be fulfilled  #TODO ) 
    
"""
#----------------

# Transaction 1 : pip writes down Debt of 100 shillings to barrerttInn (creditAccount )
#Instantiate  DebitAccount 100 (pip's Debt) amount pip should pay 
#instantiate a CreditAccount 100 barnettInn's Inn 100 

pipDebt = DebitAccount("pip's Debt", 100)
barnettInn = CreditAccount("Barnett's Inn", 100)

#------------------
#pip lower down his debt, by paying it back to barnettInn , say for the same starting amount, 100 

#pip pays off his amount 

#transaction   1: 
#an in-flow to barnettInn of (100 ) shillings matches up with an out-flow of a 
barnettInn.debit(100) # closing account for Mr. Pip
pipDebt.credit(100) # 


# Adding a debt Account for Mr. Herbert
herbertDebt = DebitAccount("Herbert's Debt", 100)
barnettInn = CreditAccount("Barnett's Inn", 100)

#now, Mr. Herbert had fallen int some issues, & is unable to pay
# for helping a friend out, Mr. pip steps in & offers barnettInn to pay for herbert's Debt

"""
#what can barnettInn do , in this case?
first, they have to close the account for `Mr. Herbert`
(the only way to fully close the (liability) account is to set to back to 0 
but to do that , they have 'somehow' to transform the Burden (liability) to his friend 
Mr. pip )

thus, lowering down Mr.Herbert, & increasing the Liability, again, for pious `Mr. Pip`

recall, increasing a Debit account is by debiting it, 
increasing a Credit Account is by crediting it 
(just remember, like attracts like)
"""
#1 barnettInn has to `close` herbertDebt & transform Liability to `Mr. Pip`

# closing Herbert Debt: 

barnettInn.debit(100) # closing the account in barnett's Inn book, as well 
herbertDebt.credit(100) # his account goes back to 0 [ as cr debitAccount(100) = -1 * 100]

# note: the two sided accounting formula makes everything in the clear `somehow`
# it has been constructed to be like this, in such a way, no tampering could exist 
# as a lie is easily detectable, by only checking whether the sums of 2 equations 
# are equal (or not)
"""
Now, BarnettInn has closed the account, but they are yet to recieve a (100 ) from Mr.pip

to completely transfer liability, 
Barnett Inn's has  to open up Mr.pip's Debt account again : 
    [as if pip was he ower]
  
dr pip's Debt 100 
    cr barnettIn 100 

"""
# debit 
# credit 

# pipDebt.Dr(100)
# barnettInn.Cr(100)

pipDebt.debit(100)
barnettInn.credit(100)


"""  
# this ends the transfer of liability 

Finally, now the manager at barnett Inn could ask Mr. Pip to finally pay his dues
-"that'll be a 100, alright, sir"
-" with pleasure "

To reiterate, Mr. Pip pays off the manager his now dues, a 100, Manager recieves the sum 
& closes pip's Debt Account , accordingly

"""


# barnettInn.Dr(100) 
# pipDebt.cr(100)

barnettInn.debit(100)
pipDebt.credit(100)




