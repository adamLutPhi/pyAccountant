class partialEntry:

    # 5.1.1. Using Lists as Stacks
    """ 
    The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index. For example:

            >>>
            stack = [3, 4, 5]
            stack.append(6)
            stack.append(7)
            stack
            [3, 4, 5, 6, 7]
            stack.pop()
            7
            stack
            [3, 4, 5, 6]
            stack.pop()
            6
            stack.pop()
            5
            stack
            [3, 4]
    """

    """ a list of items """
    # using list as stack 

    """
    def add(lst, i):

    """
    #adds a new name, and price 
    """
        lst.
        thislist = ["apple", "banana", "cherry"]
        thislist.append("orange")
        pass 
    def print():

        print(thislist)
        pass
"""

class Dict():

    def __init__():
        this.d = {}
        
    def add():
        pass
        """
        add( name, price)

        {'jack': 4098, 'sape': 4139, 'guido': 4127}
        """
    def print():
        pass
        #   for i, v in enumerate(['tic', 'tac', 'toe']):
        #        print(i, v)

# Example:
# Income statement: Income vs Expenses

# the same function works (for positive & negative values )
# (for both Debits , & Credits: each under their own context  )

names = ['wages& Tips', 'Income Interest ', 'Dividends', 'gifts recieved']
prices = [53.0   , 100.54 , 142.63 , 132.43 ]
# Add function

_sum = 0
for n, p in zip( names , prices ):
    #print()
    
    print('Income \t Budget \n {0} | {1}'.format(n, p))
    _sum += p
    print(' Subtotal: \t  \t  {0} \n '.format(_sum))

_total = _sum
print(' Total: \t  \t  {0} \n '.format(_total))


#import operator
# import operators 

names = ['Mortgage/Rent', 'Home/Rental Insurance ', 'Electricity', 'Gas/Oil', 'Water/Sewer/Traash', 'Phone', 'Cable/Satellite', 'other']
prices = [200.0   , 100.00 , 50.0 , 40.0, 20.0, 20.0, 25.0 , 0.0]

    
_sub = 0

# def x( names , prices  , total=1000):
_total = 1000 
for n, p in zip( names , prices ):
    #print()
    
    print('Income \t Budget \n {0} | {1}'.format(n, p))
    _sub += p
    print(' Subtotal: \t  \t  {0} \n '.format(_sub))

import inspect

x, y, z = 1, 2, 3

# get variable 
def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

"""
total -> 100% 
_sub -> x
x = _sub * 100/ total
"""
def getPercentage(_total, _sub):

    p = _sub * 100/ _total
    return p

def getRemainder(_total, _sub):
    return _total - _sub

def printValue(val):
    #todo: variable name 
    print(f" {val}  = ", percentSub)

# remainder = _total - _sub
remainder = getRemainder(_total, _sub)


print(' Total Net Income: \t  \t  {0} \n '.format(remainder))


def getDiff(percentAdd, percentSub):

    # calculate the gap : diff  = %Add - %Sub
    diff = percentAdd - percentSub
    print("diff = +", diff, " %")
    return diff

def getPercentGap(_total, _sub):

    #1. Get % Sub
    percentSub = getPercentage(_total, _sub)
    print("percentSub= ", percentSub, " %")

    percentTotal = 100
    # 2. Get % Add
    
    percentAdd = percentTotal - percentSub

    print("percentAdd= ", percentAdd, " %")

    #3. Calculate the gap : diff  = %Add - %Sub
    diff = percentAdd - percentSub

    print("diff = +", diff, " %")
    return diff, percentAdd, percentSub



def getGap2(percentAdd , percentSubb ):

    # 1. Diff: %Add - %Sub
    
    diff= percentAdd - percentSub
    return diff 

percentSub = getPercentage(_total, _sub)
print("percentSub= ", percentSub, " %")


percentTotal = 100
percentAdd = percentTotal - percentSub
print("percentAdd= ", percentAdd, " %")

# calculate the gap 
diff = percentAdd - percentSub


#finally calculate the gap 
diff = getDiff(percentAdd, percentSub) # percentAdd - percentSub



print("diff = +", diff, " %") # 9%

#Idea:
class partialEntry:
    """ captures a specific part of a `transaction` which can  either assume the  drSide or the crSide
    Purpose: acts as a bridge between a Report (balanceSheet in this instance` and a transction (of a Journal Entry )

    - Hint: only if we can add this as a form of function, in a transaction class, instead, that would have made things more "Straight-Forward, & easier
            (For all users: developers & end-users alike)
    """
    #pass
    def __init__(self):
        pass
    def __init__(self, drSide, crSide, amount, isDebit=True, MsgError="Unexpected Error Occured, please recheck input, then retry"):

        # Check `isDebit` flag , if so, return the debitSide Object & the amount
        if isDebit == True:
            self.transactionSide = drSide
            self.amount = amount
            return self.transactionSide, self.amount
        # otherwise, return `crSide` and the amount provided (in the consructor 
        elif isDebit == False:
            self.transactionSide = crSide
            self.amount = amount
            return self.transactionSide, self.amount

        else:
            raise ValueError(MsgError)

# Now we can capture any part (of any transaction ) with its corresponding amount, accordingly
# take the debit side (of a transaction) with its amount
pEntry1 = partialEntry("cash","bankAccount", 100, isDebit=True)

# take the credife side (of a transaction) with its amount
pEntry2 = partialEntry("cash","bankAccount", 100, isDebit=False)

#e.g. for balashe sheet: can take cash, add it into i.e. currentAssetNames list, with its amount, and `bankAmount` into currentEquities` list with its amount, as well.
        
        
"""
name: str price : double

1. Creating a new class creates a new type of object,
2. Allowing new instances of that type to be made.
3. Each class instance can have attributes attached to it for maintaining its state.
4. Class instances can also have methods (defined by its class) for modifying its state.


"""


class Report:


    dict = {} # dictionary is the not a very efficient, holds name, and price
    # as we could possibly have endless years, going back in time, each with different values
    # it's better to zip whichever years with values, with functions, to get the subTotal 
    def __init__(self):
        pass

    def __init__2(self, names, prices):
        #self
        pass 
    def calcSubtotal(self):
        pass

    def getSubtotal(self):
        self.subTotal
        
    
# class-agnostic , static function
# def ... ?



# APPL's data: @credit: : investopedia:
# image url source: https://www.investopedia.com/thmb/gUuGSjZWpXoc2miE2QfC-Z4Q6no=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/phpdQXsCD-3c3af916d04a4afaade345b53094231c.png

# Balance Sheet 's "positive-side" includes debit accounts :
# 1. Assets : ["Cash", "marketable security", "Account recievable"
# 2. SOCI "statementt of Comprehensive Income  : "Inventories", "Vendor"

    """
    why expense is a debit account?
    Q. Why are expenses debited?
    a. no answer [direct answer]
    hint: because expenses cause stockholder equity to decrease,

    """

"""
Value is not made, but is transformed, from one form to another
thus it is conserved 
Dr DrAccount -> [Increase ]

i.e. Dr cash    1000 [UP] [Asset grows]

        Cr Bank Account 1000 [UP] [Account grows ]
        
        | context = Bank Account (Personal | owned)

        1. the bank account(virtual) grows by the Asset invested in it (cash) by 1000
        
        2. the bank account is increased the same amount of cash depositied into that account

        3. This context is limited to: the bank account (Personal)
    ----

        but actually the pocket Money" account is now less by 1000

        # Cash on hand : got less
        we should also write this
        Expense of opening a bank account is 1000
        
        Dr Expense 1000 [] [UP] 
                cr Cash  1000 [DN] [Asset dimishes]

        | Context:   Pocket Money ( the liquidity) 
        
"""

"""asssumes there is a salary
    and cogs (cost of goods sold)

    """

## class BalanceSheet(Report): # TODO: complete 

# requires: partial Entry 
def iterateSubtotals(subTotals, printFunction=None):
        _sum = 0
        for item in subTotals:
            
            _sum += item
        #TODO: do sth useful, for the printFunction 
        return _sum

#Demo : Balance sheet

## currentAssets:

###names:
###Current Assets
# date Precedence:  from newest, to oldest: 2020, 2019

currentAssets = ["Cash", "marketable security", "Account recievable", "Inventories", "Vendor", "other currentAssets"] # Dt accounts 

CAprice2020 = [38016, 52927, 16120, 4061, 21325, 11264]

subTotalCA2020 = iterateSubtotals(CAprice2020)
print("current Assets Subtotal 2020 = ", subTotalCA2020)

CAprice2019 = [48844, 51713, 22926]

years = [CAprice2020, CAprice2019 ] #TODO: later " \

## subtotalCurrentAssets2019 =  iterateSubtotals(CAprice2019) # TODO: compre with later 
## for y in years no (take in the Same Year, first


# nonCurrentAssets:

nonCurrentAssets = ["Marketable Securities", "Property, plant", "equipment net"]
nCA2020  = [ 100887, 36766, 42522]

subTotalNonCurrentAssets = iterateSubtotals(nCA2020)
print("Subtotal 2020 = ", subTotalNonCurrentAssets)

totalAssets = subTotalCA2020 + subTotalNonCurrentAssets

print("total Assets  2020 = ", totalAssets)

#Ratios:
def cashRatio(cash , CurrentLiabilities):
    """Cash Ratio = Cash / Current Liabilities.""" 
    return cash / CurrentLiabilities

def currentRatio(CurrentAssets , CurrentLiabilities):
    
    return CurrentAssets / CurrentLiabilities

def quickRatio( cashEquivalents, aRecievable, currentLiabilities):
    """
    source: https://www.investopedia.com/terms/a/accountsreceivable.asp
    Key Takeaways:
    Accounts receivable (AR) are an asset account on the balance sheet
    that represents money due to a company in the short term.

    AR = Accounts receivable are created when a company lets a
    buyer purchase their goods or services on credit.
    

    """
    cashRecievable = cashEquivalents+ aRecievable
    quickRatio = cashRecievable / currentLiabilities
    return quickRatio
    # quickRatio = (cashRecievable / currentLiabilities )
    """    
    cashEquivalents = cashEquivalents + aRecievable 
    cashEquivalents / currentLiabilities
    Cash & Equivalents + A/R) / CurrentLiabilities
    """

""" Ratios:
CashRatio = cash / CurrentLiabilities
CurrentRatio = CurrentAssets / CurrentLiabilities.
Quick Ratio = (Cash & Equivalents + Accounts Receivable (A/R) / CurrentLiabilities

"""

"""
first:
We want to estimate Doubtful Debt:
Source: https://www.indeed.com/career-advice/career-development/allowance-for-doubtful-accounts#:~:text=It%20estimates%20the%20allowance%20for,10%2C000%20x%200.05%20%3D%20500
stimates the allowance for doubtful accounts by multiplying the accounts receivable by:
"appropriate percentage" for the aging period
and then adds those two totals together.
For example: 2,000 x 0.10 = 200.
10,000 x 0.05 = 500.
"""

# for item in Assets
### total assets 2020 , 2019 
assets2020 = [CAprice2019  , nCA2020 ] #TODO: try running the function ,for different years


#for item in assets2020:
    
#    item
# subtotal:

# totalAssets
#----

##Current Liabilities:

currentLiabilities = [ "AccountsPayable", "other current Liabilities", "Deferred revenue", "Commercial paper", "Term Debt"]
cl2020= [42296, 42684, 6643, 4996, 8773]

# Noncurrent Liabilities
nonCurrentLiabilities = ["Term debt", "Other non-current Liabilities"]
ncl2020 = [98667, 54490]

subTotalCurrentLiabilities2020 = iterateSubtotals(cl2020)

subTotalNonCurrentLiabilities2020 = iterateSubtotals(ncl2020)

totalLiabilities = subTotalCurrentLiabilities2020+ subTotalNonCurrentLiabilities2020

print("totalLiabilities = ", totalLiabilities )


#---
#Capital : is about
## Commitments & Contingencies , a.k.a
## Shareholder's equity

shareholderEquity = ["Common Stock", "Retained Earnings", "Accumulated Other comprehensive income (loss)"]

shEquity2020 = [50779,14966, -406]

shEquity2019 = [45174, 45898, -584]

subTotalEquities2020 = iterateSubtotals(shEquity2020) # get equity 
print("subTotalEquity2020 = ", subTotalEquities2020)
totalEquities = subTotalEquities2020
# subEquity2019 = iterateSubtotals(shEquity2019)

#---
#def calc_grossMargin():
#class Income Statement 
        
def calcCogs(subTotals):

    cogs = iterateSubtotals(subTotals)
    return cogs
#def caclGrossMargin():
#TODO: move to new  module]
#---
    
# Balnace sheet [static ] methods 

def isEqual(totalAssets, totalLiabilities, totalEquity ): # +
    """
     Applies the `Accounting Equation`
    Assets  = Liabilities + Equity
    """ 
    condition = totalAssets + totalLiabilities == totalEquity
    return condition 

def getDifference(LHS2, RHS2): # - 
    """for networth 
        totalAssets + totalLiabilities == totalEquities """
    return abs(LHS2) - abs(RHS2)

def setRhsLhs(totalAssets, totalLiabilities, totalEquities ): #+ 
    """ sets the left & right, for the Cliassical Accounting Equation : A = L + E """
    LHS =  totalAssets
    RHS =  totalLiabilities + totalEquities

    return abs(LHS) - abs(RHS)

def getDifference2(totalAssets, totalLiabilities, totalEquities ): #+
    # totalAssets + totalLiabilities) == totalEquities
    return setRhsLhs(totalAssets, totalLiabilities, totalEquities )

# Note: setRhsLhs (getDifference) != getNetWorth as:

#Rule1: totalAssets + totalLiabilities) == totalEquities
# Rule2: Networth: totalAssets - totalLiabilities == totalEquities

def getNetWorth(totalAssets, totalLiabilities): #ok 

    """  calculates `NetWorth` (original):
         NetWorth = totalAssets - totalLiabilities  ( == totalEquities ) """
    LHS = totalAssets - totalLiabilities  # Rule: `Networth == totalEquities
    RHS = totalEquities
    return abs(LHS) - abs(RHS) # setRhsLhs(totalAssets, totalLiabilities, totalEquities)

def isNetworth(totalAssets, totalLiabilities, totalEquities): #New

    return (totalAssets + totalLiabilities) - totalEquities

def verifyNetWorth1(totalAssets, totalLiabilities, networth): #TODO: appply flip of `networth` parameter in implementation

    """ verifies `NetWorth, by comparing it with `totalAssets` and `totalLiabilities` """
    # networth = totalAssets -  totalLiabilities == totalEquities [both sides should be equal]
    condition = networth  == getNetWorth(totalAssets, totalLiabilities) # totalAssets -  totalLiabilities
    return condition 

def verifyNetWorth2(networth, totalEquities ,ErrorMsg="Exception Raised: Value Error, please check all inputs, then retry"):

    """verifies `NetWorth`against `totalEquities`
    - Hint: NetWorth (in business) is also referred to as Equity
    - Applying the 3 condition logic: if, elif, else (raises an  Error) 
    - with error handling: `ValueError` exceptions 
    """
    try:
        condition = networth == totalEquities  #networth>0 and totalEquities > 0
        if condition == False:
            #pass
            return condition
        elif condition == True:
            pass
            #condition = networth == totalEquities #True (or False)
            return condition

        else:
         raise ValueError("Please Check Input then try again, later")

    except ValueError:
        print(ErrorMsg)
    
def printIsEqual(totalAssets, totalLiabilities, totalEquity ):
    """ Applying the accounting Equation : A = L + E
    """
    RHS = totalAssets
    LHS = totalLiabilities + totalEquity
    
    print("totalAssets = ",totalAssets)
    print("totalLiabilities = ",totalLiabilities)
    print("totalEquity = " , totalEquity)

    print("LHS = ", LHS)
    print("RHS = ", RHS)
    
    boolIsEqual = printIsEqual2()

def printIsEqual2(LHS, RHS):

    """ checks if both sides are equal: an alternative way that accountance use to verify accounts
        - by  calculating Owner's networth = Assets - Liabilities)

        #delete?: ins suntrating RHS from LHS :
        """
    condition = RHS == LHS
    return condition

RHS = totalAssets 
LHS =  totalLiabilities + subTotalEquities2020

print("RHS ==  LHS = ",RHS ==  LHS)
RHS ==  LHS

equals = isEqual(totalAssets, totalLiabilities, totalEquities)

print("Accounts equal = ", equals ) 

print(" Right side = ",RHS)
print(" Left side = ",LHS)

print()
print("Difference = ", LHS-RHS) # TODO: also do accounts balance (i.e. equal 0 )
print("Accounts Balnce : totalAssets + totalLiabilities  = totalEquity \n",
                "Right hand: Assets  = ",RHS, "\n" , "  ", "Left hand side =  Liabilities + Equity ", LHS,  ) 

print("try1: is equal = ",isEqual(totalAssets, totalLiabilities, totalEquities ))

#1. Data Handling

# Example APPLE INC
## Consolidated Balance Sheet
# source: https://www.investopedia.com/terms/b/balancesheet.asp


#1.1 current Assets 
ca2020 = [38016, 52927, 16120, 4061, 21325, 11264]
subtotal1 = iterateSubtotals(ca2020)
print(subtotal1)

#1.2. nonCurrent Assets
nca2020 = [100887, 36766, 42522]
subtotal2 = iterateSubtotals(nca2020)
print(subtotal2)

#2. Total Assets:
totalAssets = subtotal1 + subtotal2
print("total Assets", totalAssets) # 323888

#--
#1.1 currentLiabilities 
cL2020 = [42296, 42684, 6643, 4996, 8773]
subtotalL1 = iterateSubtotals(cL2020)
print(subtotalL1)

#1.2 nonCurrent Liabilities 
ncL2020 = [98667, 54490]
subtotalL2 = iterateSubtotals(ncL2020)
print(subtotalL2)
#2. Total Liabilities
totalLiabilities = subtotalL1 +subtotalL2 
print("total Liabilities", totalLiabilities) # 258549

#Capital [ (Owner's) Equity ]

#1. Current Equities
equity2020 = [50779, 14966, -406]
#2. Total Equities
totalEquities = iterateSubtotals(equity2020)

print("totalEquities = ", totalEquities) # 65339
#--
# 2. Information Processing

# 2.1 isEqual(totalAssets, totalLiabilities, totalEquity) 
_flag_isequal = isEqual(totalAssets, totalLiabilities, totalEquities) #isEqual()

## print("Accounts (in the accounting equation RHS = LHS : Assets+Liabilities = Equity",_flag_isequal)

# 2.2. getDifference2(totalAssets, totalLiabilities, totalEquity)
diff = getDifference2(totalAssets, totalLiabilities, totalEquities)
## print("difference = ", diff)

assets = 302083 #352755

liabilities  = 152452 # 302083
equity = 149631

_flag_accepted = isEqual(assets, liabilities, equity ) # isEqual()
print("is equal = ", _flag_accepted)
_diff = getDifference2(assets, liabilities, equity)
print("difference : ", _diff)



# As always, there is stucture, just like in everything else
# 
class balanceSheet:
    """
    balance is time oriented, usually a  year ( in which we would stick to it ) 
    we can do a balance at any given moment, se we can get a gist of what we have, and do not have
    , the this we owe  to others,
    the things others owe to us

    finally, balance is important, as from it,we can get to the 
    """

    #Helper functions:
    # iterateSubtotals
    def iterateSubtotals(self,subTotals,printFunction=None):

        _sum = 0
        for item in subTotals:
            _sum += item

        return _sum
    
    def __init__(self, year : int, proprietor : str):
        """ at each triad, there is a Duo """

        self.proprietor = proprietor
        self.year = year
        
        #the sacred Triad of a BalanceSheet:
        
        #self.Assets : 
        # which is defined by the Duo:
        self.totalAssets = 0
        self.currentAssets = []
        self.nonCurrentAssets = []

        self.currentAssetsSubTotal = 0
        self.nonCurrentAssetsSubTotal = 0
        self.totalAssets = self.currentAssetsSubTotal + self.nonCurrentAssetsSubTotal  #0
        # which is defined by the Duo:
        
        self.currentLiabilities = []
        self.nonCurrentLiabilities = []

        self.currentLiabilitiesSubTotal = 0
        self.nonCurrentLiabilitiesSubTotal = 0
        self.totalLiabilities = self.currentLiabilitiesSubTotal + self.nonCurrentLiabilitiesSubTotal #0
        #self.equity
        # which is defined by the Duo:
        
        self.currentEquities = []
        #self.nonCurrentEquity = []
        self.currentEquitesSubTotal = 0
        #self.nonCurrentEquitySubTotal = 0

        #Now: totalEquities == currentEquitiesSubtotal
        self.totalEquities =  self.currentEquitesSubTotal #0

    def __init__2(self, year : int, proprietor : str, currentAssets,nonCurrentAssets,currentLiabilities, nonCurrentLiabilities,
                  currentEquities):
        """ at each triad, there is a Duo """

        self.proprietor = proprietor
        self.year = year
        
        #the sacred Triad of a BalanceSheet:
        
        #self.Assets : 
        self.totalAssets = 0
        
        # which is defined by the Duo:
        self.currentAssets = currentAssets #[]
        self.nonCurrentAssets = nonCurrentAssets #[]

        self.currentAssetsSubTotal = self.iterateSubtotals(self.currentAssets)
        self.nonCurrentAssetsSubTotal = self.iterateSubtotals(self.nonCurrentAssets)
        self.totalAssets = self.currentAssetsSubTotal + self.nonCurrentAssetsSubTotal

        #self.Liabilities
        self.totalLiabilities = 0

        # which is defined by the Duo:
        self.currentLiabilities = currentLiabilities #[]
        self.nonCurrentLiabilities = nonCurrentLiabilities # []

        self.currentLiabilitiesSubTotal = self.iterateSubtotals(self.currentLiabilities) 
        self.nonCurrentLiabilitiesSubTotal = self.iterateSubtotals(self.nonCurrentLiabilities) 
        self.totalLiabilities = self.currentLiabilitiesSubTotal + self.nonCurrentLiabilitiesSubTotal 

        #self.equity
        # which is defined by the Duo:
        
        self.currentEquities = currentEquities #[]
        #self.nonCurrentEquity = []
        
        self.currentEquitesSubTotal = self.iterateSubtotals( self.currentEquities ) #0
        #self.nonCurrentEquitySubTotal = 0
        
        #Now: totalEquities == currentEquitiesSubtotal
        self.totalEquities =  self.currentEquitesSubTotal #0
            
    
    # get totals (easy path , Impractical ) 

    def getTotalAssets(self, _currentAssetsSubTotal, _nonCurrentAssetsSubTotal):
            #1. Assign
            self.currentAssetsSubTotal = _currentAssetsSubTotal
            self.nonCurrentAssetsSubTotal = _nonCurrentAssetsSubTotal

            #2. Add 
            self.totalAssets = self.currentAssetsSubTotal + self.nonCurrentAssetsSubTotal

            #3. Return 
            return self.totalAssets

    def getTotalLiabilities(self, currentLiabilitiesSubTotal, nonCurrentLiabilitiesSubTotal):
            #1. Assign 
            self.currentLiabilitiesSubTotal = currentLiabilitiesSubTotal
            self.nonCurrentLiabilitiesSubTotal = nonCurrentLiabilitiesSubTotal

            #2. Add 
            self.totalLiabilities = self.currentLiabilitiesSubTotal +  self.nonCurrentLiabilitiesSubTotal

            #3. Return 
            return self.totalLiabilities

    def getTotalEquities(self, currentEquitySubTotal ) : #, nonCurrentEquitySubTotal):
            """ Assigns  currentEquitySubtotal """ 
            #1. Assign 
            self.currentEquitiesSubTotal = currentEquitySubTotal
            # self.nonCurrentEquitySubTotal = nonCurrentEquitySubTotal
            #2. Assign #Add 
            self.totalEquities = self.currentEquitiesSubTotal  # +  self.nonCurrentEquitySubTotal
            #3. Return 
            return self.totalEquities

   # def getTotalEquityTotal2(self, ):

        # Update Asset
        ## Update Current Asset
    def updateCurrentAssetList(self, currentAssets):
             self.currentAssets = currentAssets
             return self.currentAssets
        # Update `_currentEquities`
        ## Update Current `_currentEquities`
    def updateCurrentEquityList(self, _currentEquities):
        """ updates a list of `_currentEquities` elements  """
        self.currentEquities = _currentEquities
        #As: a part of calculation, find `CurrentEquitiesSubtotal`
        self.calcCurrentEquitiesSubtotal(_currentEquities)
        #As: TotalEquities == currentEquities
        
        self.currentEquities= _currentEquities # calculate `currentEquity`
        self.totalEquities = iterateSubtotal(_currentEquities) #calculate totalEquities
        return self.currentEquities
        """
        ## Update NonCurrent Equity 
        def updateNonCurrentEquity(self, nonCurrentEquity):

            self.nonCurrentEquity = nonCurrentEquity
            return self.nonCurrentEquity
        """
        #Better Approach:
        
        #CalcAssets
        ## calcCurrentAssetsSubTotal
        
    def calcCurrentAssetsSubTotal(self,currentAssets):

            """ calculates  nonCurrentEquity Subtotal """
            #1. Assign `currentAssets` list
            self.currentAssets = currentAssets

            #2. Calculate `currentAssetsSubTotal`
            self.currentAssetsSubTotal = self.iterateSubtotals(self.currentAssets)
            #3. Return self.currentAssetsSubTotal
            return self.currentAssetsSubTotal

        ## calcNonCurrentAssetsSubTotal
    def calcNonCurrentAssetsSubTotal(self,_nonCurrentAssets):

            """ calculates  nonCurrentEquity Subtotal """
            #1. Assign `currentAssets`
            self.nonCurrentAssets = _nonCurrentAssets

            #2. Calculate `nonCurrentAssetsSubTotal`
            self.nonCurrentAssetsSubTotal = self.iterateSubtotals(self.nonCurrentAssets)

            #3. Return `nonCurrentAssetsSubTotal` figure
            return self.nonCurrentAssetsSubTotal

    def calcAssets(self, _currentAssets, _nonCurrentAssets): #Debug #modify

            #1. call calcCurrentAssetsSubTotal
            #currentAssetsSubTotal
            self.calcCurrentAssetsSubTotal(_currentAssets)

            #2. call `calcNonCurrentAssetsSubTotal
            self.calcNonCurrentAssetsSubTotal(_nonCurrentAssets)

            #3. Add results to `self.totalAssets`
            self.totalAssets =  self.currentAssetsSubTotal + self.nonCurrentAssetsSubTotal   #self.currentAssets + self.nonCurrentAssets

            return self.totalAssets

    #CalcLiabilities

    ## CalcCurrentLiabilities

    def calcCurrentLiabilitiesSubTotal(self, _currentLiabilities):
            """ Calculates `currentLiabilities` Subtotal """

            # 1. Assign `currentLiabilities` list
            self.currentLiabilities = _currentLiabilities

            # 2. Assign `currentLiabilitiesSubTotal` figure

            self.currentLiabilitiesSubTotal = self.iterateSubtotals(self.currentLiabilities)

            # 3. Return `currentLiabilitiesSubTotal` figure
            return self.currentLiabilitiesSubTotal

    def calcNonCurrentLiabilitiesSubTotal(self, _nonCurrentLiabilities):

        """ Calculates `currentLiabilities` Subtotal """
        # 1. Assign `currentLiabilities` list
        self.nonCurrentLiabilities = _nonCurrentLiabilities

        # 2. Assign `NonCurrentLiabilities` figure
        self.nonCurrentLiabilitiesSubTotal = self.iterateSubtotals(self.nonCurrentLiabilities)

        # 3. Return `currentLiabilitiesSubTotal` figure
        return self.nonCurrentLiabilitiesSubTotal

    def calcTotalLiabilities(self, _currentLiabilities, _nonCurrentLiabilities ):  
        """
            1.Calculates `currentLiabilitiesSubTotal` by summing up _currentLiabilities)
            2.Calculates `nonCurrent
        """
        #1. call calcCurrentAssetsSubTotal
        self.calcCurrentLiabilitiesSubTotal(_currentLiabilities)

        #2. call `calcNonCurrentAssetsSubTotal`
        self.calcNonCurrentLiabilitiesSubTotal(_nonCurrentLiabilities)

        #3. Add results to `self.totalAssets`
        self.totalLiabilities = self.currentLiabilitiesSubTotal + self.nonCurrentLiabilitiesSubTotal

        return self.totalLiabilities
        
    def calcLiabilities(self, _currentLiabilities,_nonCurrentLiabilities):

            self.calcTotalLiabilities(_currentLiabilities, _nonCurrentLiabilities)
            return self.totalLiabilities

    def getTotalLiabilities(self):
        if  self.totalLiabilities is None:
            raise ValueError("Inappropriate value for `totalLiabilities`")
        return self.totalLiabilities


    def calcEquities(self,_currentEquities): #TODO: ERRONeous (Change) 
        
        if self.currentEquities is None:#not self.currentEquities is None:
            
            self.getEquities(_currentEquities) #call 
            #self.currentEquities = self.iterateSubtotals(iterateSubtotals)#calcCurrentEquities(_currentEquities)
            #self.totalEquities = getEquities(_currentEquities) #calcCurrentEquitiesSubtotal(_currentEquities)  #self.currentEquities
        return self.totalEquities
    
    def calcCurrentEquitiesSubtotal(self,_currentEquities):

        """Assigns `currentEquities` list, calculates the figure of `nonCurrentEquity` Subtotal """
        
        # 1. Assign to `currentEquities` 
        self.currentEquities = self.iterateSubtotals( _currentEquities)
        self.totalEquities = self.currentEquities 
        #2. currentEquitiesSubTotal
        self.currentEquitiesSubTotal =  self.currentEquities

        #3. Return subTotal
        return self.currentEquitiesSubTotal

    def getcurrentEquities(self):
        """
            1. Gets back a list of equiities
            2. Calculates their subtotal ,
            3. Then returns it
    
        """
        
        return self.currentEquitiesSubTotal
    
    def getTotalEquities(self):

        if self.currentEquitiesSubtotal is None: #not self.currentEquitiesSubtotal is None:
            self.totalEquities = self.currentEquitiesSubTotal
            
        return self.totalEquities

    def getTotalEquities2(self, totalEquities):
        """overrides totalEquities """
        
        self.totalEquities = totalEquities
        return self.totalEquities 

     # lvl1

    # Working Capital  
    def workingCapital(self):
        """
        1. A Short-Term measure: of overall liquidity (source:https://www.causal.app/whats-the-difference/working-capital-vs-net-working-capital)
        2.Working capital is the amount of money used to facilitate the operations of the business.
        calculated by:
         Current Assets less Current Liabilities.

         pros:
         1.allows to set short term -goals
         (by meeting short-term obligations (i.e. current Liabilities, within a year)

         pros : of being
         working capital position
         "Strong Working Capital" position,
         it may be able to take advantage of a supplier's
         
         -it's ( possible to ) extend Debt terms from 30 to 60 days.
         This would free up cash ( that could be
         used for other purposes.)

         cons:
         1. a large capital may mean that lots of assets are stored
         in a form of inventories (in warehouses, instead of liquid cash)
         thus, it is less likeliky to take advantage of opportunities,
         requiring "quick cash investment"
         
        """

        self.workingCapital = self.currentAssetsSubTotal - self.currentLiabilitiesSubTotal

        return self.workingCapital

    # Net Worth


    def calcNetWorth(self): # takes 0 parameters

        """
        - A Long-Term measure: of Proprietor's overall `liquidity`
        Note: the sucess of running this function tightly depends on whether  we have previously calculated the `subTotals` of both: Assets, liabilites
            (otherwise, it wouldn't function, as expected)
        - is also called : the `Net Working Capital`

        pros: advantages over working capital
        1. provides a big pitcture of proprietor's liquidity,
        taking into account both
        1.1 short-term
        1.2 long-term obligations
        2. it is a forward-looking measure:
        it includes all of proprietor's assets (not only short-term ones)
        Infer: thus, it provides a more comprehensive picture of proprietor's value

        cons:
        It may give a `False Sense of Security`
        Because proprietor's overall liquidity can  drastically change, (i.e. forex) from 1 timestamp, to another` 
        (?)
        
        
        """

        #get assets and liabilities , assign them to NetWorth

        self.NetWorth = abs(self.totalAssets) - abs(self.totalLiabilities)  #self.totalAssets - self.totalLiabilities

        return self.NetWorth
    
    def calcNetWorth2(self, _totalAssets, _totalLiabilities):

        self.totalAssets = _totalAssets
        self.totalLiabilities = _totalLiabilities
        self.NetWorth = _totalAssets - _totalLiabilities 

        return self.NetWorth
    
    def calcNetworth3(self, _currentAssets, _nonCurrentAssets, _currentLiabilities, _nonCurrentLiabilities): # ok

        # 1 calc totalAssets
        self.calcAssets( _currentAssets, _nonCurrentAssets )

        #2. calc totalLiabilities
        self.calcLiabilities(_currentLiabilities,_nonCurrentLiabilities) # this should also compile

        #3. calc NetWorth
        self.NetWorth =  self.totalAssets - self.totalLiabilities

        return self.NetWorth
    
    # Verify Net Worth
    def verifyNetworth(self):
        condition  = self.NetWorth == self.Equities
        return condition
    def verifyNetworth2(self):
        condition = self.getDifference() == 0

    def getEquities(self, _currentEquities):
        
            self.currentEquities = self.iterateSubtotals(_currentEquities)#calcCurrentEquitiesSubtotal(_currentEquities) 
            self.totalEquities = self.currentEquities
            return self.totalEquities
            

    def calcEquities(self,_currentEquities): #TODO: ERRONeous (Change) 
        
        #if self.currentEquities is None:#not self.currentEquities is None:
            
        self.getEquities(_currentEquities) #call 
            #self.currentEquities = self.iterateSubtotals(iterateSubtotals)#calcCurrentEquities(_currentEquities)
            #self.totalEquities = getEquities(_currentEquities) #calcCurrentEquitiesSubtotal(_currentEquities)  #self.currentEquities
        return self.totalEquities

        def calcCurrentEquities(self, _currentEquities):

            #1. call`getEquities` calc currentEquities Subtotal (from `_currentEquities` list ) 
            self.getEquities(_currentEquities)
            #self.currentEquities =  self.calcCurrentEquitiesSubtotal(_currentEquities)  
            #self.totalEquities = self.currentEquities 
            return self.currentEquities
    
    def calcTotalEquities(self, _currentEquities): # checked parameter name

        self.totalEquities = self.iterateSubtotals(_currentEquities) #calcCurrentEquitiesSubtotal(_currentEquities) 
        return self.totalEquities

    def getEquities2(self):
        return   bSheet2.calcEquities() # bSheet2.currentEquities # bSheet2.calcEquities()

    def getTotalEquities(self):
        """ returns totalEquities (from current """
        if not self.currentEquities is None:
            self.totalEquities = self.CurrentEquities 
        return self.totalEquities

    
    def verifyNetWorth(self): #,_networth):
        """ Compares Networth with total Equities """
        condition = self.NetWorth == self.totalEquities
        return condition
    
        if  condition == True: #== #totalEquities:
            return True
        elif _networth != totalEquities:
            return False
        else: raise ValueError("Please Check Input then try again, later")

    def setTitle( self, title="Consolidated Balance Sheets", optionalDesc=None):

        if not optionalDesc is None:
            self.description = optionalDesc

        self.title = title
        return title


    def getDifference(self):
        """ in best cases: difference =0 and all 3 major accounts
        (totalAssets, totalLiabilities, totalEquities)
        balances out """

        LHS = self.totalAssets - self.totalLiabilities 
        RHS = self.totalEquities

        diff = abs( LHS) - abs(RHS) #abs(LHS) - abs(RHS)
        return diff    

    def getAccountingEquation(self):
        """ Assets = Liabilities + Equities => Assest - (RHS) 
in best cases: difference =0 and all 3 major accounts
        (totalAssets, totalLiabilities, totalEquities)
        balances out """

        LHS = self.totalAssets 
        RHS = self.totalLiabilities + self.totalEquities

        diff = abs( LHS - RHS) #abs(LHS) - abs(RHS)
        return diff

        
# DEMO

# Example : applying balance sheet of APPL
# source: https://www.investopedia.com/terms/b/balancesheet.asp
# For the year 2020

totalAssets = 323888
totalLiabilities = 258549
totalEquities = 65339 # totalEquity 
_equals = isEqual(totalAssets, totalLiabilities,  totalEquities)
print("Equals = ", _equals )

#LHS [Assets] , RHS[ Liabilities + Equities]
print( "difference = ", getDifference(totalAssets, totalLiabilities + totalEquities) )
# difference ( Assets, Liabilities, Equity)
accountDifference = getDifference2(totalAssets, totalLiabilities , totalEquities)

print( "difference3 = ", accountDifference )

# Another way: which accountants How: "checking Net Worth = Assets - Liabilities "
_networth = getNetWorth(totalAssets, totalLiabilities) #

print("Net Worth = ", _networth)

# NetWorth ?= Equity 

##isNetWorthVerified = verifyNetWorth1(_networth)
#isNetWorthVerified = verifyNetWorth2(_networth, totalEquity)

##print("NetWorth Verified: ", isNetWorthVerified)
# DEMO : class utilization: `bSheeet` (balance sheet)

print("Demo:  class Demo , of APPL 2022")

# Balance sheet, year , title
# At start: set a Title and a year, for the `BalanceSheet`
bSheet= balanceSheet("2020", "APPLE INC `APPL`")

#Assets
## Current Assets

ca2020 = [38016, 52927, 16120, 4061, 21325, 11264] #current Asset list (2020) 

## Current Assets
nca2020 = [100887, 36766, 42522] # non-current Asset list (2020)

## Current Liabilities
cl2020 = [42296, 42684, 6643, 4996, 8773] #current-liabilitiy list 2020)
## non-Current Assets
ncl2020 = [98667, 54490]    # non-current liability list (2020)

## Equities 2020
equities2020 = [50779, 14966, -406] #current-Equity list (2020)

# 
#SubTotals:
#1. currentAssets
currentAssetsSubTotal = bSheet.calcCurrentAssetsSubTotal(ca2020)
print("currentAssetsSubTotal = ", currentAssetsSubTotal)

#2. nonCurrentAssets' Subtotal
nonCurrentAssetsSubTotal = bSheet.calcNonCurrentAssetsSubTotal(nca2020)
print("nonCurrentAssetsSubTotal = ", nonCurrentAssetsSubTotal)

#3. currentLiabilities' Subtotal
print("bSheet.calcCurrentLiabilitiesSubTotal( cL2020) = ", bSheet.calcCurrentLiabilitiesSubTotal( cl2020) )

#non-current Liabilities' Subtotal
print("bSheet.calcNonCurrentLiabilitiesSubTotal(ncL2020)  = ",bSheet.calcNonCurrentLiabilitiesSubTotal(ncl2020))

#currentEquity Subtotal
print("bSheet.calcCurrentEquitiesSubtotal(equities2020)  = ",bSheet.calcCurrentEquitiesSubtotal(equities2020))

#User can also view CurrentAsset Subtotal
print("bSheet.currentAssetsSubTotal = ", bSheet.currentAssetsSubTotal )


#Totals
# A user can: 
# 1.TotalAssets
#1. Calculate the Assets' `Total` by calcAssets(currentAssets, nonCurrentAssets)
totalAssets = bSheet.calcAssets(ca2020,nca2020 )
print("totalAssets = ", totalAssets)

# 2.TotalLiabilities
#2. Calculate the Liabilities' `Total by `calcTotalLiabilities(currentLiabilities, nonCurrentLiabilities)
totalLiabilities = bSheet.calcTotalLiabilities(cL2020, ncL2020)
print("totalLiabilities = ", totalLiabilities)

#3. TotalEquities
#3. Calculate the Equiries' `Total` by `calcEquities(currentEquity)`
#error: takes 1 positional argument but 2 were given
Equities = bSheet.calcEquities(equity2020) # calcEquities(equity2020) 
print("Equities =", Equities) 
#end of Lvl 0

#lvl1: Analysis
#1. Working Capital

workingCapital = bSheet.workingCapital() # #no error (check why)

print("workingCapital = ", workingCapital)

#2. Net Worth

bSheet.calcNetWorth2(totalAssets, totalLiabilities)
print("bSheet.NetWorth = ",bSheet.NetWorth)

#Is NetWorth

IsNetWorthVerified = bSheet.verifyNetWorth() #bSheet.NetWorth) #should compile 
print("IsNetWorthVerified = ", IsNetWorthVerified)
# IsNetWorth = bSheet.verifyNetWorth(_networth, totalEquities) # bSheet.verifyNetWorth()


# DEMO2:
#PS. in this example: current Assets seems to be missing exactly 2$ only

#Source: https://www.investopedia.com/ask/answers/09/does-balance-sheet-always-balance.asp
# the lists `XYearnames`, `xYear` to be zipped , as a dictionary at the end  
ca2017names = ["Cash & Cash equivalents", "Short-term marketable Securities",
          "Accounts recievable, less alloances of 58 and 53 respectively",
          "Inventories", "vendor non-trade Recievables", "Other Current Assets"]
# Added 2 dollars: 1$ for cash, 1$ for "vendor non-trade Recievables

ca2017 = [20290, 53892, 17874, 4855, 17800, 13936]#[20289, 53892, 17874, 4855, 17799, 13936]
nca2017names = ["Long-term Marketable Securities","Property, Plant , Equipment,net", "Goodwill",
                "Acquiried Intangible Assets, net", "other Non-Current Assets"]
nca2017 = [194714, 33783, 5717, 2296, 10162]

cl2017names=["Accounts payable","Accrued Expenses", "Deferred Revenue", "Commercial Paper", "Current portion of long-term Debt"]
cl2017 = [49049, 25744, 7548, 11977, 6496]

ncl2017names = ["Deferred revenue, non-current", "Long-term Debt",
                "Other, Non-Current Liabilities"]
ncl2017 = [2836, 97207, 40415]

## Equity 2017
equity2017 = [35867, 98330, -150] #current-Equity list (2017)

#(static) balanceSheet methods

# 1. constructor: balanceSheet(year: int, proprietor : str) 
bSheet2 = balanceSheet(2017,proprietor="APPLE INC APPL")

# 2. setTitle( title : str )
bSheet2.setTitle("Consolidated Balance Sheets","(in millions, except number of shareswhich are reflected in thousands and per value")

#SubTotals:

#1. currentAssets
currentAssetsSubTotal = bSheet2.calcCurrentAssetsSubTotal(ca2017)
print("currentAssetsSubTotal = ", currentAssetsSubTotal)

#2. nonCurrentAssets' Subtotal
nonCurrentAssetsSubTotal = bSheet2.calcNonCurrentAssetsSubTotal(nca2017)
print("nonCurrentAssetsSubTotal = ", nonCurrentAssetsSubTotal)

#3. currentLiabilities' Subtotal
print("bSheet.calcCurrentLiabilitiesSubTotal( cL2020) = ", bSheet2.calcCurrentLiabilitiesSubTotal( cl2017) )

#4.non-current Liabilities' Subtotal
print("bSheet.calcNonCurrentLiabilitiesSubTotal(ncL2020)  = ",bSheet2.calcNonCurrentLiabilitiesSubTotal(ncl2017))

#currentEquity Subtotal
#User can also view CurrentAsset Subtotal
print("bSheet.currentAssetsSubTotal = ", bSheet2.currentAssetsSubTotal ) #TODO: currentEquitiesSubtotal()


#Totals
# A user can calculate: 
# 1.TotalAssets
#1. Calculate the Assets' `Total`: calcAssets(currentAssets, nonCurrentAssets)
totalAssets = bSheet2.calcAssets(ca2017,nca2017 )
print("totalAssets = ", totalAssets)

# 2.TotalLiabilities
#2. Calculate the Liabilities' `Total: `calcTotalLiabilities(currentLiabilities, nonCurrentLiabilities)
totalLiabilities = bSheet2.calcTotalLiabilities(cl2017, ncl2017)
print("totalLiabilities = ", totalLiabilities)

#3. TotalEquities
#3. Calculate the Equities' `Total`: `calcEquities(currentEquity)`
Equities = bSheet2.calcEquities(equity2017) # calcEquities(equity2020) 
print("Equities =", Equities) 
#End of [Lvl 0]

#[lvl1: Analysis]

#1. Working Capital
workingCapital = bSheet2.workingCapital() #compiles
print("workingCapital = ", workingCapital)

#2. Net Worth
#2.1 calcNetWorth(): #Note: pre-supposes both `totalAssets`, `totalLiabilites` been: calculated,& stored in  `balanceSheet` instance [if not, use the other function]
#2.2 calcNetWorth(totalAssets, totalLiabilities)
bSheet2.calcNetWorth2(totalAssets, totalLiabilities)
print("bSheet.NetWorth = ",bSheet2.NetWorth)

#3. verifyNetWorth()
IsNetWorthVerified = bSheet2.verifyNetWorth() #bSheet2.NetWorth) # compiles 
print("IsNetWorthVerified = ", IsNetWorthVerified)


#4. getDifference()
print("Difference(Assets - (liabilities+ Equities) = ",bSheet2.getDifference() )
#5.
print("bool is the same (getDifference() ==0)? = ", bSheet2.getDifference() == 0 )
# calcEquities
print("1. bSheet2.calcCurrentEquitiesSubtotal(equity2017) = ",bSheet2.calcCurrentEquitiesSubtotal(equity2017)) # returns a list (of equities) 
print("2. bSheet2.currentEquities = ",bSheet2.currentEquities)
print("3. bSheet2.getEquities = ", bSheet2.getEquities(equity2017))#TODO

print("bSheet2.NetWorth == bSheet2.calcEquities(equity2017)",bSheet2.NetWorth == bSheet2.calcEquities(equity2017))

# print("difference of difference" , abs(bSheet2.getDifference()) - bSheet2.verifyNetWorth() == bSheet2.calcEquities(equity2017) )  # False 
#print("difference of difference" , abs(bSheet2.getDifference()) - bSheet2.verifyNetWorth() == bSheet2.calcEquities() )  #bSheet2.NetWorth(NetWorth) == bSheet2.calcEquities() )
#TODO:

#1. check function  `calcEquities`
# takes one Input argument: calcEquities(_currentEquities)

#2. ensure function `getEquities` ,adding an attribute  `self.totalEquities`  (instead of the hassle of re-calculating `calcEquities(_currentEquities)` )

#The End

## def getEquities(self):
##     return   self.calcEquities()  # bSheet2.currentEquities # bSheet2.calcEquities() #not currentEquities (list of Equities)

#Extra:
#class `printReport`
#Encapsulates function above (including their different `lvl`s : lvl0, lvl1

class printReport:
    def __init__(bSheet):
        pass # encapsulates the `printed values` above 

class StockholderEquity: 
    """ - The Capital 
        - Stock holder equity:

    1. proprietor: is 1. `personal` 2. `smallBusiness` 3. `company` (or so) #TODO:enum
    
    2. calculated from :
    2.1. retainedEarnings : from the balances brought forward, at the start of each month (for the monthly) , Quarter (for the Quarterly) , year (for the Annual) Balance Sheet
    2.2. capitalStock[if proprietor is a `listed-company` ]: current number of shares in the market
    2.3. Gains losses: calculated from: generating the Report: `Income Statement` (or the `Statement of Comprehensive Income`) Report's **Ending** figure, for a specific period (of time).
         # In the following Scenarios: whether `User` is: a person (or even a company, in the case of a `small-business`, single proprietorship, or partnership )
         # Whether they have incurred Gains (above break-even `0` ) or Incurred Losses (went below the Break-even point `0`)
         # Hence the requirement for an `IncomeStatement` that boils down a year of Operations, including All -Immediate- Expenses Incurred, & `Gains` Realized, for specified period (month, Quarter, annum (year) ).
         
    """

    class CapitalStock:

        def __init__(self, capitalStock):
            self.capitalStock = capitalStock
                # pass

    class CommonStock(CapitalStock):

        def __init__(self, commonStock):
            self.commonStock = commonStock 
                # pass 

        def __init__(self,capitalStock, retainedEarnings,GainsLosses):
            """ Pass-in:
            1.capital stock (from )
            2. retainedEarnings: earnings in a period, that stays in buisness for further circulation, to capture and maximize benefits
            - Note: [Tutor: Krassimir Petrov]: Also Account for `Dividends ( A company must set ); a `portion` from retained Earnings , given to `stockholders` #TODO
            - Dividends: in otherwords, it is a contra-account [me:negative-Account] of `retainedEarnings` Account : an
            that we (ethically) let go off , for the sake of `stockholders` ownerships of our `company`
            
            self.capitalStock = capitalStock
            self.retainedEarnings = retainedEarnings
            self.GainsLosses = GainsLosses
            # pass

            def calcStockHolderEquity(self):
                self.StockholderEquity =  self.capitalStock + self.retainedEarnings + self.GainsLosses
            """
