"""
#Accounting Rules:
## Rule1: Accounting Equation: totalAssets                     == totalLiabilities + totalEquities
## Rule2: NetWorth           : totalAssets - totalLiabilities  == totalEquities
##Note: the equations above are equivalent, in addition.

## Rule3: bookValue of totalEquities calculated by : totalAssets less totalLiabilities. if its value is different than `totalEquities`
        If that is the case, then further `Auditing` Might be required (to discover the source of error, and `mis-balanced` accounts, in Accounting ).


"""
class partialEntry:

    # 5.1.1. Using Lists as Stacks
    """ 
    The list method` make it is easy to use a list as a stack,
    where the last element added at the first, element ( that is  retrieved ) 
    (“last-in, first-out”). To add an item to the top of the stack, use append().
    -To retrieve an item from the top of the stack,
    -use pop() without an explicit index. For example:

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

        {'cash': 2000, 'AccountsRecievable': 5000, 'bankAccount': 10000}
        """
    def print():
        pass
        #   for i, v in enumerate(['one', 'two', 'three']):
        #        print(i, v)


#Idea:
class partialEntry:
    """ Captures a specific part of a `transaction` which can  either assume the  drSide or the crSide
    Purpose: acts as a bridge, between a `Report` (balanceSheet in this module`)and a `Transction` (of a Journal Entry )

    - Hint: when we interact with a `Transaction`, we only need a part of it: let it be its Debit Side ( or its Credit Side).
    
    -If we could only add that, as a function, in a transaction class, instead,
        then, we would have made things more "Straight-Forward, & easy
        (For all users: developers & end-users alike)
    """

    def __init__(self, drSide, crSide, amount, isDebit=True, MsgError="Unexpected Error Occured, please recheck input, then retry"):

        # Check `isDebit` flag , if so, return the ``drSide` Object & the amount
        if isDebit == True:
            self.transactionSide = drSide
            self.amount = amount
            # return self.transactionSide, self.amount
        # otherwise, return `crSide` and the amount provided (in the consructor )
        elif isDebit == False:
            self.transactionSide = crSide
            self.amount = amount
            #return self.transactionSide, self.amount
            
        else:
            raise ValueError(MsgError)

       #in a constructor, cannot return ,thus, we create a function getTransactionSide, returns above are both equal  
        
    def getTransactionSide(self):
        """ returns a transaction side, and the amount (of the `partialEntry`)
        (whether it's a debit, or a credit side)
        """
        return self.transactionSide, self.amount


# Now we can capture any part (of any transaction ) with its corresponding amount, accordingly
# Take the debit side (of a transaction) with its amount
pEntry1 = partialEntry("cash","bankAccount", 100, isDebit=True) #debitSide when `1isDebit` equals `True`
transactionside, amount = pEntry1.getTransactionSide()
print("debit Side = ", transactionside, " , amount = ", amount)

#Seemingly,take the credit side (of a transaction) with its amount
pEntry2 = partialEntry("cash","bankAccount", 100, isDebit=False) #creditside when `isDebit` equals `False`
transactionside, amount = pEntry2.getTransactionSide()

print("credit Side = ", transactionside, " , amount = ", amount) 
#E.g. for the balance sheet: we can take `cash`, add it into i.e. `currentAssetNames` list, with its amount,
# and creditside: `bankAmount` into currentEquitiesname` list with its amount, as well.
        
"""
name: str ,price : float

1. Creating a new class creates a new type of object,
2. Allowing new instances of that type to be made.
3. Each class instance can have many attributes (attached to it) for maintaining its state.
4. Class instances can also have methods (defined by its class) for modifying its state.


"""


class Report:


    dict = {} # dictionary is the not a very efficient, it holds name, and price
    # as we could possibly have endless years, going back in time, each with different values
    # It's better to zip whichever years with values, with functions, to get the subTotal 

    def iterateSubtotals(subTotals, printFunction=None):
        _sum = 0
        for item in subTotals:
            
            _sum += item
        
        return _sum
        
    
    def __init__(self, names, prices):
        pass 
    #def calcSubtotal(self):
    #    pass

    def getSubtotal(self,subTotal ):
        self.subTotal = subTotal

CAprice2020 = [38016, 52927, 16120, 4061, 21325, 11264]

# subTotalCA2020 = iterateSubtotals(CAprice2020)

subTotalCA2020 = Report.iterateSubtotals(CAprice2020)
# class-agnostic , static function


# APPL's data: @credit: : investopedia:
# image url source: https://www.investopedia.com/thmb/gUuGSjZWpXoc2miE2QfC-Z4Q6no=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/phpdQXsCD-3c3af916d04a4afaade345b53094231c.png

# Balance Sheet's "positive-side" includes the following debit accounts :
# 1. Assets : ["Cash", "marketable security", "Account recievable"
# 2. SOCI "statementt of Comprehensive Income  : "Inventories", "Vendor"
# 3. CashFlow "statement of Cash Flows"

"""
    Q. Why expense is a debit account?
    Q. Why are expenses debited?
    A. no answer [direct answer]
    Hint: `Expenses` cause `stockholder equity` to decrease

Value is not made, but is transformed, from one form to another
thus it is conserved

Dr DrAccount -> [Increase ]

#transaction Example:
##Scenario: Incremenental Transaction:

Dr cash    1000 [UP] [Asset grows]

    Cr Bank Account 1000 [UP] [(theoretical bank) Account also grows ]

#-----------

       def __ ( | context = Bank Account (Personal | owned) )

        1. bank account(virtual) grows by the Asset invested in it (cash) by 1000
        
        2. bank account is increased the same amount of cash depositied into that account

        3. This context is limited to: the (context) bank account (Personal)
        
#-----------
Dichotomy:
        Issue:
        As of result, the `pocket Money` account is now less by 1000

    def __ ( | context =`pocketMoney` Account )
    
    # `pocketMoney` Account

        # Cash on hand : becomes less (by a 1000)
        we should also write this
        As an `Expense` of opening a `bank Account` (by a  1000) [in local currency, in local time]
        
        Dr Expense 1000   [UP] [Expense Increases]
                cr Cash  1000 [Down] [Asset dimishes]
        (Comment: being payment to `top-up` a  bank account)
        
        | Context:   Pocket Money ( a liquid, personal account) 
        
    """

#incomeStatement
"""asssumes there is a salary
    and cogs (cost of goods sold)

    """

#code that bridges between partial Entry's output (value)   and a list 
# List CRUD ops:

# Create
def add(_lst, _value):
    """ adds a value to a list"""
    _lst.append(_value)
    return _lst

def Insert(_lst, _idx):
    pass

def updateAt(lst, idx=2, newValue=4):
    """ update a `newValue` by an index """
    oldIndex = idx

    #Do computation (update):

    #1. Remove the value at`oldIndex`
    lst= removebyIdx(lst, oldIndex)

    #2. Insert the `newValue` at the `oldIndex`

    lst.insert(oldIndex, newValue)
    
    #3. return `lst`
def update(lst, oldValue=3, newValue=4):
    """ Updates an `oldValue` with a new `newValue` , in a list `_lst """
    #1. store Index of `oldValue` in an `oldIndex` 
    oldIndex = lst.index(oldValue) # 1 #store old index

    #Do computation (update):

    #1. remove `oldIndex`
    lst= removebyIdx(lst, oldIndex)

    #2. insert the `newValue` at the `oldIndex`

    lst.insert(oldIndex, newValue)
    
    #3. return `lst`
    return lst


def remove(lst,_value):
    """ removes value from lst , if it exists"""
    _idx = lst.index(_value)
    if not _idx is None: 
        #remove value in a `_lst`
        del lst[_idx]
    return lst

def removebyIdx(lst,_idx):
    if not _idx is None: 
        #remove value in a `_lst`
        del lst[_idx]
    return lst

lst = [2,3]
print("lst.index(3) = ", lst.index(3))

index=3
newValue = 4

oldIndex = lst.index(3) # 1 #store old index
#Do computation (update):
#1. remove
lst= removebyIdx(lst, oldIndex)
# insert

lst.insert(oldIndex, newValue)
print("new lst = ", lst ) 


#lst.insert(lst.index(3), 4)
print("lst, post-modification= ", lst)

def update(_lst,_oldValue,_newValue):

    _ls
## class BalanceSheet(Report): # TODO: complete 

#TODO: partial Entry : depends upon it
def iterateSubtotals(subTotals, printFunction=None):
        _sum = 0
        for item in subTotals:
            
            _sum += item
        
        return _sum

#TODO: do sth useful, for the printFunction
    
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

years = [CAprice2020, CAprice2019 ] #TODO: later

## subtotalCurrentAssets2019 =  iterateSubtotals(CAprice2019) # TODO: compre with later 
## for y in years no (take in the Same Year, first


# nonCurrentAssets:

nonCurrentAssets = ["Marketable Securities", "Property, plant", "equipment net"]
nCA2020  = [ 100887, 36766, 42522]

subTotalNonCurrentAssets = iterateSubtotals(nCA2020)
print("Subtotal 2020 = ", subTotalNonCurrentAssets)

totalAssets = subTotalCA2020 + subTotalNonCurrentAssets

print("total Assets  2020 = ", totalAssets)

#lvl 2
#Ratios:

""" Ratios:
CashRatio = cash / CurrentLiabilities
CurrentRatio = CurrentAssets / CurrentLiabilities
Quick Ratio = (Cash & Equivalents + Accounts Receivable (A/R) / CurrentLiabilities

"""
def cashRatio(cash , CurrentLiabilities):
    """Cash Ratio = Cash / Current Liabilities.""" 
    return cash / CurrentLiabilities

def currentRatio(CurrentAssets , CurrentLiabilities):
    """ CurrentRatio = CurrentAssets / CurrentLiabilities"""
    return CurrentAssets / CurrentLiabilities

def quickRatio( cashEquivalents, aRecievable, currentLiabilities):
    """
    Quick Ratio = (Cash & Equivalents + Accounts Receivable (A/R) / CurrentLiabilities

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


"""
Lastly: estimate Doubtful Debt:
Source: https://www.indeed.com/career-advice/career-development/allowance-for-doubtful-accounts#:~:text=It%20estimates%20the%20allowance%20for,10%2C000%20x%200.05%20%3D%20500
-Stimates the allowance for doubtful accounts [HOW?]: by multiplying the accounts receivable by:
1--"appropriate percentage" for the aging period
2 -- then adds the sum of those (2) totals together.
 example: 2,000 x 0.10 = 200.
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

def isBalanced(totalAssets, totalLiabilities, totalEquity ): # +
    """
     Checks whether Accounts in the balanceSheet is balanced
     By checking whether totalAssets equals: `totalLiabilities` plut `totalEquities`
     Applies to the classical `Accounting Equation`
     As: Assets  = Liabilities + Equities
    """ 
    condition = totalAssets  == totalLiabilities + totalEquities
    return condition 

def getDifference(LHS, RHS): # - 
    """for networth 
        totalAssets + totalLiabilities == totalEquities """
    return abs(LHS) - abs(RHS)

def setRhsLhs(totalAssets, totalLiabilities, totalEquities ): #+ 
    """ sets the left & right, for the Cliassical Accounting Equation : A = L + E """
    LHS =  totalAssets
    RHS =  totalLiabilities + totalEquities

    return LHS, RHS

def getDifference2(totalAssets, totalLiabilities, totalEquities ): #+ = (-) == 0 
    """ Checks whether the sides (of a classical Accounting Equation are equal """
    #   LHS       =?=  LHS
    # totalAssets  ==  totalLiabilities + totalEquities
    LHS, RHS = setRhsLhs( totalAssets, totalLiabilities, totalEquities )#+
    figure = getDifference(LHS, RHS) #If accounts are balanced,  their total should be equal to 0
                                    #either Assets == Liabilities + Equities OR
                                    #Assets - Liabilities -Equities  == 0 OR Assets - (Liabilities +Equities) == 0
    return figure

# Note: setRhsLhs (getDifference) != getNetWorth as:

#Rules:
## Rule1: AccountingEquation: totalAssets   ==  totalLiabilities + totalEquities
## Rule2: Networth          : totalAssets - totalLiabilities  == totalEquities

# Networth
## getNetWorth(totalAssets, totalLiabilities)

#getRelationNetWorthAccouting():


#Note: from (1) we can arrive to formula (2) how: by subtracting both sides of (1) by totalLiabilities

def getRelationNetWorthAccounting(totalAssets, totalLiabilities,totaEquities ):
    """ gets relationship between `NetWorth` and `Accounting` Equation [How?]
    by Asking:
        What is the difference between equivalence relations of Accounting against NetWorth` ?

    # accounting: totalAssets == totalLiabilities + totalEquities  (1)
    # networth: totalAssets - totalLiabilities == totaEquities     (2) then:
    # accounting == networth as 
    # accounting - networth == 0
    # Only iff (tne Equivalence Relation Exists):
    # totalAssets == (totalLiabilities + totalEquities)  === (totalAssets - totalLiabilities) == totaEquities 
    or
    totalAssets - totalLiabilities == totalEquities === (totalAssets - totalLiabilities) == totalEquities
    #note2: it's enough to show (1) relation which equals to (from left equivalence Relation) :
    totalAssets - totalLiabilities == totalEquities === ... 
    OR
            totalAssets - totalLiabilities - totalEquities == 0 === 
    or      totalAssets - (totalLiabilities + totalEquities ) == 0
    
    """
    #subtract totalLiabilities 
    LHS = totalAssets - totalLiabilities - totalEquities # 0 
    RHS = totalAssets - (totalLiabilities + totalEquities ) #0 
    condition = LHS == RHS # 0
    
    if  condition == True:
        return True
    elif condition == False:
        return False
    else: raise ValueError(ErrorMsg)

def getNetWorth(totalAssets, totalLiabilities): #ok 

    """  calculates `NetWorth` (original):
         NetWorth = totalAssets - totalLiabilities  ( == totalEquities ) """
    LHS = totalAssets - totalLiabilities  # Rule: `Networth == totalEquities
    RHS = totalEquities
    return abs(LHS) - abs(RHS) # setRhsLhs(totalAssets, totalLiabilities, totalEquities)

# isNetworth(totalAssets, totalLiabilities, totalEquities)
def isNetworth(totalAssets, totalLiabilities, totalEquities): #New #checked
    """ checks if accounts (Assets, Liabilities, Equities) are balanced, through
    Evaluating the total of : (totalAssets - totalLiabilities) = + totalEquities
    OR (this Equation is equivalent to): (totalAssets - totalLiabilities) - totalEquities = 0
    """
    return (totalAssets - totalLiabilities) - totalEquities

def verifyNetWorth1(totalAssets, totalLiabilities, networth): #TODO: appply flip of `networth` parameter in implementation

    """ verifies `NetWorth, by comparing it with `totalAssets` and `totalLiabilities` """
    # networth = totalAssets -  totalLiabilities == totalEquities [both sides should be equal]
    condition = networth  == getNetWorth(totalAssets, totalLiabilities) # totalAssets -  totalLiabilities
    return condition 

def verifyNetWorth2(networth, totalEquities  ,ErrorMsg : str ="Exception Raised: Value Error, please check all inputs, then retry"):

    """ Verify `NetWorth`against `totalEquities`
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
    """ Apply the accounting Equation : A = L + E
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
        - By  calculating Owner's networth = Assets - Liabilities)

        - In subtrcating: RHS from LHS (accounting terminology: `LHS` Less `RHS` )
    """
    condition = RHS == LHS
    return condition

totalEquities = subTotalEquities2020
RHS =  totalAssets 
LHS =  totalLiabilities + totalEquities
print(" Right side =  totalAssets  = ",RHS)
print(" Left side =  =  totalLiabilities + totalEquities = ",LHS)
print("RHS ==  LHS = ",RHS ==  LHS)
RHS ==  LHS

equals = isBalanced(totalAssets, totalLiabilities, totalEquities)

print("Accounts equal = ", equals ) 

print(" Right side = ",RHS)
print(" Left side = ",LHS)


print("Difference LHS-RHS= ", LHS-RHS) # TODO: also do accounts balance (i.e. equal 0 )
print("Accounts Balnce : totalAssets + totalLiabilities  = totalEquity \n",
                "Right hand: Assets  = ",RHS, "\n" , "  ", "Left hand side =  Liabilities + Equity ", LHS,  ) 

print("try1: is isBalanced = ",isBalanced(totalAssets, totalLiabilities, totalEquities ))

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
cl2020 = [42296, 42684, 6643, 4996, 8773]
subtotal1 = iterateSubtotals(cl2020)
print(subtotal1)

#1.2 nonCurrent Liabilities 
ncl2020 = [98667, 54490]
subtotal2 = iterateSubtotals(ncl2020)
print(subtotal2)
#2. Total Liabilities
totalLiabilities = subtotal1 +subtotal2 
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
_flag_isequal = isBalanced(totalAssets, totalLiabilities, totalEquities) #isEqual()

## print("Accounts (in the accounting equation RHS = LHS : Assets+Liabilities = Equity",_flag_isequal)

# 2.2. getDifference2(totalAssets, totalLiabilities, totalEquity)
diff = getDifference2(totalAssets, totalLiabilities, totalEquities)
## print("difference = ", diff)

assets = 302083 #352755

liabilities  = 152452 # 302083
equity = 149631

_flag_accepted = isBalanced(assets, liabilities, equity ) # isEqual()
print("is equal = ", _flag_accepted)
_diff = getDifference2(assets, liabilities, equity) #( getDifference2(assets, liabilities, equity))
print("difference : ", _diff)



# As always, there is Stucture, just like in everything else

class balanceSheet:
    """
    Balance is time oriented, usually a  year ( in which we would stick to it ) 
    We can do a balance (at any given moment: month, quarter, year) so we can get a gist of what we have, and do not have
    - This we owe  to others,
    The things others owe to us

    Finally, balance is important, as from it,we can get to the 
    """

    #Helper functions:
    # iterateSubtotals
    def iterateSubtotals(self,subTotals,printFunction=None):

        _sum = 0
        for item in subTotals:
            _sum += item

        return _sum
    #def setTitle(self, title: str ):
    #    """ sets the title of a report instance """
    #    if not optionalDesc is None:
    #        self.description = optionalDesc

    #    self.title = title
    #    return title
        #pass
    
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
            
    
    # getTotalAssets# get totals #easy  #Impractical
    def getTotalAssets(self, _currentAssetsSubTotal, _nonCurrentAssetsSubTotal):

        """returns TotalAssets, from Subtotal of currentAssets, nonCurrentAssets """
        #1. Assign
        self.currentAssetsSubTotal = _currentAssetsSubTotal
        self.nonCurrentAssetsSubTotal = _nonCurrentAssetsSubTotal

        #2. Add 
        self.totalAssets = self.currentAssetsSubTotal + self.nonCurrentAssetsSubTotal

        #3. Return 
        return self.totalAssets

    def getTotalLiabilities(self, currentLiabilitiesSubTotal, nonCurrentLiabilitiesSubTotal):
        
        """returns Liabilities, from Subtotal of `currentLiabilities`, `nonCurrentLiabilities` """
        #1. Assign 
        self.currentLiabilitiesSubTotal = currentLiabilitiesSubTotal
        self.nonCurrentLiabilitiesSubTotal = nonCurrentLiabilitiesSubTotal

        #2. Add 
        self.totalLiabilities = self.currentLiabilitiesSubTotal +  self.nonCurrentLiabilitiesSubTotal

        #3. Return 
        return self.totalLiabilities

    def getTotalEquities(self, currentEquitySubTotal ) : #, nonCurrentEquitySubTotal):

        """returns Equities, from Subtotal of `currentEquities`, `nonCurrentEquities` """""" Assigns  currentEquitySubtotal """ 
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
        functions
        calcCurrentAssetsSubTotal(self,currentAssets)
        """
        #Better Approach:
        
        #CalcAssets
        ## calcCurrentAssetsSubTotal
         # calcNonCurrentAssetsSubTotal(self,_nonCurrentAssets)
         # calcAssets(self, _currentAssets, _nonCurrentAssets)
         # calcCurrentLiabilitiesSubTotal(self, _currentLiabilities)
         # calcNonCurrentLiabilitiesSubTotal(self, _nonCurrentLiabilities)
         # calcTotalLiabilities(self, _currentLiabilities, _nonCurrentLiabilities )
         
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

    def calcTotalAssets(self, _currentAssets, _nonCurrentAssets): #Debug #modify

        #1. call calcCurrentAssetsSubTotal
        #currentAssetsSubTotal
        self.calcCurrentAssetsSubTotal(_currentAssets)

        #2. call `calcNonCurrentAssetsSubTotal
        self.calcNonCurrentAssetsSubTotal(_nonCurrentAssets)

        #3. Add results to `self.totalAssets`
        self.totalAssets =  self.currentAssetsSubTotal + self.nonCurrentAssetsSubTotal   #self.currentAssets + self.nonCurrentAssets

        return self.totalAssets


    
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

        def getTotalLiabilities(self):
            """gets the total if found and has a valid value, otherwise, raises a
                `ValueError """
            if  self.totalLiabilities is None:
                raise ValueError("Inappropriate value for `totalLiabilities`")
        return self.totalLiabilities
    
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
        
    def calcTotalLiabilities2(self, _currentLiabilities,_nonCurrentLiabilities):

            self.calcTotalLiabilities(_currentLiabilities, _nonCurrentLiabilities)
            return self.totalLiabilities

    #def getTotalLiabilities(self): # Remark: weak function definition
    #    if  self.totalLiabilities is None:
    #        raise ValueError("Inappropriate value for `totalLiabilities`")
    #    return self.totalLiabilities

    #CalcLiabilities
    def calcTotalLiabilities(self, _currentLiabilities, _nonCurrentLiabilities):

        ## CalcCurrentLiabilities
        self.CurrentLiabilitiesSubTotal =  self.iterateSubtotals(_currentLiabilities)
        
        self.calcCurrentLiabilitiesSubTotal( _currentLiabilities)
        self.calcNonCurrentLiabilitiesSubTotal( _nonCurrentLiabilities)

        return self.totalLiabilities


    def calcTotalEquities(self,_currentEquities): #TODO: ERRONeous (Change) 
        
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
            3. Then returns it, as `currentEquitiesSubTotal`
            
        getcurrentEquities():
        getTotalEquities()
        getTotalEquities2(totalEquities)
        workingCapital()
        """
        
        return self.currentEquitiesSubTotal
    
    def getTotalEquities(self):

        if self.currentEquitiesSubtotal is None: #not self.currentEquitiesSubtotal is None:
            self.totalEquities = self.currentEquitiesSubTotal
            
        return self.totalEquities

    def getTotalEquities2(self, totalEquities):
        """responsible for overriding `totalEquities` """
        
        self.totalEquities = totalEquities
        return self.totalEquities 


    def workingCapital(self):
        """(source:https://www.causal.app/whats-the-difference/working-capital-vs-net-working-capital)

        - Advantages [3]:

        1. A Short-Term measure: of the overall `liquidity`
        (by meeting short-term obligations  i.e. current Liabilities, within a year)
        
        2. Ability to adjust the (workingCapital position, the amount of money used to facilitate the

        the business operations.
        The larger the final figure is, the more enticing `Equity` account becomes,
        which helps proprietor with moving (some) liquidity to other, riskier projects.
        (If proprprietor is a small-buisness, partnership, or sole proprietor)
        [calculated by: Current Assets, less Current Liabilities]

        3. It (might be possible) to extend `Debt-terms` from 30 to 60 days,
         so that proprietor would free-up cash required (for other upcoming purposes) 
        
         - Disadvantages [1]:
         
         1. Could give a false sense of Security:
         If there is a large capital, that means a lot of assets (or inventories) are stored
         (in a warehouse, instead of liquid cash).
         Thus, the proprietor is less likely to take advantage of opportunities,
         requiring "Quick cash investment"
         
        """

        self.workingCapital = self.currentAssetsSubTotal - self.currentLiabilitiesSubTotal

        return self.workingCapital

    # Net Worth
    ## calcNetWorth(self):
    #def calcNetWorth(self): # takes 0 parameters

        """
        - A Long-Term measure: of Proprietor's overall `liquidity`
        Note: the sucess of running this function tightly depends on whether  we have previously calculated the `subTotals` of both: Assets, liabilites
            (otherwise, it wouldn't function, as expected)
        - is also called : the `Net Working Capital`

        pros: advantages over working capital
        1. provides a big picture of proprietor's liquidity,
        taking into account both:

        1.1 short-term obligations
        1.2 long-term obligations

        2. it is a `forward-looking` measure:
        it includes all of `proprietor`'s assets (not only short-term ones)
        Infer: thus, it provides a more comprehensive picture of proprietor's value

        cons:
        1. It may give a `False Sense of Security`:
        
            Because proprietor's overall liquidity  can  drastically change, (i.e. `forex`/`ETF` /`stock-market`) from 1 timestamp, to another` 
        (hence, failing to reflect the `currentEquity` after recent events that caused that change ).


        """

        #get assets and liabilities , assign them to NetWorth

       # self.NetWorth = abs(self.totalAssets) - abs(self.totalLiabilities)  #self.totalAssets - self.totalLiabilities

       # return self.NetWorth
    
    def calcNetWorth2(self, _totalAssets, _totalLiabilities):
        """ calculates the Book value of `totalEquities: the expected value of `totalEquities` (by calculating `totalAssets` less `totalLiabilities` ) """
        self.totalAssets = _totalAssets
        self.totalLiabilities = _totalLiabilities
        self.NetWorth = self.totalAssets - totalLiabilities 

        return self.NetWorth
    
    def calcNetworth3(self, _currentAssets, _nonCurrentAssets, _currentLiabilities, _nonCurrentLiabilities):
        """ calculates the Book value of `totalEquities: the expected value of `totalEquities` (by calculating `totalAssets` less `totalLiabilities` )
            - an additional step includes calculating totalAssets (from `_currentAssets` plus `_nonCurrentAssets` 
            
        """
        # 1 calc totalAssets
        self.calcTotalAssets( _currentAssets, _nonCurrentAssets )

        #2. calc totalLiabilities
        self.calcTotalLiabilities(_currentLiabilities,_nonCurrentLiabilities) # this should also compile

        #3. calc NetWorth
        self.NetWorth =  self.totalAssets - self.totalLiabilities

        return self.NetWorth
    
    # Verify Net Worth
    def verifyNetworth(self):
        """ Verifies `NetWorth` is the same as `TotalEquities` """
        
        condition  = self.NetWorth == self.TotalEquities
        return condition
    
    def verifyNetworth2(self):
        """ checks if the difference is equal to zero (0) """
        condition = self.getDifference() == 0
        return condition
    
    def getTotalEquities(self,  _currentEquities):
        """ Retrieves `TotalEquities`  using `_currentEquity` """
        self.currentEquities = _currentEquities
        self.currentEquities = self.iterateSubtotals(_currentEquities)#calcCurrentEquitiesSubtotal(_currentEquities) 
        self.totalEquities = self.currentEquities

        return self.totalEquities

    def isBalanced(totalAssets, totalLiabilities, totalEquity ): # +
        """
         Checks whether Accounts in the balanceSheet is balanced
         By checking whether totalAssets equals: `totalLiabilities` plut `totalEquities`
         Applies to the classical `Accounting Equation`
         As: Assets  = Liabilities + Equities
        """ 
        condition = totalAssets  == totalLiabilities + totalEquities
        return condition 


    #helper function

    def setRhsLhs(self, totalAssets, totalLiabilities, totalEquities ): #+ 
        """ sets the left & right, for the Cliassical Accounting Equation : A = L + E """
        LHS =  totalAssets
        RHS =  totalLiabilities + totalEquities

        return LHS, RHS

    #Note: change getDifference2 into `calcDifference`
    def calcDifference(self): #, totalAssets, totalLiabilities, totalEquities ): #+ = (-) == 0 
        """ Checks whether the sides (of a classical Accounting Equation are equal """
        #   LHS       =?=  LHS
        # totalAssets  ==  totalLiabilities + totalEquities
        LHS, RHS = setRhsLhs(self.totalAssets, self.totalLiabilities, self.totalEquities )#+
        figure = getDifference(LHS, RHS) #If accounts are balanced,  their total should be equal to 0
                                    #either Assets == Liabilities + Equities OR
                                    #Assets - Liabilities -EOFErrorquities  == 0 OR Assets - (Liabilities +Equities) == 0
        return figure


    def getDifference(self,LHS, RHS): # - 
        """ gets  the difference, between what's written on the left, with whats on the Right Hand Side"""
        return abs(LHS) - abs(RHS)

    #def getDifference2(self): #+ = (-) == 0 
   #     """ Checks whether the sides (of a classical Accounting Equation are equal """
        #   LHS       =?=  LHS
        # totalAssets  ==  totalLiabilities + totalEquities
    #    LHS, RHS = setRhsLhs(self.totalAssets, self.totalLiabilities, self.totalEquities )#+
    #    figure = getDifference(LHS, RHS) #If accounts are balanced,  their total should be equal to 0
                                    #either Assets == Liabilities + Equities OR
                                    #Assets - Liabilities -Equities  == 0 OR Assets - (Liabilities +Equities) == 0
    #    return figure

    def calcTotalEquities(self,_currentEquities): #TODO: ERRONeous (Change) 
            
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

    #helper function
        
    def calcTotalEquities(self, _currentEquities): # checked parameter name
        """ Direct `totalEquities` calculates `totalEquities`
        by calculating entries in the  `_currentEquities` list """ 
        self.totalEquities = self.iterateSubtotals(_currentEquities) #calcCurrentEquitiesSubtotal(_currentEquities) 
        return self.totalEquities

    def getEquities2(self,_currentEquities):
        """Direct totalEquities` calculation """ 
        return   bSheet2.calcTotalEquities(_currentEquities) # bSheet2.currentEquities # bSheet2.calcTotalEquities()

    def getTotalEquities(self):
        """ Returns totalEquities (from current """
        if not self.currentEquities is None:
            self.totalEquities = self.CurrentEquities 
        return self.totalEquities

    
    def verifyNetWorth(self, _networth):
        """ Compares Networth with total Equities """
        condition = self.NetWorth == self.totalEquities
        return condition
    
        if  condition == True: #== #totalEquities:
            return True
        elif _networth != totalEquities:
            return False
        else: raise ValueError("Please Check Input then try again, later")

    def setTitle( self, proprietor , title="Consolidated Balance Sheets", optionalDesc=None):
        """ sets the title of this instance, passingin proprietor name,
        the desired title, plus other optional Description `optionalDesc` """
        
        if not optionalDesc is None:
            self.description = optionalDesc

        self.title = title
        return title

    def getEquitiesBookValue(self ):

        """Gets the book value of Equities [How?]
         - By calculating: totalAssets -
         - note: figure above should be equal to `totalEquities`
         when evaluated , at any time
         (or else, we have uncovered
         - Solution : further auditing is required
         
         - The  best case: difference is equalt to `0`, and all 3 major accounts
        (totalAssets, totalLiabilities, totalEquities)
        balances out """

        LHS = self.totalAssets - self.totalLiabilities 
        RHS = self.totalEquities

        self.diff = abs( LHS) - abs(RHS) #abs(LHS) - abs(RHS) # created variable
        return diff    

    def getAccountingEquation(self):
        """ Gets the classicals Accounting Equation: 
            totalAssets = totalLiabilities + totalEquities => where LHS =  totalAssets
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
_equals = isBalanced(totalAssets, totalLiabilities,  totalEquities)

#setTitle( "APPLE INC ",title="Consolidated Balance Sheets", optionalDesc=None)


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
totalAssets = bSheet.calcTotalAssets(ca2020,nca2020 )
print("totalAssets = ", totalAssets)

# 2.TotalLiabilities
#2. Calculate the Liabilities' `Total by `calcTotalLiabilities(currentLiabilities, nonCurrentLiabilities)
totalLiabilities = bSheet.calcTotalLiabilities(cl2020, ncl2020) # <--
print("totalLiabilities = ", totalLiabilities)

#3. TotalEquities
#3. Calculate the Equiries' `Total` by `calcTotalEquities(currentEquity)`
#error: takes 1 positional argument but 2 were given
Equities = bSheet.calcTotalEquities(equity2020) # calcTotalEquities(equity2020) 
print("Equities =", Equities) 
#end of Lvl 0

#lvl1: Analysis
#1. Working Capital

workingCapital = bSheet.workingCapital() # #no error (check why)

print("workingCapital = ", workingCapital)

#2. Net Worth

res = bSheet.calcNetWorth2(totalAssets, totalLiabilities)
print("calcNetWorth2( = ", res)
print("bSheet.NetWorth = ",bSheet.NetWorth)

#Is NetWorth

IsNetWorthVerified = bSheet.verifyNetWorth(bSheet.NetWorth) #bSheet.NetWorth) #should compile 
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
totalAssets = bSheet2.calcTotalAssets(ca2017,nca2017 )
print("totalAssets = ", totalAssets)
CL = bSheet2.iterateSubtotals(cl2017)
NCL = bSheet2.iterateSubtotals(ncl2017)
print("CL =",CL)
print("NCL =",NCL)
print("liabilities =",CL+NCL)
print("totalAssets - liabilities = ", totalAssets - (CL+NCL))
# 2.TotalLiabilities
print("cl2017 = ", cl2017)
print("bSheet2.iterateSubtotals(cl2017)", bSheet2.iterateSubtotals(cl2017) )

print(")   ")
print("ncl2017= ", ncl2017)
#2. Calculate the Liabilities' `Total: `calcTotalLiabilities(currentLiabilities, nonCurrentLiabilities)
totalLiabilities = bSheet2.calcTotalLiabilities(cl2017, ncl2017)
print("totalLiabilities = ", totalLiabilities)

#3. TotalEquities
#3. Calculate the Equities' `Total`: `calcTotalEquities(currentEquity)`

Equities = bSheet2.calcTotalEquities(equity2017) # calcTotalEquities(equity2020) 

print("Equities =", Equities) 
#End of [Lvl 0]

#[lvl1: Analysis]

#1. Working Capital
workingCapital = bSheet2.workingCapital() #compiles
print("workingCapital = ", workingCapital)

#2. Net Worth
#2.1 calcNetWorth(): #Note: pre-supposes both `totalAssets`, `totalLiabilites` been: calculated,& stored in  `balanceSheet` instance [if not, use the other function]
#2.2 calcNetWorth(totalAssets, totalLiabilities)
res = bSheet2.calcNetWorth2( totalLiabilities, totalAssets)
print("bSheet.NetWorth2 = ",res)

#3. verifyNetWorth()
IsNetWorthVerified = bSheet2.verifyNetWorth(bSheet2.NetWorth)
print("IsNetWorthVerified = ", IsNetWorthVerified)


#4. getDifference()
print("Difference(Assets - (liabilities+ Equities) = ",bSheet2.calcDifference()) # totalAssets,totalLiabilities) )
#5.
print("bool is the same (getDifference() ==0)? = ", bSheet2.calcDifference() == 0 )
# calcTotalEquities
print("1. bSheet2.calcCurrentEquitiesSubtotal(equity2017) = ",bSheet2.calcCurrentEquitiesSubtotal(equity2017)) # returns a list (of equities) 
print("2. bSheet2.currentEquities = ",bSheet2.currentEquities)
print("3. bSheet2.getEquities = ", bSheet2.getEquities2(equity2017))
print("4. bSheet2.getEquities = ", bSheet2.calcTotalEquities(equity2017))
networth2 = bSheet2.NetWorth  # 375319
print("networth2" , networth2)
print("bSheet2.NetWorth2 ", bSheet2.calcNetWorth2(totalAssets,totalLiabilities )) # 375319 # wrong [this is from the last value ]

#self.totalAssets = totalAssets
#self.totalLiabilities = totalLiabilities


def calcNetWorth2(totalAssets,totalLiabilities ):
    return getDifference(totalAssets - totalLiabilities)
    
def calcLiabilities(cl,ncl):
    _cl = iterateSubtotals(cl)
    _ncl= iterateSubtotals(ncl)
    return _cl + _ncl
    
totalLiabilities =  calcLiabilities(cl2017,ncl2017)
print("totalLiabilities",totalLiabilities)
networth2 = bSheet2.calcNetWorth2(totalAssets , totalLiabilities)
print("networth2", networth2)
print("totalAssets - totalLiabilities",totalAssets - totalLiabilities)


bSheet2_calcNetWorth2 = (   totalAssets- totalLiabilities)
print("bSheet2_calcNetWorth2 = ", bSheet2_calcNetWorth2)


bSheet2.calcNetWorth2 = bSheet2.calcNetWorth2(totalAssets,totalLiabilities )
#print("calcNetWorth2(totalAssets,totalLiabilities )) = ",bSheet2.calcNetWorth2(totalAssets,totalLiabilities )) #  134047
print("bSheet2.calcTotalEquities(equity2017) = ", bSheet2.calcTotalEquities(equity2017)) # 134047 # correct
print(" bSheet2.NetWorth == bSheet2.NetWorth(equity2017)",bSheet2.NetWorth == bSheet2.calcTotalEquities(equity2017)) # 375319 

print("difference of difference" , abs(bSheet2.getDifference( totalAssets, totalLiabilities)) -  bSheet2.calcTotalEquities(equity2017) == 0) #True 

#print("difference of difference" , abs(bSheet2.getDifference()) - bSheet2.verifyNetWorth() == bSheet2.calcTotalEquities() )  #bSheet2.NetWorth(NetWorth) == bSheet2.calcTotalEquities() )

#TODO:
#1. Rakes one Input argument: calcTotalEquities(_currentEquities)
#2. ensure function `getEquities` ,adding an attribute  `self.totalEquities`  (instead of the hassle of re-calculating `calcTotalEquities(_currentEquities)` )

#The End

## def getEquities(self):
##     return   self.calcTotalEquities()  # bSheet2.currentEquities # bSheet2.calcTotalEquities() #not currentEquities (list of Equities)

#Extra:
#class `printReport`
#Encapsulates function above (including their different `lvl`s : lvl0, lvl1

class printReport:
    def __init__(bSheet):
        pass # encapsulates the `printed values` above 

class StockholderEquity: 
    """ - The Capital 
        - Stock holder equity:

    1. Proprietor: is either a :  1. `personal` 2. `smallBusiness` 3. `company` (or so) #TODO:enum
    2. Calculated from:
    2.1. retainedEarnings : from the balance Brought Forward (at the start of a month, ususally termed balance 'b/d',
    at the start of each Period: let it be monthly, Quarterly, or yearly (i.e. Annum ).
    2.2. `capitalStock` [if proprietor is a `listed-company`:(in this casem we have to account for ) the current number of shares in the market
    2.3. Gains losses: calculated from: generating the Report: `Income Statement` (or the `Statement of Comprehensive Income`) Report's **Ending** figure, for a specific period (of time).
         # In the following Scenarios: whether `User` is: a person (or even a company, in the case of a `small-business`, single proprietorship, or partnership )
         # Whether they have incurred Gains (above break-even `0` ) or Incurred Losses (went below the Break-even point `0`)
         # Hence: the requirement for an `IncomeStatement` that boils down a year of Operations, including All -Immediate- Expenses Incurred, & `Gains` Realized, for specified period (month, Quarter, annum (year) ).
         
    """

    class CapitalStock:

        def __init__(self, capitalStock):
            self.capitalStock = capitalStock
                

    class CommonStock(CapitalStock):

        def __init__(self, commonStock):
            self.commonStock = commonStock 
                 

        def __init__(self,capitalStock, retainedEarnings,GainsLosses):
            """ constructor
            Passes-in:
            
            1. capital stock (from )
            2. retainedEarnings: earnings in a period, that stays in buisness for further circulation, to capture and maximize benefits
            
            - Note: [Tutor: Krassimir Petrov]: Account  might also  have `Dividends ( which a company must set ).
            - It's a `portion` from retained Earnings, given to `stockholders` #TODO
            - Dividends: in otherwords, is a `Contra-Account` [me:negative-Account] of the `retainedEarnings` Account:
            
            -- which we (ethically) let go off , for the sake of `stockholders` , the owners  of our `company`


            def calcStockHolderEquity(self):
                self.StockholderEquity =  self.capitalStock + self.retainedEarnings + self.GainsLosses
            """
            self.capitalStock = capitalStock
            self.retainedEarnings = retainedEarnings
            self.GainsLosses = GainsLosses
