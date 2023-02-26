# -*- coding: utf-8 -*-
"""
Created on Sun Aug 7 08:15:23 2022

@author: Ahmad Lutfi 

this version is prefered, to continue to work on, & further develop: 
    it recognizes the
    1 bank as a credit account 
    2 cash as a Debit accound 
    *(other minor issues may exist, accordingly)* 
    
    3 account transaction is functioning as expected
    (Correction: transation returns totalBalance instead of self.totalBalance)
"""
import copy
#from Date import relativedelta, date
import numpy as np
#from math import *
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
# Static variables
msg = "ERROR! Unexpected Value Occured "

# class Account:
#    pass


# Static Functions

# ================================================================================
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


def amountIsValid(amount):
    if amountIsPositive(amount) and not amountIsEmptyString(amount) and not amountIsNullable(amount):
        return True
    elif  \
            amountIsNegative(amount) or amountIsEmptyString(amount) or amountIsNullable(amount):
        return False
    else:
        raise Exception("unexpected Error Occured")


#   def amountIsNegative(amount):

#      return  amount < 0


print("Is `None` Nullable? ", amountIsNullable(None))  # True


# ===============================================================================
# AccountTypeCheck

# valid
def notNullorEmptyPositive(amount):
    if not amountIsNullable(amount) and not amountIsEmptyString(amount) and not amountIsNegative(amount):
        return True
    elif amountIsNullable(amount) or amountIsEmptyString(amount) or amountIsNegative(amount):
        return False

    # Invalid


def NullorEmptyorNegative(amount):
    if amountIsNullable(amount) or amountIsEmptyString(amount) or amountIsNegative(amount):
        return True

    elif not amountIsNullable(amount) and not amountIsEmptyString(amount) and not amountIsNegative(amount):
        return False

# ===============================================================================


def calcDifference(_first, _second):

    return max(_first, _second) - min(_first, _second)

# ===============================================================================
# Account Class


# debugged

# static methods


def increment(totalBalance, amount):  # now works
    """ increments an an account totalBalance balance , by a value equal to an amount """
    # if not  amount == None and not amount == "" and amount >=0.0: # 0 is also a valid number, indeed
    #totalBalance = 0.0

    # 1 check amount not amountIsNullable(amount) and not amountIsEmptyString(amount) and :
    # if notNullorEmptyPositive(amount):

    inflow = + amount

    tmp = totalBalance + abs(inflow)  # amount  # store value temporarily

    #tmp = totalBalance

    #inflow = abs(amount)

    # totalBalance += amount
    # Check Failure Condition
    if tmp >= 0:  # and amount > 0: # amount already is positive
        totalBalance = tmp

    # instead of totalBalance, should calculate & return the flow (the difference between  totalBalance and new amount)
    return totalBalance
    # return inflow


def decrement(totalBalance, amount):
    """ decrements an amount, by a value """
    #totalBalance = 0.0

    # 1000

    # if notNullorEmptyPositive(amount):
    tmp = totalBalance
    outflow = -  abs(amount)  # always negative

    tmp += outflow  # + outflow #totalBalance + outflow #- amount

    #tmp = totalBalance
    # totalBalance -= amount
    # Check Failure Condition
    if tmp >= 0:  # amount >= 0:
        totalBalance = tmp  # assign tmp to totalBalance

    return totalBalance
    # return outflow

# mini-demo:
tot = 1000
tot = increment(tot, 100)

# hmm this is wrong ! #  100.0  (+1000 = 1100)) #correct
print("increment(100) = ", tot)
tot = decrement(tot, 1100)  # -1100
# mmm it misses a 100 , correctly decrements a 1000, [but misses out on the last 100] #incorrect
print("decrement(1100) = ", tot)

# this is the core issue of this part of program


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

    Hence, we start with 4 flags

    2 Account flags: describe what the account would be about (credit or debit Account)

    2 Transaction flags: describe what transaction, & which part of the accounting equation 
    the account would be at 



    """

    # pass
    # The following Naming attributes solves 
    #"inherited child does not have this attribute" AttributeError
    # initially, an account has as neutral Nullable sateless state `None`
    #or a stateful state (`Dr` or `Cr`) set

    # stateful-actions:
    #Dr = None
    #Cr = None

    drAcc = None
    crAcc = None

    # transaction flags (stateless)
    drTransaction = None
    crTransaction = None

    # state-less action

    def resetAccountState(self):
        """
        after having an action, account, should return to `None`

        Returns
        -------
        None.

        """
        # reset the transaction flags
        self.drTransaction = None
        self.crTransaction = None

        # self.Dr = None
        # self.Cr = None

    def __init__(self, Name="N/A", totalBalance=0.0):
        """

        Parameters
        ----------
        Name : TYPE, optional
            the Account's Name . The default is "N/A".


        totalBalance : TYPE, optional
            the Account's value. The default is 0.0 : float.

        Returns
        -------
        None. # TODO: return an inflow (or outflow), or None 

        """

        self.Name = Name
        #self.Dr = None
        #self.Cr = None
        self.totalBalance = np.round(totalBalance, 2)

    """
    def __init__(self):
        self.id == None

        self.Name = "N/A"
        self.Dr = None
        self.Cr = None
        self.totalBalance = np.round(0.0, 2)

    
    def __init__(self, Counter=intCounter):
        if self.id == None:
            self.id = Counter
            self.Name = "N/A"
            self.Dr = None
            self.Cr = None
            self.totalBalance = np.round(0.0, 2)


        def __init__(self, Name="N/A"):
    
            self.Name = Name
            self.Dr = None
            self.Cr = None
            self.totalBalance = np.round(0.0, 2)
    

    def __init__(self, Name="N/A", Counter=intCounter):
        if self.id == None:
            self.id = Counter
            self.Name = Name
            self.Dr = None
            self.Cr = None
            self.totalBalance = np.round(0.0, 2)
  
    def __init__(self, Name="N/A", Counter=intCounter):
        if self.id == None:
            self.id = Counter
            self.Name = Name
            self.Dr = None
            self.Cr = None
            self.totalBalance = np.round(0.0, 2)

    def __init__(self, Name="N/A", totalBalance=0.0, Counter=intCounter):
        if self.id == None:
            self.id = Counter
            self.Name = Name
            self.Dr = None
            self.Cr = None
            self.totalBalance = np.round(totalBalance, 2)
    """
    # depreciate

    def incrementId(self):

        if self.Id != None:
            self.Id += 1

    """
    def increment(totalBalance, amount=0.0):
         tmp = totalBalance + amount
         # totalBalance += amount
         # Check Failure Condition
         if tmp >= 0 and amount > 0:
             totalBalance = tmp
         return totalBalance
     """

    def isClosed(self):
        balance = copy(self.totalBalance)
        if balance == 0:
            self.AccountClosed = True
            return self.AccountClosed
        elif balance != 0:
            self.AccountClosed = False
            return self.AccountClosed
        else: 
            raise Exception(msg)
        
        
    # amount condition specification

    # amount Is Negative
    """ #applying deMorgans law for logic (and ->or , or -> and) (inverting and to or, not or without (to be or not to be ))"""

    #TODO: fill
    def calcFlow(self, amount, operator):
        if operator == self.crTransaction:  # self.Cr:
            pass
            # check accountType
        elif operator == self.drTransaction:  # self.drAcc: #self.drTransaction:
            pass
        elif operator == None:
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

    def amountIsPositive(amount):
        # amountIsNullable(amount) and  amountIsEmptyString(amount) and  amountIsNegative(amount) = amount < 0.0 :
        if amountIsPositive(amount):
            # = amount == "" # =  if amount == None
            return True
        elif amountIsNegative(amount):  # amountIsPositive(amount): #<0 :
            return False

        # amountIsNullable or amountIsEmptyString or amountIsNegative:
        elif amountIsNegative(amount):
            return False

      #  elif not  amountIsNullable and not amountIsEmptyString and not amountIsNegative: # 0 is also a valid number, indeed
        #    return True #True
        else:
            raise Exception("an unknown error Occured ")

    def increment(self, amount):
        """ increments an an account, by a value """
        # if not  amount == None and not amount == "" and amount >=0.0: # 0 is also a valid number, indeed
        #totalBalance = 0.0

        # 1 check amount not amountIsNullable(amount) and not amountIsEmptyString(amount) and :
        # if notNullorEmptyPositive(amount):
        #inflow = + amount
        # tmp = self.totalBalance + abs( inflow)  # amount  # store value temporarily
        # totalBalance += amount
        # Check Failure Condition
        # if tmp >= 0:  # and amount > 0: # amount already is positive
       #     self.totalBalance = tmp

        inflow = + amount

        # amount  # store value temporarily
        tmp = self.totalBalance + abs(inflow)

        #tmp = totalBalance

        #inflow = abs(amount)

        # totalBalance += amount
        # Check Failure Condition
        if tmp >= 0:  # and amount > 0: # amount already is positive
            self.totalBalance = tmp

            # instead of totalBalance, should calculate & return the flow (the difference between  totalBalance and new amount)
            return self.totalBalance

        # instead of totalBalance, should calculate & return the flow (the difference between  totalBalance and new amount)
        return self.totalBalance
        # return inflow

    def decrement(self, amount):
        """ decrements an amount, by a value """

        #totalBalance = 0.0

        # 1000

        # if notNullorEmptyPositive(amount):
        tmp = self.totalBalance
        outflow = -  abs(amount)  # always negative

        tmp += outflow  # + outflow #totalBalance + outflow #- amount

        #tmp = totalBalance
        # totalBalance -= amount
        # Check Failure Condition
        if tmp >= 0:  # amount >= 0:
            self.totalBalance = tmp  # assign tmp to totalBalance

        return self.totalBalance
        # return outflow
        #totalBalance = 0.0
        """
        #if notNullorEmptyPositive(amount):
        outflow = - abs( amount) #always negative 
        self.totalBalance = self.totalBalance + outflow #- amount
        tmp = self.totalBalance
            # totalBalance -= amount
            # Check Failure Condition
        if amount >= 0:
            self.totalBalance = tmp
        
        return self.totalBalance
        #return outflow
        """

    """
    def decrement(totalBalance, amount=0.0):
         tmp = totalBalance - amount
         # totalBalance -= amount
         # Check Failure Condition
         if tmp >= 0:
             totalBalance = tmp
         return totalBalance
     """

    # set Credit Debit
    def setCredit(self):
        """
        sets the account would be a credit account 

        Returns
        -------
        None.

        """
        #self.Cr = 1
        #self.Dr = None

        self.crTransaction = True  # = 1
        self.drTransaction = None
        #self.crAcc = 1
        #self.drAcc = None

    def setDebit(self):
        """
        sets account would be a debit account 

        Returns
        -------
        None.

        """

        #self.Dr = 1
        #self.Cr = None

        self.drTransaction = True  # 1
        self.crTransaction = None

       ## self.drAcc = 1
       ##self.crAcc = None

    def _debit(self):  # , amount):  # ):
        self.setDebit()  # prepares for a debit account

        # pass
    def _credit(self):  # , amount):
        self.setCredit()  # prepares for a credit account
        # if self.__account
        # pass
    # TODO: add here

    """ Do Not Implement it , out of the bat 
    def debit(self, amount):  # ):
        self.setDebit()  # prepares for a debit account

        # pass
    
    def credit(self,amount ): # , amount):
        self.setCredit() 
   """


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

    def calcFlow(self, amount, operator):
        """
        for a DebitAccount 
        a crTransaction renders flow as an out-flow 
        a drTransaction renders flow as an in-flow 

        Parameters
        ----------
        amount : TYPE
            DESCRIPTION.
        operator : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        flow = 0
        if operator == self.crTransaction:  # self.crTransaction:  # self.Cr: #If Credit Transaction
            # pass #representing an out-flow (with a minus sign)
            flow = -1 * amount  # then it's a negative flow [Out-Flow]
            # check accountType
        elif operator == self.drTransaction:  # self.drTransaction:  # If Debit
            flow = 1 * amount  # then it's a Positive Flow [In-Flow]
            # pass
        elif operator == None:  # if no operator, then do nothing at all
            pass
        return flow

    def flowHandling(flow):
        _stringFlow = ""
        if flow < 0:
            _stringFlow = "Out-Flow (-)"
        elif flow > 0:
            _stringFlow = "In-Flow (+)"
        elif flow == 0:  # at 0
            "No-Change (n.c) "  # N.C

        else:  # there must've been a mistake
            raise Exception("an error in amount")
        return _stringFlow
    """
    def __init__(self, Name, totalBalance):

    #super().__init__(Name=Name, totalBalance=totalBalance)
    #super(DebitAccount, self).__init__(Name=Name, totalBalance=totalBalance)
    Account.__init__(Name=Name, totalBalance= totalBalance)
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
       # self.drTransaction = 1  # True #1 # assign it  #N.D
        #self.Cr = None
        #super.drTransaction = 1
        print("Debit Finished")
    """

    def __init__(self, Name, totalBalance):  # same

        super(DebitAccount, self)._debit()
        # super().Dr = 1      #N.D
        # sets account (with name, totalBalance  specified)
        super(DebitAccount, self).__init__(Name, totalBalance)

        # Intent: initialize account, with a sum `totalBalance`
        #  self.drTransaction = 1  # N.D
        #  self.CrTransaction = None
        # sets account to be a DebitAccount  #incrementing initial balance of drAccount [Dr]
        # self.setDebit()

        print("Debit(2) Finished")

        # now reset account's state
        self.resetAccountState()

    def setCredit(self):

        self.crTransaction = True  # 1
        self.drTransaction = None

    # TODO: depreciate the following
        #self.Cr = 1
        #self.Dr = None

    def setDebit(self):
        """
        sets accounts 

        Returns
        -------
        None.

        """
        #self.drTransaction = 1
        #self.crTransaction = None
        self.drTransaction = True  # 1
        self.crTransaction = None

        # TODO: depreciate the following
        #self.Dr = 1
        #self.Cr = None

    def finalize(self):
        self.resetAccountState()

    def calculateFlow(self, amount):  # se:
        # 1 checks if amount is valid
        self.checkAmountIsValid(amount)

        # TODO:

       # self.totalBalance -
        # pass

    # Stateful- Actions: debit , credit

    def debit(self, amount=100):  # 0.0): # same
        super()._debit()  # setDebit() Set dr transaction flag
        # self.drTransaction == 1: #.Dr == 1:  # problem self.Dr == None (not 1 [Expected ])
        if self.drTransaction:
            if amount > 0:
                # self.decrement(amount)
                # super(DebitAccount, self).increment(amount)
                # debitAccount =  super(DebitAccount, self)
                # debitAccount.totalBalance, amount)
                newTotalBalance = increment(self.totalBalance, amount)
                self.cashflow = calcDifference(
                    newTotalBalance, self.totalBalance)
                self.totalBalance = newTotalBalance

                self.resetAccountState()

                """
                    if self.Cr == 1:
                        self.increment(amount)
                    elif self.drTransaction == 1:
                        self.decrement(amount)
                """

        else:
            raise Exception("ERROR: `amount` must be positive")  # <----------
        #else: #
        #    raise  Exception("ERROR: `amount` must be positive")

    def credit(self, amount=100):  # 0.0): # same
        super()._credit()  # sets credit flag  #self.setCredit()    # set a credit state

        # self.calculateFlow(amount)  # TODO <--------- # unsure
        print("entering credit ")
        print("amount = ", amount)

        if self.crTransaction:  # == 1:  #Cr == 1:  # checks if credit operation
            # if amount > 0:
            # self.cr
            #super(DebitAccount, self).decrement(amount)
            #debitAccount =  super(DebitAccount, self)
            #decrement(debitAccount.totalBalance, amount)

            newTotalBalance = decrement(self.totalBalance, amount)
            self.cashflow = calcDifference(newTotalBalance, self.totalBalance)
            self.totalBalance = newTotalBalance
            self.resetAccountState()
            return newTotalBalance
            """
                    if self.Dr == 1:
                        self.decrement(amount)
        
                    elif self.Cr == 1:
                        self.increment(amount)
                    """
      # UncommentMe
      #  else:
      #      raise Exception("ERROR: `amount` must be positive")

    """
        def debit(amount):
           #fetches totalBalance, increments it by amount, returns updated totalBalance
            tmp = self.totalBalance +amount
            if ampunt >0 and tmp>0:
                self.totalBalance = tmp
            return self.totalBalance
    
    
        def credit(amount):
                #fetches totalBalance, decrements it by amount, returns updated totalBalance
                # super().debit(amount)
                tmp = self.totalBalance - amount
                if ampunt >0 and tmp>0:
                    self.totalBalance = tmp
                return self.totalBalance
    
        """

    def checkDrCondition(self, amount: float):
        """checks current Dr Condition """

        if self.drTransaction:  # self.drTransaction == 1:  # self.Dr == 1:
            # increment , if Dr (Debit)
            #super.increment(self.totalBalance, amount)
            super(DebitAccount, self).increment(amount)

            self.finalize()
        elif self.crTransaction:  # self.CrTransaction == 1:
            # decrement , if Cr (Credit)
            #super.decrement(self.totalBalance, amount)
            super(DebitAccount, self).decrement(amount)
            self.finalize()

        # (potential 2-faced loophole)
        elif self.drTransaction == None and self.crTransaction == None:
            pass
        else:
            raise Exception(
                "Unexpected Error Occured , please try again later")

    """
        def __init__(self, amount: float):
            super().__init__(amount)  # call the default function
            checkDrCondition(amount)
       

        def __init__(self, Name: str, totalBalance: float):
            super(DebitAccount,self).__init__(Name, totalBalance)  # call the default function

        
        def __init__(self, Name="N/A",  amount=0.0):
    
            super().__init__(Name, totalBalance, amount)  # call the default function
            checkDrCondition(amount)
    
    
        """

    def increment(self, amount):
        """
            increments by an amount 
            (only way of incrementing a dr Account is by debiting it or 
             by having a drTransaction ==1)
        Parameters
        ----------
        amount : float 
            amount should be positive
        DESCRIPTION.

        Raises
        ------
        Exception
        if amount is negative, null, or an empty string

        Returns [should return the flow ]
        -------
        None.

        """
        if self.drTransaction:  # == 1:  # self.Dr == 1:

            # increment , if Cr (Credit)
            super(DebitAccount, self).increment(amount)  # compiles

            #     elif Dr  ==1:
            # decrement , if Dr (Debit)
            #        decrement(self.totalBalance, amount)

        # Otherwise, if nothing is set, then do Nothing
        elif self.drTransaction == None and self.crTransaction == None:
            pass

        else:
            raise Exception(
                "Unexpected Error Occured , please try again later")
    """
    
        def increment(self, amount=0.0):
            if self.Dr == 1:
                #super.increment(self.totalBalance, amount)
                super.increment(amount)
    
        def decrement(self, amount=0.0):
            if.:
                # super.decrement(self.totalBalance, amount)
                super.decrement(amount)
    
        """

    def decrement(self, amount):
        """
        decrements amount, if amount is negative 

        Parameters
        ----------
        amount : TYPE
            DESCRIPTION.

        Raises
        ------
        Exception
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if self.crTransaction:  # == 1:  # and self.drAcc == 1: #self.Cr == 1:
            # increment , if Cr (Credit)

            super(DebitAccount, self).decrement(self.totalBalance, amount)
            # reset cr flag, assign to None

            #self.crTransaction = None
            self.resetAccountState()

            #     elif Dr  ==1:
            # decrement , if Dr (Debit)
            #        decrement(self.totalBalance, amount)

        # Evaluate the passing condition (both bool flags are equal to None )
        elif self.drTransaction == None and self.crTransaction == None:
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
    def __init__(self, Name, totalBalance):  # same #*args, **kwargs): #changed
        # self.website=kwargs.pop('website')
        # the thing Dr is not given directly thru the  parameter
        #  self.Dr=kwargs.pop('Dr') # pop the required attribute

        # sets up the account with name & totalBalance
        super(CreditAccount, self).__init__(Name, totalBalance)

        self.resetAccountState()

        # self.Cr = 1 # assign it
        # self.Cr = 1  # True #1 # assign it
        #super.Dr = 1
        print("Credit Finished")

    def __init(self, Name, totalBalance):
        super(CreditAccount, self).__init__(Name, totalBalance)

    # Domain functions:
    # Unused
    def checkCrCondition(self, amount: float):
        # if Dr value is set to 1
        if self.drTransaction:  # self.Dr == 1:
            # increment , if Dr (Debit)
            #super.increment(self.totalBalance, amount)
            super(CreditAccount, self).decrement(amount)  # Account decrements
            self.resetAccountState()  # followed by a reset state, back to `None`
        elif self.crTransaction:  # self.Cr == 1:
            # decrement , if Cr (Credit)
            #super.decrement(self.totalBalance, amount)
            super(CreditAccount, self).increment(amount)
            self.resetAccountState()  # followed by a reset state, back to `None`
        elif self.drTransaction == None and self.crTransaction == None:  # If both none, then do nothing
            pass
        else:
            raise Exception(
                "Unexpected Error Occured , please try again later")

    # Behaviors:
# bank.credit [crAccount.credit] [+]
    def debit(self, amount=100):  # 0.0): # dr CreditAccount [-]
        # self.Dr == 1:            #amount > 0:
        super()._debit()  # set debit flags

        if self.drTransaction == 1 and amountIsPositive(amount):

            # self.decrement(amount)
            #super(CreditAccount, self).decrement(amount)
            # .increment(amount)  #<-------
            ##creditAccount = super(CreditAccount, self)
            # TODO: should return the cash-flow

            #decrement(creditAccount.totalBalance, amount)
            newTotal = decrement(self.totalBalance, amount)
            # max(self.totalBalance, newTotal ) -    min(self.totalBalance, newTotal)
            self.cashFlow = calcDifference(self.totalBalance, newTotal)

            self.totalBalance = newTotal

            self.resetAccountState()  # reset state
            """
                    if self.crTransaction == 1:
                        self.increment(amount)
                    elif self.drTransaction == 1:
                        self.decrement(amount)
                """
        else:
            raise Exception("ERROR: `amount` must be positive")

    def credit(self, amount=100):  # 0.0): # # cr CreditAccount [+]  #<------
        # and amountIsPositive(amount): #self.Cr == 1: # amountIsPositive(amount): #amount > 0:
        super()._credit()  # added _credit
        if self.crTransaction == 1:
            # self.cr
            # .increment(amount)  #<-------
            ##creditAccount = super(CreditAccount, self)

            # TODO: should return the cash-flow
            #increment(creditAccount.totalBalance, amount)

            newTotal = increment(self.totalBalance, amount)

            # max(self.totalBalance, newTotal ) -    min(self.totalBalance, newTotal)
            self.cashFlow = calcDifference(self.totalBalance, newTotal)
            self.totalBalance = newTotal

            self.resetAccountState()  # reset state, back to `None`

            """
                    if self.drTransaction == 1:
                        self.decrement(amount)
        
                    elif self.crTransaction == 1:
                        self.increment(amount)
                    """

     #   else:
     #       raise Exception("ERROR: `amount` must be positive")

    # The end # Correct function implementation


# Credit Accounts
# Liability : CreditAccount
class Liability(CreditAccount):

    def __init__(self, Name, totalBalance):
        super(Liability, self).__init__(Name, totalBalance)
        self.tag = "Liability"
# ==========================================


class Capital(CreditAccount):

    def __init__(self, Name, totalBalance):
        super(Capital, self).__init__(Name, totalBalance)
        self.tag = "Capital"

# ===============================================================================

# Revenue [Statement of Comprehensive Income (SOCI ) object ]


class Revenue(Capital):  # Revenue is a Capital account

    def __init__(self, Name, totalBalance):
        super(Revenue, self).__init__(Name, totalBalance)
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

    def __init__(self, Name, totalBalance):
        super(Asset, self).__init__(Name, totalBalance)
        self.tag = "Asset"

##  Expense : DebitAccount


class Expense(Asset):  # Expense is a
    """ an Expense shows a `Value Outflow` of an account, for a given period of time """

    def __init__(self, Name, totalBalance):
        super(Expense, self).__init__(Name, totalBalance)
        self.tag = "Expense"

# ==============================================================
# Experimental part - transaction


class transaction():
    """set dr for debit side, cr for cr side , then nullify flags after transaction's finished """

    def __init__(self, Acc1: Account, Acc2: Account, amount: float):
        # Assignment
        self.firstAccount = Acc1
        self.secondAccount = Acc2

        # dichotomy detected:
        # Q. is Acc1 , Acc2 classes already initialized?  if so then (assuming it already got some previous value )
        # set totalBalance

        # Acc1.totalBalance = #amount #or += amount
        # Acc2.totalBalance = #amount #or += amount

        # Check if such Amount Exists

        # self.firstAccount.totalBalance

        # Q. do we need enforce a decorator or wrapper?
        # Condition check
        #self.amount = round(amount, 2)
        # DebitAccount.drTransaction = 1 and CreditAccount == 1
        # TODO: Specify all possible combination of Accounts

        if Acc1.drTransaction == 1 and Acc2.CrTransaction == 1:  # Dr == 1 and Acc2.Cr == 1:  # <-----------
            Acc1.__class__ = DebitAccount(
                Acc1.Name, Acc1.totalBalance)  # Set Debit Account
            Acc2.__class__ = CreditAccount(
                Acc2.Name, Acc2.totalBalance)  # Set Credit Account
            print("Transaction:\ntype(Acc1) = ", type(
                Acc1), " type(Acc2) = ", type(Acc2))

            # Acc1 = (Debit) Acc1
            # Acc2 = (Credit) Acc2

            # self.Acc1 = Acc1
            # self.Acc2 = Acc2

            Acc1.debit(amount)
            Acc2.credit(amount)

            Acc1.credit(amount)
            Acc2.debit(amount)

        # the following
        # == 1 and Acc2.crTransaction == 1:
        elif Acc1.crTransaction and Acc2.Transaction:

            # Acc2 =(Debit) Acc2
            # Acc1 = (Credit) Acc1

            Acc1.__class__ = CreditAccount
            Acc2.__class__ = CreditAccount

            # Return a User-Friendly Message to the User
            print("InvalidInput: both accounts are of class CreditAccount")
            pass

        elif Acc1.drTransaction and Acc2.drTransaction:  # == 1 and Acc2.drAcc == 1:
            # pass always
            # Acc2 =(Debit) Acc2
            # Acc1 = (Credit) Acc1

            Acc1.__class__ = DebitAccount
            Acc2.__class__ = DebitAccount

            # Return a User-Friendly Message to the User
            print("InvalidInput: both accounts are of class DebitAccount")
            pass

        """
        elif Acc1.crTransaction == 1 and Acc2.drTransaction == 1:

            # Acc2 =(Debit) Acc2
            # Acc1 = (Credit) Acc1

            Acc1.__class__ = CreditAccount(Acc1.Name, Acc1.totalBalance)
            Acc2.__class__ = DebitAccount(Acc2.Name, Acc2.totalBalance)
            Acc1.debit(amount)
            Acc2.credit(amount)
        """
        """
        print("type(Acc1) = ", type(Acc1), "type(Acc2) = ", type(Acc2))
        self.Acc1 = Acc1
        self.Acc2 = Acc2"""

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


AccountReceivable  = DebitAccount("Mr.pip A/c Recievable ","Pip",100) #Pip [+100] 

cash = DebitAccount("cash ", 100)   # 100 [+100]

#============
1.3 Herbert's
Account Receivable Herbert = DebitAccount("Mr. Herbert's A/c Receivable ",100) 



# Transaction 3  

dr cash 100                 # increment 100 [+100]

    cr AccountReceivable Pip 100 # decrement  [ -100]

Comment: Being Herbert's Debt A/R for Service Rendered, 100 shillings") 

#Initialize accounts, by  Adding a debt Account (Expense) for Mr. Herbert

herbertDebt = AccountRecievable("Herbert's Debt","Herbert", 100) # [+100]
serviceRendered = RevenueAccount("Service Rendered", 100)  # [+100]

# Comment: Being Herbert's Debt A/R for Service Rendered, 100 shillings
#===================

# Transaction 4 : BadDebt Expense 


dr BadDebt Expense  100

cr herbertDebt 100 

dr BadDebt Expense 100 [+100] #[Expenditure, to SOCI]

cr herbertDebt [-100] # [now Closed (herbertDebt = 0) ]

#TODO: report back that account `herbertDebt` is now closed 



"""
# ==============================================================
# Demo
# 1 Transaction of Incrementation:

# Transaction of transfer
# between an abstract account i.e. bank and a real account i.e. cash


# DebitAccount  # correcrt #comment: increments a debitAccount, `DebitAccount` ,  `cash`,
cash = DebitAccount("cash", 1000)
# CreditAccount # correct #comment: increments a creditAccount, `CreduitAccount` ,  `bank`,
bank = CreditAccount("bank", 1000)  # compiles properly

print("cash.totalBalance", cash.totalBalance)    # display cash
print("bank.totalBalance", bank.totalBalance)   # display

# ===============================================

# _dr(bank,100)
# _cr(cash,100)
print("cash = ", cash)
print("bank = ", bank)

print("cash.totalBalance = ", cash.totalBalance,
      " bank.totalBalance = ", bank.totalBalance)

# returns type(Acc1) =  <class 'enum.EnumMeta'> type(Acc2) =  <class 'enum.EnumMeta'>
# Transaction(Account1, Account2 , amount)
transaction(DebitAccount, CreditAccount, 100)

print("cash.totalBalance = ", cash.totalBalance,
      " bank.totalBalance = ", bank.totalBalance)


# Increment

"""
# try 1 : ( debugs

print("try 1:")
cash.debit(100)
bank.credit(100) # Issue while using this function with this function # 

"""

print("cash's totalBalance = ", cash.totalBalance)
print("Bank's totalBalance = ", bank.totalBalance)


# try 2 : ( debugs)
print("try 2:")
cash.increment(100)
bank.increment(100)

print("cash's totalBalance = ", cash.totalBalance)
print("Bank's totalBalance = ", bank.totalBalance)

# try 3 : ( debugs)
print("try 3:")
cash.decrement(100)
bank.decrement(100)

print("cash's totalBalance = ", cash.totalBalance)
print("Bank's totalBalance = ", bank.totalBalance)
# Comment: increment &  decrement, along with `DebitAccount` & `CreditAccount` function properly
# =====================

# Inherits DebitAccount #TODO: apply `Personal Account`


class AccountReceivable(DebitAccount):

    # i.e. transactionName = Pip's Debt", DebtorName = "Pip", proprietorName 
    def __init__(self, transactionName, DebtorName,proprietorName, amount):
        """
        it's about a payer i.e. DebtorName & 
        a payee i.e. proprietor

        Parameters
        ----------
        entityDesc : str
            Provides an account Description, user-friendly
        DebtorName : TYPE
            DESCRIPTION.
        amount : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        super().__init__(transactionName, amount)
        # self.Name = entityName  #Debtor's Name
        # Object , of type DebitAccount
        # self.Receivable = AccountReceivable #unsure about this
        # amount (decimal, to 2 places)
        #self.amount =  round(amount,2)

        # Debit For DebtorName
        self.DebtorName = DebtorName  # new

        self.proprietorName = proprietorName
        

# Inherits DebitAccount #TODO: apply `Personal Account` [as it should be ]
class AccountPayable(CreditAccount):

    # takes
    def __init__(self, transactionName, creditorName,proprietorName, amount):
        """
        it's about a payee i.e. CreditorName
        & 
        a  payer : the proprietor 
       (for an amount loaned, or on credit )

        Parameters
        ----------
        transactionName : str
            the name Describing the transaction 
        CreditorName : TYPE
            A name of the creditor, providing credit to Proprietor (by cash , or other  mediums of `asset`s, Agreed upon by both parties )
        amount : TYPE
            quantity , sum of money

        Returns
        -------
        None.

        """
        super().__init__(transactionName, amount)
        # self.Name = entityName  #Debtor's Name
        # Object , of type DebitAccount
        # self.Receivable = AccountReceivable #unsure about this
        # amount (decimal, to 2 places)
        #self.amount =  round(amount,2)

        # adding info For CeditorName
        self.creditorName = creditorName  # new
        self.proprietorName = proprietorName
        
        
    def init2(self, transactionName, CreditorName,proprietorName, amount):
        super().__init__(transactionName, amount)
        # self.Name = entityName  #Debtor's Name
        # Object , of type DebitAccount
        # self.Receivable = AccountReceivable #unsure about this
        # amount (decimal, to 2 places)
        #self.amount =  round(amount,2)

        # adding info about CeditorName
        self.creditorName = CreditorName  # new

        
# =======================================

# capital classes

# RevenueAccount

class RevenueAccount(Capital):  # CreditAccount):
    """ 
    - RevenueAccount is a gain in Capital.
    - from 
    - It is  not an income, but to calculate it:
    find the difference between the account's `totalBalance`, for a certain period 
    & its previous period income, at a previous time:
        -- if loss account :"""

    def __init__(self, entityName, amount):
        super().__init__(entityName, amount)
        self.tag = "Revenue"

# ExpenditureAccount

class ExpenditureAccount(DebitAccount): # Contra- Asset account
    """
    - ExpenditureAccount it is a Contra-Asset Account 
    while an asset increases by a `Debit` `Dr` , decreases by a `Credit`, `Cr`)
    this Contra-Asset Accout increases by a `Credit`, decreases by a `Debit`    
    why it is a contra: 
    As it's responsible for decreasing (i.e. eating up) a `DebitAccount`
        

    """

    def __init__(self, entityName, amount):
        super().__init__(entityName, amount)
        self.tag = "Expenditure"
        
    #Note: ExpenditureAccount` as a `Contra-` Account : it constitutes that 
    def debit(self, entityName, amount): #as an asset increases by a debit (i.e + 100)
        super().credit(amount) # a contra_account increases by a credit (i.e. -100 )
        
    def Credit(self, entityName, amount): # seemingly , same logic follows 
        super().debit(amount) 

#Note:  in the US `GAAP`: the counter accounts are called `Contra`
    """
    def __init__(name,totalBalance):
        super().__init(name,totalBalance)
        

#barnettInn  Barnett Inn's
"""

class badDebtRecovered(DebitAccount):
    
    def __init__(self,transactionName, proprietor,debtor, payer, amount):
        
        super(Revenue, self).__init__(transactionName, amount)
        
        self.proprietor = proprietor 
        self.debtor = debtor
        self.payer = payer 

        
    
# =======================================


# =======================================
# Demo
# note: only in Demo , cash is cashbarnettInn
"""pip's Debt is an expense for **Barnett's Inn**, or `barnettInn` i.e. 
he has to pay for it  ( in  return of service rendered i.e. the liquor had at Barnett's Inn)

types of reports
1.Balance Sheet: most important report , with it we (accountant)  can verify & Test  accounting is balanced (& correct)

2.SOCI (Statement of Comprehensive Income)

Payment Players:
    a `payer` who pays, & a payee: who recieves the payment (in exchange of 
a `product` or a service)

# payment 

there are 2 types of payment 
 
 1. in full [payment medium: cash /debtCard ]
payer: who pays
payee: who recieves the payment 

Meaning of Accounts Recievable

here> the proprietory `BarnettInn` that had a debor account `pip` of `100` shellings, 
 `100` from the debtor `pip` is to be recieved ( 
     note: account reviebale is a current Asset account: meaningp
     the proprietor `BarnettInn` expects its Debtor `pip` to pay back the amount, 
     in exchange for the service rendered ( at one time in a `BarnettInn` pub).
     Hence, `Pip` the Debtor now has a debt of 100 shillings, to pay back to proprietor `BarnettInn`
     within this year.
     

 2. on-account [payment medium: creditCard/ Recie] 
 
 3. in-installments: #TODO
    especially if the sum is hefty  & large, payment with  installments would be practical 
    (involves a down-payment, then other payments, monthly usually at start or end of period 
     (has to have the agreements of both parties, beforehand ) )
     - balance is debited when the payer repays a portion ( or the rest of the sum)



     
# Back to the story: from Barnett Inn's Perspective,we'd see how to write accounts 
#Note : A/c is a short-hand for Account
#curcial note : each transaction happens at a specific time specified, 
`Date` won't be of a concern ( temporarily , for now )
  
#================
"""
#Notes: 
    
# `AccountReceivable` is an `Asset` account 

# import accounting  # correctly imported [But other files (in the same Dir) cannot read it, on Windows ]


# =======================================
# cashBarnettInn.totalBalance = increment(cashBarnettInn.totalBalance, 100) # dr cashBarnettInn 100  [+100]

def demoEasyAccounting():

    # Transaction 1
    """
    Transaction 1 : the Value Increasing Transaction 
    Because of a 
    certain `Action` performed (sell of a `product` or `service`  rendered (Tendered)
    # Debit & Credit are incremented , by a 100

    """

    """
    Dr Accounts Receivable (from Pip) 100

    	Cr Service Rendered 100

    commment: (Being Serice Rendered to Mr. pip, on account) 

    """

    """
    Description:
    # pip makes a promise, to return back his Debt 
      of 100 shillings to `barrerttInn` as serviceRendered [CreditAccount]  (in exchange of service rendered )
     
    Note: service rendered in an 'abstract' accounting object, a 'CreditAccount'
    # Instantiate accountReceivable by 100 ( is a  DebitAccount) that pip should pay
    # instantiate a CreditAccount 100 (serviceRendered) 100

    Note: pipdebt is an instance of  AccountRecievable class (an Asset for Proprietor, Barnett Inn's)
     It will stay the same, for the rst of the demoo (but it helps adding clarity, clearing confusion )

    From the BarnettInn's Perspective, they must the following: 
        
    """
    print("Transaction 1:\n")
    # pipDebt = DebitAccount("pip's Debt", 100) # Dr Expense Account   by 100 [+100]
    # serviceRendered = CreditAccount("Service Rendered", 100) #Cr Credit Account  by 100 [+100]

    # accountReceivable = DebitAccount( "pip's Debt (Accounts Recievable)",100) # increment [100]
    # sericeRendered = CreditAccount("Service Rendered",100) # increment [100] (to SOCI report )

    # Instantiate pipDebt, from AccountsRecievable[Dr] , serviceRendered from RevenueAccount [Cr]

    # increment [+100] (to Balance Sheet) [Dr  AccountReceivable (from Debtor `Pip` to Proprietor `BarnettInn` )]
    #                "Transaction" , "DebtorName", "ProprietorName, 100 ) 
    
    pipDebt = AccountReceivable("Pip's Debt", "Pip","BarnettInn", 100)

    # increment [+100] (to SOCI report ) [Cr]
    serviceRendered = RevenueAccount("Service Rendered", 100)

    print("pipDebt = ", pipDebt.totalBalance)
    print("serviceRendered = ", serviceRendered.totalBalance)

    # **note :** Revenue is not Income (It is equal to serviceRendered)
    # Comment: Being Payment of Service Rendered, by Mr. Pip, on Account
    print("Comment: Being Payment of Service Rendered, by Mr. Pip, on Account ")

    # ============================
    # Transaction 2:
    print("Transaction 2:\n")
    """
    decrement(pipDebt.totalBalance, 100)  # Dr pipDebt 100
    increment(barnettInn.totalBalance, 100) # Cr B. Inn 100
    """
    # Transaction 2: `Balancing  Transaction`
    #  `pip` pays back his debt , to `Barnett's Inn, in full [or BarnettInn Receives cash from Mr. Pip ]
    # Crucial Note: Use `cashBarnettInn` instead of cash already used [ Demo, only]

    # Create a cash account for barnettInn  i.e.  cashBarnettInn add 100
    # cashBarnettInn =
    # used instead of  Cash [as `cashBarnettInn`] # [+100] #up by 100 [+100] #  Dr barnettInn 100
    cashBarnettInn = DebitAccount("Cash", 100)

    # down by 100 [-100]  # Cr pipDebt 100 # [-100]
    pipDebt.totalBalance = decrement(pipDebt.totalBalance, 100)

    # =============================
    # 2
    """
    cashBarnettInn = DebitAccount("Cash", 100) # used instead of  Cash [as `cashBarnettInn`] # [+100] #up by 100 [+100] #  Dr barnettInn 100

    pipDebt.credit(100) # down by 100 [-100] # pipDebt.totalBalance = 0
    """
    # =============================
    # [100] # Dr  cashBarnettInn
    print("cashBarnettInn.totalBalance = ", cashBarnettInn.totalBalance)
    print("pipDebt.totalBalance = ", pipDebt.totalBalance)  # [-100] #

    # Comment: Being Payment by Mr. Pip in full, by cash
    print("Comment: Being Payment by Mr. Pip in full, by cash")  # [-100] #

    # ============================
    # Transaction 3
    #
    print("Transaction 3:\n")
    # pipDebt.credit(100)

    # RevenueAccount increments the Capital `Owner's Equity`

    # acccount for debt for Mr. Hurbert, for service rendered

    # Initialize accounts, by  Adding a debt Account (Expense) for Mr. Herbert
    herbertDebt = AccountReceivable(
        "Herbert's Debt", "Herbert","BarnettInn", 100)  # up 100 [+100]
    serviceRendered = RevenueAccount(
        "Service Rendered", 100)  # creditAcc up by 100
    print("herbertDebt.totalBalance", herbertDebt.totalBalance, " open")  # 100
    print("serviceRendered.totalBalance", serviceRendered.totalBalance)

    print("Comment: being payment on service rendered, on Account ")
    # ===============================
    # ======
    # WARNING: IFRS Debt Handling Method : `Direct Write-Off`
    """
    The Dichotomy of Debt Handling

    1. Direct Write-off [IFRS] (World-wide)
        we wait, until debitor either:
            1. pay us back: we close his account [& problem is solved]
            2. debitor defaults (files for bankrupcy):
                the whole sum is **non-recoverable**
                and 
        
    2. GAAP (US):
        [Note1: DATE handling is required, as a pre-requisite ]
        if we are at the year end, account-balancing is needed
        
        - Gaap standards suggests estimating a non-recovereable sum (`out of the bat`)
        for the AccountRecievable totalBalance. 
        
        - this means: proprietor have to estimate a proportion of losses,
        in this example, 
        if HerbertDebt is not paid back at the end of the accounting period (month, year)
        1. the proprietor has to take a part of account recievable (may include HerbertDebt, along with other debtors)
        2. the proprietor trasfer it to `Doubtful Debts`
        
        as time moves on, the proprietor continues taking off proportions of accountrecievable, 
        (specifically those who are not paying back )
        
        
        
        
        Note2: this **may not** apply to small Businesses 
        
        
    """
    # Transaction 4
    # Bad Debt Example:
    # ExpenditureAccount decreases the Capital

    # Transaction 4 # Balancing Transaction
    print("Transaction 4:\n")

    # Description:
    # -------------

    # Herbert is unable to payback his Debt
    # Debt becoming an Expenditure (badDebtExpense)
    # closing account for `Mr. Herbert` (with a loss incurred )

    # badDebtExpense doesn't exist: create an ExpenditureAccount (contra- capital Debit Account )

    badDebtExpense = ExpenditureAccount(
        "Bad Debt Expense", 100)  # [+100] #[Expenditure, to SOCI]

    # decrement(barnettInn.totalBalance, 100) #down by 100 #  Dr barnettInn 100
    # down by 100  # Cr herbertDebt 100 [-100] # # [now Closed ]
    herbertDebt.totalBalance = decrement(herbertDebt.totalBalance, 100)

    print("badDebtExpense", badDebtExpense.totalBalance)

    print("Comment: Being Bad Debt Recovered \n")

    print("herbertDebt.totalBalance", herbertDebt.totalBalance, "<Closed>")

    print("Comment: Being Debt as a badDebt Expense\n")

    # ===============================
    print("Transaction 5\n")
    # Transaction 5 (helping transaction )
    # move the badDebt Expense to Losses Account
    """
    Transfers badDebtExpense from BalanceSheet to Statement of Comprehenisve Income [SOCI]
    at the end of the Accounting Period 
    """

    # We don't have LossAccount, but an Expenditure (account, which at the end of a period,
    # the account is calculated, & checked :
    # (1) Expenditure Account < 0:  *Loss Incurred*
    # (2) Expenditure Account == 0:  & the account is henceforth, closed .
    # ------------------
    #pipDebt = DebitAccount("pip's Debt", 100)
    #barnettInn = CreditAccount("Barnett's Inn", 100)

    # Transaction 5 # increment Transaction
    # pip pays back his debt ,in cash, to Barnett's Inn
    # pip pays off the transfered account, out of pocket

    cashBarnettInn.totalBalance = increment(
        cashBarnettInn.totalBalance, 100)  # dr cashBarnettInn 100  [+100]
    herbertRepayment = RevenueAccount(
        "Herbert's Debt repayment ", 100)  # [+100] (to SOCI)

    print("cashBarnettInn", cashBarnettInn.totalBalance)
    print("herbertRepayment.totalBalance", herbertRepayment.totalBalance,
          " To SOCI report, In-Flow (+100)")

    print("Comment: Being Debt repayment \n")

    # bad Debt Recovered
    """
    Transaction 6
    now we got the back the anoub
    Undoes & Removes the badDebt Expense [100]

    Dr  Bad Debt Recovered [+100] 
    cr bad Debt Expense [-100] #this removes the bad Debt: badDebtExpense= 100 - 100 = 0 <Closed>


    """

    # Transaction 6

    # badDebtRecovered doesn't exist, create a Debit Account for it, sum of 100
    # to close badDebtExpense Credit the account, by a 100

    # Dr badDebtRecovered # account states that  a bad debt has been recovered []
    badDebtRecovered = DebitAccount("Bad Debt Recovered", 100)

    # Cr badDebtExpense 100  [- 100] : badDebtExpense = 100 (before ) - 100 (now ) = 0 <Account Closed>
    badDebtExpense.totalBalance = decrement(badDebtExpense.totalBalance,  100)
    print("Comment: Being BadDebt Recovered", 100)

    return pipDebt, serviceRendered, herbertDebt, badDebtExpense, cashBarnettInn, herbertRepayment, badDebtRecovered


def demoIntermetiateAccounting(pipDebtBalance=100, cashBarnettInnBalance=100):

    # 1  Dr pipDebt , Cr serviceRendered 100
    """
    # Transaction Cause: A Service, for Mr. Pip
    # Transaction Effect: Mr. pip Debt
    """
    # pipDebt does not exist , create it, as an AccountReceivable [inheriting from a DebitAccount]
    # serviceRendered does not exist, create is, as a RevenueAccount  [inheriting from a ]

    # increment [+100] (to Balance Sheet) [Dr ]  in-flow: pipDebtBalance +100
    pipDebt = AccountReceivable("Pip's Debt", "Pip","BarnettInn", pipDebtBalance) 
    # increment [+100] (to SOCI report ) [Cr]
    serviceRendered = RevenueAccount("Service Rendered", pipDebtBalance)

    print("Comment:  Service Rendered for Mr. Pip, for 100 Shillings \n")

    # 2  Dr Cash 100 , Cr pipDebt 100
    # `cashBarnettInn` does not exist, create it, as a DebitAccount , with 100
    # `pipDebt` exists, as an AccountReceivable [Debit Account] , decrement it by 100, by crediting it [cr pipDebt 100 ]

    # [+100] totalBalance = 100
    cashBarnettInn = DebitAccount("Cash", cashBarnettInnBalance)

    # down by 100 [-100]  # out-flow: pipDebtBalance -100, pipDebt = 100 - 100 = 0 <Closed>
    pipDebt.credit(pipDebtBalance)

    print("Comment:  Being Cash Received, 100 Shillings, from Mr. Pip\n")

    # 3
    # `herbertDebt` doesn't exist: create it, as an AccountReceivable [DebitAccount],  with sum of 100
    # `serviceRendered` doesn't exist: create it, as a RevenueAccount [CreditAccount], with sum of 100

    herbertDebt = AccountReceivable(
        "Herbert's Debt", "Herbert","BarnettInn", 100)  # up 100 [+100]

    serviceRendered = RevenueAccount(
        "Service Rendered", 100)  # creditAcc up by 100

    print("Comment:  Service Rendered, for 100 Shillings, for Mr. Herbert\n")

    # 4

    # `badDebtExpense` doesn't exist, create it, as an `ExpenditureAccount` [ counter (Contra) Capital, as  a DebitAccount ], with sum of 100
    # `herbertDebt` exists, as a Account's Receivable , decrement it by a 100, via crediting it, by a 100

    badDebtExpense = ExpenditureAccount(
        "Bad Debt Expense", 100)  # [+100] #[Expenditure, to SOCI]

    herbertDebt.credit(100)
    print("Comment: Being Writing Off a  Bad Debt Expense\n")

    # 5 Pip Cash repayment (for friend Herbert )

    # `cashBarnettInn` exists, as a `DebitAccount`, increment it by a 100, via debiting it, by a 100 [Dr cashBarnettInn 100]
    # `herbertRepayment` doesn't exist, create it, as a `RevenueAccount` [of a `CreditAccount`] with a sum of 100

    cashBarnettInn.debit(100)  # [+100]  totalBalance = 200
    herbertRepayment = RevenueAccount(
        "Herbert's Debt repayment ", 100)  # [+100] (to SOCI)
    print("Comment: Being Debt repayment \n")

    # 6  Bad Debt Recovered
    #Intent: 
    #1. removes badDeb as `Expense` `badDebtExpense` replacing it with 
    #2. shows it has been recovered in `badDebtRecovered`
    # Dr badDebtRecovered # account states that  a bad debt has been recovered []
    badDebtRecovered = DebitAccount("Bad Debt Recovered", 100)
    badDebtExpense.credit(100)

    # badDebtExpense.decrement( badDebtExpense.totalBalance,  100) # Cr badDebtExpense 100  [- 100] : badDebtExpense = 100 (before ) - 100 (now ) = 0 <Account Closed>
    badDebtExpense.totalBalance = badDebtExpense.credit(100)
    print("Comment: Being BadDebt Recovered", 100)

    return pipDebt, serviceRendered, herbertDebt, badDebtExpense, cashBarnettInn, herbertRepayment, badDebtRecovered

# resetdemo

def demoReset():
    """ resets the demo associated with the "Great Expectations" proprietor is BarnettInn's""" 
   
    # 1 
    pipDebt = None
    serviceRendered = None

    # 2

    cashBarnettInn = None
    #pipDebt = None

    # 3

    herbertDebt = None
    serviceRendered = None

    # 4

    badDebtExpense = None
    herbertDebt = None

    # 5
    cashBarnettInn  = None
    herbertRepayment = None
    
    #6 
    badDebtRecovered = None 
    #badDebtExpense  = None
    return pipDebt, serviceRendered, herbertDebt, badDebtExpense, cashBarnettInn, herbertRepayment,badDebtRecovered



def demoProrietorPip(): #TODO: Continue
    
    #===============
    #Pip is the Proprietor

    #===============
    # Transaction 1
    # Pip writes in his `book` the creditor name 

    """
    The entity for whom he owes money to 

    Dr service rendered  100  [+100 ]
    	Cr Account Payable [Barnett Inn's] [+100] 
    """
    #----------------
    	
    # Transaction 2 
    """

    Pip pays back Barnett Inn's , in full 

    Dr Account Payable [to Barnett Inn's] 100 [-100]

        Cr cash 100  [-100]


    """
    #----------------

    # Transaction 3 : 
    """
    Herbert's debt :

    Dr service rendered  100  [+100 ]
    
    	Cr Account Payable [Barnett Inn's] [+100] 

    """


    #---------------
    # transaction 4 : 
    """
    Bad Debt Expense entry: 

    Where Herbert cannot pay back 


    Dr Account Payable [Barnett Inn's]  100 [-100]

        Cr Default Amount unpaid [Barnett Inn's] 100 [+100] 
                              #note: this must refer the the creditor 


    #Imagine: a scenario with full of creditors , each wants their piece 
    # to distinguish between them , you must have a credotpr name in there,
    as well 

    Thus , a personal name (for debitor/ creditor ) 
    is necessary to clearly distinguish them 

    """
    #----------------

    # Transaction 5: 
    """
    Pip pays off herbert's debt 

    pip's account: 
    Pays money sum, back to Barnett Inn's 

    Dr Expenditure  (payment to barnettInn) 100 [+100]
        Cr cash  100 [- 100] 
    """

    #--------------
    # Happens simultaneously, as pip pays off his friend's debt:

    #Herbert's account: 
    """
    Dr Default Amount unpaid [Barnett Inn's] 100 [-100] # money owed to barnettInns is paid 
        Cr  Account Payable [pip] 100  #liability to payback Mr.pip 

    # 1. removes the default amount , on Mr. Herbert 
    #2.  move the liability to pip

    #----------------------
    #Rewind: Intermediate level 
    Observation: an account could affect 1 or more accounts 
    (like domnios, falling because of on that caused them to move ) 

    """
# =======================================
# Main 

demoEasyAccounting()
demoReset()
demoIntermetiateAccounting()



# ============================




#print("cashBarnettInn.totalBalance =",cashBarnettInn.totalBalance)  # cash = 200
#print("herbertRepayment.totalBalance = ", herbertRepayment.totalBalance)


print("Comment: Being Herbert's Debt repayment, by Mr. Pip in full\n")
# increment(pipDebt.totalBalance,100)
# increment(cashBarnettInn.totalBalance,100) # Dr[cashBarnettInn : DebitAccount]

"""

Final Notes

Bad Debt handling has a deeper meaning than stated () 
Elaboration in demo would further complicate things 

"""
# =====================
print("successfully finished the accounting usecase")

"""increasing a Debit account is by debiting it, 
increasing a Credit Account is by crediting it 
(just remember, ""like"" attracts like)""
"""
print("demo2:\n")

cashSales = RevenueAccount("cashSales", 100)  # Cr Account
print("cashSales = ", cashSales.totalBalance)

cashSales.debit(50)  # = 50 # [-50]
print("cashSales = ", cashSales.totalBalance)
cashSales.credit(150)

print("cashSales = ", cashSales.totalBalance)
# =============

# Barnett Inn's is the Proprietor

# Print
# inint DebitAccount: Account Receivable for Barnett Inn's about Debtor Pip, for 100 Shillings
print("Transaction 1: \n")
# increment [+100] (to Balance Sheet) [Dr ]
pipDebt = AccountReceivable("Pip's Debt", "Pip", "BarnettInn" ,100)

# increment [+100] (to SOCI report ) [Cr]
serviceRendered = RevenueAccount("Service Rendered", 100)


print("pipDebt = ", pipDebt.totalBalance)
print("serviceRendered = ", serviceRendered.totalBalance)

print("Transaction 2: \n")


# ===============
# Pip is the Proprietor

# ===============
# Transaction 1
# Pip writes in his `book` the creditor name

"""
The entity for whom he owes money to 

Dr service rendered  100  [+100 ]
	Cr Account Payable [Barnett Inn's] [+100] 
"""
# ----------------

# Transaction 2
"""

Pip pays back Barnett Inn's , in full 

Dr Account Payable [to Barnett Inn's] 100 [-100]

Cr cash 100  [-100]


"""
# ----------------

# Transaction 3 :
"""
Herbert's debt :

Dr service rendered  100  [+100 ]
	Cr Account Payable [Barnett Inn's] [+100] 

"""


# ---------------
# transaction 4 :
"""
Bad Debt Expense entry: 

Where Herbert cannot pay back 


Dr Account Payable [Barnett Inn's]  100 [-100]

Cr Default Amount unpaid [Barnett Inn's] 100 [+100] #note: this must refer the the creditor 


#Imagine: a scenario with full of creditors , each wants their piece 
# to distinguish between them , you must have a credotpr name in there,
as well 

Thus , a personal name (for debitor/ creditor ) 
is necessary to clearly distinguish them 

"""
# ----------------

# Transaction 5:
"""
Pip pays off herbert's debt 

pip's account: 
Pays money sum, back to Barnett Inn's 

Dr Expenditure  (payment to barnettInn) 100 [+100]
    Cr cash  100 [- 100] 
"""

# --------------
# Happens simultaneously, as pip pays off his friend's debt:

# Herbert's account:
"""
Dr Default Amount unpaid [Barnett Inn's] 100 [-100] # money owed to barnettInns is paid 
    Cr  Account Payable [pip] 100  #liability to payback Mr.pip 

# 1. removes the default amount , on Mr. Herbert 
#2.  move the liability to pip

#----------------------
#Rewind: Intermediate level 
Observation: an account could affect 1 or more accounts 
(like domnios, falling because of on that caused them to move ) 

"""
# =============
# checkObjectIsaClass


def isNone(_object):
    if _object == None:
        return True
    elif _object != None:
        return False
    else:
        raise Exception(msg)


# requires: this function raises error if class is `None` , so check for `None`\
# then, call this function
def checkObjectIsaClass(_object, _classOrTuple):
    """
    checks whether the given object is of type class (or a tuple) 

    Parameters
    ----------
    _object : TYPE
        DESCRIPTION.
    _classOrTuple : object or tuple
        note: classor tuple cannot be `None`.

    Raises
    ------
    Exception
        DESCRIPTION.

    Returns
    -------
    response : bool
        returns true if object is of type of the mentioned class (or tuple).

    """

    response = None
    if isinstance(_object, _classOrTuple):
        print("Yes,", _object, " is a class of  ", _classOrTuple)
        response = True
    elif not isinstance(_object, _classOrTuple):
        print("No, ", _object, " is NOT a class of  ", _classOrTuple)
        response = False
    else:
        raise Exception(msg)
    return response


def checkObjectInClass(_object, _class):
    """
    if isNullable:  # is it None
        # if True then it's new, thus create it [require additional info: AccountType:Asset, Capital, ...]
        pass  # TODO: Instantiate a new object, from a given AccountType
    # check if this object is of this type:

    elif isNullable:  # and
        # checkObjectIsaClass(cashBarnettInn, DebitAccount ) # 2nd argument can't be None
        pass

    # https://stackoverflow.com/questions/16709879/how-can-i-get-previous-month-and-year-using-python/16710165#16710165
    """
    """ experimental 
    def getPrevMonth(_year=2012, _month=3, _day=1):
        return date(_year, _month, _day)+relativedelta(years=-1)


    def getPrevMonthN(n, _Year=2012, _month=3, _day=1):
        return date(2012, 3, 1)+relativedelta(years=-n)
    """

    isNullable = copy(isNone(_object))  # 1. check object is set to  `None`
    # 2. check object is of type `_class`
    isObjectAClass = copy(checkObjectIsaClass(_object, _class))

    if isNullable:  # 1. is it None ?
        # if True, then it's new object, hence, create it [require additional info: AccountType: Asset, Capital, ...]
        pass  # TODO: Instantiate a new object, from a given AccountType

    elif not isNullable and isObjectAClass:  # 2. is it an object of that class?
        pass

    # 3. last part # maybe, it's  an object of another class
    elif not (isNullable and isObjectAClass):
        pass
        print("object", _object, " is of another class from ", _class)
    else:
        raise Exception(msg)


#isNullable = copy(isNone(cashBarnettInn))
#isObjectAClass = copy(checkObjectIsaClass(cashBarnettInn, DebitAccount))


# Demo

pipDebt, serviceRendered, herbertDebt, badDebtExpense, cashBarnettInn, herbertRepayment, badDebtRecovered =demoIntermetiateAccounting()