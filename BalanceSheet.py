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


import operator
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

def getGap(_total, _sub):

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
    return diff



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


class partialEntry:
    pass
"""
name: str price : double

1. Creating a new class creates a new type of object,
2. Allowing new instances of that type to be made.
3. Each class instance can have attributes attached to it for maintaining its state.
4. Class instances can also have methods (defined by its class) for modifying its state.


"""
    # stmt-1

    # stmt-2

    # stmt-3


# class object

class MyClass:
    """A simple example class

then MyClass.i and MyClass.f are valid attribute references,
returning an integer and a function object,
respectively. Class attributes can also be assigned to,
so you can change the value of MyClass.i by assignment. __doc__ is also a valid attribute,
returning the docstring belonging to the class: "A simple example class".

Class instantiation uses function notation.
Just pretend that the class object is a parameterless function
that returns a new instance of the class. For example (assuming the above class):
"""
    i = 12345

    def f(self):
        return 'hello world'

#create class object
x = MyClass()
"""
Creates a new instance of the class and assigns this object
to the local variable x.

The instantiation operation (“calling” a class object)
Creates an "empty object".
Many classes like to
"create objects"
with instances customized to a specific "initial state".
Therefore a class may define a special method named "__init__()",

like this:

"""

#def __init__(self):
##    self.data = []

"""
When a class defines an __init__() method,
class instantiation automatically invokes __init__()
for the newly created class instance. So in this example,
a new, initialized instance can be obtained by:
"""

"""
for greater flexibility :

__init__() method have arguments:
in that case: arguments given to the class instantiation operator
passed on to __init__()
"""

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)

print("x.r = ", x.r, " x.i = ", x.i)
# (3.0, -4.5)

# 9.3.3. Instance Objects

"""
Now what can we do with instance objects?
The only operations understood by instance objects are attribute
references. There are two kinds of valid attribute names:
data attributes and methods.

data attributes correspond to “instance variables” in `Smalltalk`,
and to “data members” in C++. Data attributes need not be declared;
like local variables, they spring into existence when they are first
assigned to. For example, if x is the instance of MyClass created above,
the following piece of code will print the value 16,
without leaving a trace:


"""
"""
x.counter = 1
while x.counter < 10:
    x.creater = x.counter * 2
    
print("count = ", x.counter)
del x.counter
"""

"""

Now what can we do with instance objects? The only operations understood by instance objects are attribute
references. There are two kinds of valid attribute names:
data attributes and methods.

data attributes correspond to “instance variables” in Smalltalk,
and to “data members” in C++. Data attributes need not be declared;
like local variables, they spring into existence when they are first assigned to.
For example, if x is the instance of MyClass created above,
the following piece of code will print the value 16,
without leaving a trace:

# 9.3.4. Method Objects
Usually, a method is called right after it is bound:

"""

# x.f()

"""
In the MyClass example, this will return the string 'hello world'.
However, it is not necessary to call a method right away: x.f is a method object,
and can be stored away and called at a later time. For example:

"""

#xf = x.f
#while True :
#    print(xf())

"""
will continue to print hello world until the end of time.

What exactly happens when a method is called? You may have noticed that x.f()
was called without an argument above, even though the function definition for f()
specified an argument. What happened to the argument? Surely Python raises an exception when a function
that requires an argument is called without any — even if the argument isn’t actually used…

Actually, you may have guessed the answer: the special thing about methods is that the instance object
is passed as the first argument of the function. In our example, the call x.f() is exactly equivalent to MyClass.

f(x). In general, calling a method with a list of n arguments is equivalent to calling the corresponding function
with an argument list that is created by inserting the method’s instance object before the first argument.

If you still don’t understand how methods work, a look at the implementation can perhaps clarify matters.

When a non-data attribute of an instance is referenced, the instance’s class is searched.

If the name denotes a valid class attribute that is a function object, a method object is created by packing
(pointers to) the instance object and the function object just found together in an abstract object:
this is the method object. When the method object is called with an argument list, a new argument list is constructed
from the instance object and the argument list, and the function object is called with this new argument list.

9.3.5. Class and Instance Variables
Generally speaking, instance variables are for data unique to each instance and class variables are
for attributes and methods shared by all instances of the class:


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

#print()

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

""" 
CashRatio = cash / CurrentLiabilities
CurrentRatio = CurrentAssets / CurrentLiabilities.
Quick Ratio = (Cash & Equivalents + A/R) / CurrentLiabilities

"""

"We want estimated Doubtful Debt, first:"

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
cL2020= [42296, 42684, 6643, 4996, 8773]

# Noncurrent Liabilities
nonCurrentLiabilities = ["Term debt", "Other non-current Liabilities"]
nCL2020 = [98667, 54490]

subTotalCurrentLiabilities2020 = iterateSubtotals(cL2020)

subTotalNonCurrentLiabilities2020 = iterateSubtotals(nCL2020)

totalLiabilities = subTotalCurrentLiabilities2020+ subTotalNonCurrentLiabilities2020

print("totalLiabilities = ", totalLiabilities )

 

#---
#Capital
## Commitments & Contingencies
## Shareholder's equity

shareholderEquity = ["Common Stock", "Retained Earnings", "Accumulated Other comprehensive income (loss)"]
#
shEquity2020 = [50779,14966, -406]

shEquity2019 = [45174, 45898, -584]

subTotalEquity2020 = iterateSubtotals(shEquity2020) # get equity 
print("subTotalEquity2020 = ", subTotalEquity2020)
totalEquity = subTotalEquity2020
# subEquity2019 = iterateSubtotals(shEquity2019)


#def __init__(self):
#        pass

#def __repr__(self):
    #pass
    

#def calc_grossMargin():

# Income Statement [#TODO: move to new  module]
        
def calcCogs(subTotals):

    cogs = iterateSubtotals(subTotals)
    return cogs

# Balnace sheet [static ] methods 

def isEqual(totalAssets, totalLiabilities, totalEquity ):
    """
 # applying basic accounting equation:
        Assets  = Liabilities + Equity

""" 
    RHS =     totalAssets 
    LHS = ( totalLiabilities  + totalEquity )
    if RHS == LHS: # good 
        
        return True
    
    if RHS != LHS:

        return False

    
def getDifference(LHS, RHS):

    return abs(LHS) - abs(RHS)


def getDifference2(totalAssets, totalLiabilities, totalEquity ):

    LHS = totalAssets
    RHS =  totalLiabilities + totalEquity

    diff = getDifference( LHS, RHS  )
    return diff

      
def getNetWorth(totalAssets, totalLiabilities):
    """  networth (original) """
    return totalAssets - totalLiabilities

def verifyNetWorth1(networth):

    pass

def verifyNetWorth2(networth, totalEquity):
    "NetWorth (in business) is also referred to as Equity "
    if networth == totalEquity:
        return True
    elif networth != totalEquity:
        return False
    else: raise ValueError("Please Check Input then try again, later")
    
def printIsEqual(totalAssets, totalLiabilities, totalEquity ):

    RHS =     ( totalAssets + totalLiabilities )
    LHS = totalEquity
    print("totalAssets = ",totalAssets)
    print("totalLiabilities = ",totalLiabilities)
    print("totalEquity = " , totalEquity)

    boolIsEqual = printIsEqual2()
    if RHS == LHS: # good 
        
        # accountant check if sides nbalances , but suntrating RHS from LHS :
        
        print(" Right side = ",RHS)
        print(" Left side = ",LHS)
        print("Difference = ", LHS-RHS) 
        print("Accounts Balnce : totalAssets + totalLiabilities  = totalEquity \n",
                RHS , "  ", LHS,  ) 
        #boolIsEqual =  True
    
    if RHS != LHS:
        print("Assets: ", totalAssets ,"\n")
        print("Liabilities: ", totalLiabilities  , "\n")
        print("Total: ", totalAssets  +totalLiabilities )
        print("Owner's Equity:", totalEquity, "\n")

        print("Accounts do Not Balance")
        print("Difference = ", LHS-RHS)
        #boolIsEqual =  False 

def printIsEqual2(LHS, RHS):
    
    if RHS == LHS: # good 
        
        # accountant check have another way  of checking if sides balances (one way is by calculating Owner's networth = Assets - Liabilities)
        #delete?: ins suntrating RHS from LHS :
        
            print(" Right side = ",RHS)
            print(" Left side = ",LHS)
            print("Difference = ", LHS-RHS) 
            print("Accounts Balnce : totalAssets + totalLiabilities  = totalEquity \n",
                RHS , "  ", LHS,  ) 
        #return True
    
    if RHS != LHS:
        print("Assets: ", totalAssets ,"\n")
        print("Liabilities: ", totalLiabilities  , "\n")
        print("Total: ", totalAssets  +totalLiabilities )
        print("Owner's Equity:", totalEquity, "\n")

        print("Accounts do Not Balance")
        #return False
    
        #    print("Difference = ", LHS-RHS)  

        #pass



RHS = totalAssets 
LHS =  totalLiabilities + subTotalEquity2020

print("RHS ==  LHS = ",RHS ==  LHS)
RHS ==  LHS

equals = isEqual(totalAssets, totalLiabilities, totalEquity)

print("Accounts equal = ", equals ) 

print(" Right side = ",RHS)
print(" Left side = ",LHS)

print()
print("Difference = ", LHS-RHS) # TODO: also do accounts balance (i.e. equal 0 )
print("Accounts Balnce : totalAssets + totalLiabilities  = totalEquity \n",
                "Right hand: Assets  = ",RHS, "\n" , "  ", "Left hand side =  Liabilities + Equity ", LHS,  ) 

print("try1: is equal = ",isEqual(totalAssets, totalLiabilities, totalEquity ))

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
_flag_isequal = isEqual(totalAssets, totalLiabilities, totalEquity) #isEqual()

## print("Accounts (in the accounting equation RHS = LHS : Assets+Liabilities = Equity",_flag_isequal)

# 2.2. getDifference2(totalAssets, totalLiabilities, totalEquity)
diff = getDifference2(totalAssets, totalLiabilities, totalEquity)
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
        self.totalAssets = 0
        #self.liabilities
        # which is defined by the Duo:
        
        self.currentLiabilities = []
        self.nonCurrentLiabilities = []

        self.currentLiabilitiesSubTotal = 0
        self.nonCurrentLiabilitiesSubTotal = 0

        #self.equity
        # which is defined by the Duo:
        
        self.currentEquity = []
        #self.nonCurrentEquity = []

        self.currentEquitySubTotal = 0
        #self.nonCurrentEquitySubTotal = 0

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

    def getTotalEquity(self, currentEquitySubTotal ) : #, nonCurrentEquitySubTotal):
            """ Assigns  currentEquitySubtotal """ 
            #1. Assign 
            self.currentEquitySubTotal = currentEquitySubTotal
            # self.nonCurrentEquitySubTotal = nonCurrentEquitySubTotal
            #2. Assign #Add 
            self.totalEquity = self.currentEquitySubTotal  # +  self.nonCurrentEquitySubTotal
            #3. Return 
            return self.totalEquity

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
            self.currentAssetsSubTotal = iterateSubtotals(self.currentAssets)
            #3. Return self.currentAssetsSubTotal
            return self.currentAssetsSubTotal

        ## calcNonCurrentAssetsSubTotal
    def calcNonCurrentAssetsSubTotal(self,_nonCurrentAssets):

            """ calculates  nonCurrentEquity Subtotal """
            #1. Assign `currentAssets`
            self.nonCurrentAssets = _nonCurrentAssets

            #2. Calculate `nonCurrentAssetsSubTotal`
            self.nonCurrentAssetsSubTotal = iterateSubtotals(self.nonCurrentAssets)

            #3. Return `nonCurrentAssetsSubTotal` figure
            return self.nonCurrentAssetsSubTotal

    def calcAssets(self, _currentAssets, _nonCurrentAssets): #Debug #modify

            #1. call calcCurrentAssetsSubTotal
            #currentAssetsSubTotal
            self.calcCurrentAssetsSubTotal(_currentAssets)
            #_currentAssets= self.calcCurrentAssetsSubTotal(_currentAssets)

            #2. call `calcNonCurrentAssetsSubTotal
            self.calcNonCurrentAssetsSubTotal(_nonCurrentAssets)
            # _nonCurrentAssets = self.calcNonCurrentAssetsSubTotal(_nonCurrentAssets)

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

            self.currentLiabilitiesSubTotal = iterateSubtotals(self.currentLiabilities)

            # 3. Return `currentLiabilitiesSubTotal` figure
            return self.currentLiabilitiesSubTotal

    def calcNonCurrentLiabilitiesSubTotal(self, _nonCurrentLiabilities):

            """ Calculates `currentLiabilities` Subtotal """
            # 1. Assign `currentLiabilities` list
            self.nonCurrentLiabilities = _nonCurrentLiabilities

            # 2. Assign `currentLiabilitiesSubTotal` figure
            self.nonCurrentLiabilitiesSubTotal = iterateSubtotals(self.nonCurrentLiabilities)

            # 3. Return `currentLiabilitiesSubTotal` figure
            return self.nonCurrentLiabilitiesSubTotal

    def calcTotalLiabilities(self, _currentLiabilities, _nonCurrentLiabilities ):  

            #1. call calcCurrentAssetsSubTotal
            self.calcCurrentLiabilitiesSubTotal(_currentLiabilities)

            #2. call `calcNonCurrentAssetsSubTotal`
            self.calcNonCurrentAssetsSubTotal(_nonCurrentLiabilities)

            #3. Add results to `self.totalAssets`
            self.totalLiabilities = self.currentLiabilitiesSubTotal + self.nonCurrentLiabilitiesSubTotal

            return self.totalLiabilities
        
    def calcLiabilities(self, _currentLiabilities,_nonCurrentLiabilities):

            #1. call calcCurrentAssetsSubTotal
            self.calcCurrentLiabilitiesSubTotal(_currentLiabilities)

            #2. call `calcNonCurrentAssetsSubTotal`
            self.calcNonCurrentAssetsSubTotal(_nonCurrentLiabilities)

            #3. Add results to `self.totalAssets`
            self.totalLiabilities = self.currentLiabilitiesSubTotal + self.nonCurrentLiabilitiesSubTotal

            return self.totalLiabilities
    
    def calcCurrentEquitiesSubtotal(self,_currentEquities):

        """Assigns `currentEquities` list, calculates the figure of `nonCurrentEquity` Subtotal """
        # 1. Assign
        self.currentEquities = _currentEquities    # iterateSubtotals(currentEquity) 

        #2. currentEquitiesSubTotal
        self.currentEquitiesSubTotal = iterateSubtotals(self.currentEquities)

        #3. Assign
        return self.currentEquitiesSubTotal

    def getcurrentEquities(self, _currentEquities):
        """ gets  list ofequiities
        self.TotalEquities =  _currentEquities #self.calcCurrentEquitySubtotal(_currentEquities)

        return self.TotalEquities    
        
        """
        
        self.currentEquitiesSubTotal =  iterateSubtotals(_currentEquities)

        return self.currentEquitiesSubTotal
    
    def getTotalEquities(self):
        self.totalEquities = self.getCurrentEquitiesSubtotal() # + self.getNonCurrentEquitySubtotal()
        return self.totalEquity

     # lvl1

    # Working Capital  
    def workingCapital(self):
        """
    1. A Short-Term measure: of overall liquidity (source:https://www.causal.app/whats-the-difference/working-capital-vs-net-working-capital)
    2.Working capital is the amount of money used to facilitate the operations of the business.
    calculated by:
     Current Assets less Current Liabilities.

     pros:
     allows to set short term -goals
     (by meeting short-term obligations (i.e. current Liabilities, within a year)

     pros : of being a strong woerking capital position
     "Strong Working Capital" position,
     it may be able to take advantage of a supplier's
     offer to extend terms from 30 days to 60 days.
     This would free up cash ( that could be
     used for other purposes.)

     cons:
     1. a strong capital may mean that lots of assets are stored
     in a form of inventories (in warehouses, instead of liquid cash)
     thus, it is less likeliky to take advantage of opportunities,
     requiring "quick cash investment"
     
    """

        self.workingCapital = self.currentAssetsSubTotal - self.currentLiabilitiesSubTotal

        return self.workingCapital

    # Net Worth


    def calcNetWorth(self): # takes 0 parameters

        """
        - Is a Long-Term measure: of Proprietor's overall `liquidity`
        Note: the sucess of running this function tightly depends on whether previously we have calculated the subTotals of : Assets, liabilites
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
        It may give a False sense of Security
        Because proprietor's overall liquidy can drastically change
        (Even if its net worth is strong)
        
        """

        #get assets and liabilities , assign them to NetWorth

        self.NetWorth = self.totalAssets - self.totalLiabilities  #self.totalAssets - self.totalLiabilities

        return self.NetWorth
    
    def calcNetWorth2(self, _totalAssets, _totalLiabilities):

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
    """
    def verifyNetWorth(self, _networth): #practical 

       +-*+ if _networth == self.totalEquities:
            return True
        elif  _networth != self.totalEquities:
            return False
        else: raise ValueError("Please Check Input then try again, later")

    # Verify Net Worth
    """
    """
    def verifyNetWorth(self, _networth, totalEquities):
        "NetWorth (in business) is also referred to as Equity "

        if _networth == totalEquities:
            return True
        elif _networth != totalEquities:
            return False
        else: raise ValueError("Please Check Input then try again, later")
    """
    def calcEquities(self, _currentEquities): # checked parameter name

        #get CurrentEquities
        self.totalEquities = self.calcCurrentEquitiesSubtotal(_currentEquities) 
        return self.totalEquities
        
    def verifyNetWorth(self,_networth):
        if _networth == totalEquities:
            return True
        elif _networth != totalEquities:
            return False
        else: raise ValueError("Please Check Input then try again, later")

    def setTitle( self, title="Consolidated Balance Sheets", optionalDesc=None):

        if not optionalDesc is None:
            self.description = optionalDesc

        self.title = title
        return title
        
# DEMO

# Example : applying balance sheet of APPL
# source: https://www.investopedia.com/terms/b/balancesheet.asp
# For the year 2020

totalAssets = 323888
totalLiabilities = 258549
totalEquities = 65339 # totalEquity 
_equals = isEqual(totalAssets, totalLiabilities,  totalEquities)
print("Equals = ", _equals )

#LHS , RHS
print( "difference = ", getDifference(323888, 258549 + 65339) )
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
cL2020 = [42296, 42684, 6643, 4996, 8773] #current-liabilitiy list 2020)
## non-Current Assets
ncL2020 = [98667, 54490]    # non-current liability list (2020)

## Equity 2020
equity2020 = [50779, 14966, -406] #current-Equity list (2020)

# 
#SubTotals:
#1. currentAssets
currentAssetsSubTotal = bSheet.calcCurrentAssetsSubTotal(ca2020)
print("currentAssetsSubTotal = ", currentAssetsSubTotal)

#2. nonCurrentAssets' Subtotal
nonCurrentAssetsSubTotal = bSheet.calcNonCurrentAssetsSubTotal(nca2020)
print("nonCurrentAssetsSubTotal = ", nonCurrentAssetsSubTotal)

#3. currentLiabilities' Subtotal
print("bSheet.calcCurrentLiabilitiesSubTotal( cL2020) = ", bSheet.calcCurrentLiabilitiesSubTotal( cL2020) )

#non-current Liabilities' Subtotal
print("bSheet.calcNonCurrentLiabilitiesSubTotal(ncL2020)  = ",bSheet.calcNonCurrentLiabilitiesSubTotal(ncL2020))

#currentEquity Subtotal
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
Equities = bSheet.calcEquities(equity2020) # calcEquities(equity2020) 
print("Equities =", Equities) 
#end of Lvl 0

#lvl1: Analysis
#1. Working Capital

workingCapital = bSheet.workingCapital() # #no error (check why)

print("workingCapital = ", workingCapital)
#2. Net Worth

#NetWorth = bSheet.calcNetWorth2( ca2020, nca2020) #bSheet.getNetWorth()

bSheet.calcNetWorth2(totalAssets, totalLiabilities)
print("bSheet.NetWorth = ",bSheet.NetWorth)

#Is NetWorth

IsNetWorthVerified = bSheet.verifyNetWorth( _networth) #should compile 
print("IsNetWorthVerified = ", IsNetWorthVerified)
# IsNetWorth = bSheet.verifyNetWorth(_networth, totalEquities) # bSheet.verifyNetWorth()


# DEMO2:
#Source: https://www.investopedia.com/ask/answers/09/does-balance-sheet-always-balance.asp
ca2017names = ["Cash & Cash equivalents", "Short-term marketable Securities",
          "Accounts recievable, less alloances of 58 and 53 respectively",
          "Inventories", "vendor non-trade Recievables", "Other Current Assets"]
ca2017 = [20289, 53892, 17874, 4855, 17799, 13936]
nca2017names = ["Long-term Marketable Securities","Property, Plant , Equipment,net", "Goodwill",
                "Acquiried Intangible Assets, net", "other Non-Current Assets"]
nca2017 = [193714, 33783, 5717, 2296, 10162]

cl2017names=["Accounts payable","Accrued Expenses", "Deferred Revenue", "Commercial Paper", "Current portion of long-term Debt"]
cl2017 = [49049, 25744, 7548, 11977, 6496]

ncl2017names = ["Deferred revenue, non-current", "Long-term Debt",
                "Other, Non-Current Liabilities"]
ncl2017 = [2836, 97207, 40415]

## Equity 2017
equity2017 = [35867, 98330, -150] #current-Equity list (2020)

bSheet2 = balanceSheet(2017,proprietor="APPLE INC APPL")
bSheet2.setTitle("Consolidated Balance Sheets","(in millions, except number of shareswhich are reflected in thousands and per value")

#SubTotals:
#1. currentAssets
currentAssetsSubTotal = bSheet2.calcCurrentAssetsSubTotal(ca2017)
print("currentAssetsSubTotal = ", currentAssetsSubTotal)

#2. nonCurrentAssets' Subtotal
nonCurrentAssetsSubTotal = bSheet2.calcNonCurrentAssetsSubTotal(nca2017)
print("nonCurrentAssetsSubTotal = ", nonCurrentAssetsSubTotal)

#3. currentLiabilities' Subtotal
print("bSheet.calcCurrentLiabilitiesSubTotal( cL2020) = ", bSheet.calcCurrentLiabilitiesSubTotal( cl2017) )

#non-current Liabilities' Subtotal
print("bSheet.calcNonCurrentLiabilitiesSubTotal(ncL2020)  = ",bSheet.calcNonCurrentLiabilitiesSubTotal(ncl2017))

#currentEquity Subtotal
#User can also view CurrentAsset Subtotal
print("bSheet.currentAssetsSubTotal = ", bSheet.currentAssetsSubTotal )


#Totals
# A user can: 
# 1.TotalAssets
#1. Calculate the Assets' `Total` by calcAssets(currentAssets, nonCurrentAssets)
totalAssets = bSheet.calcAssets(ca2017,nca2017 )
print("totalAssets = ", totalAssets)

# 2.TotalLiabilities
#2. Calculate the Liabilities' `Total by `calcTotalLiabilities(currentLiabilities, nonCurrentLiabilities)
totalLiabilities = bSheet.calcTotalLiabilities(cl2017, ncl2017)
print("totalLiabilities = ", totalLiabilities)

#3. TotalEquities
#3. Calculate the Equiries' `Total` by `calcEquities(currentEquity)`
Equities = bSheet.calcEquities(equity2017) # calcEquities(equity2020) 
print("Equities =", Equities) 
#end of Lvl 0

#lvl1: Analysis
#1. Working Capital

workingCapital = bSheet2.workingCapital() # #no error (check why)

print("workingCapital = ", workingCapital)
#2. Net Worth

#NetWorth = bSheet.calcNetWorth2( ca2020, nca2020) #bSheet.getNetWorth()

bSheet.calcNetWorth2(totalAssets, totalLiabilities)
print("bSheet.NetWorth = ",bSheet.NetWorth)

#Is NetWorth

IsNetWorthVerified = bSheet.verifyNetWorth( _networth) #should compile 
print("IsNetWorthVerified = ", IsNetWorthVerified)
# IsNetWorth = bSheet.verifyNetWorth(_networth, totalEquities) # bSheet.verifyNetWorth()



#the end

class printReport:
    def __init__(bSheet):
        pass # encapsulated the `printed values` above 
class StockholderEquity:
    """ stock holder equity: is calculated iff:

    1. proprietor: is a `company`, small business (or so)
    2. calculated from :
    2.1. retainedEarnings : from the balances brought forward, at the start of each month (for the monthly) , Quarter (for the Quarterly) , year (for the Annual) Balance Sheet
    2.2. capitalStock: current number of shares in the market
    2.3. gains losses: calculated from the `Income Statement` or the `Statement of Comprehensive Income` Report's last figure , whether a company (or even a person, in the case of a small-business: single proprietorship, or partnership )
    Whether they have incurred Gains (above break-even) or Incurred Losses (went below the Break-even point)

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
            self.capitalStock = capitalStock
            self.retainedEarnings = retainedEarnings
            self.GainsLosses = GainsLosses
            # pass

        def calcStockHolderEquity(self):
            self.StockholderEquity =  self.capitalStock + self.retainedEarnings + self.GainsLosses
            
