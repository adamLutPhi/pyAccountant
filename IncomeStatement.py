import inspect

"""
Notes:

1. Redundancy List:
1.1 iterateItems(: list) - > float

"""
conditionNegative  = lambda x:  True if x < 0 else  False
# conditionNegative(-1)

def getPercentage( _total, _sub):
    """ gets the percentage of sun (in relation to the sub (the expenses) """
    total = 100 
    

    x = _sub * 100/ total

    _add = 1- _sub
    p = _add * 100 / _total
    return x, p

def iterateSubtotals(subTotals,printFunction=None):

    #conditionNegative  = lambda x:  True if x < 0 else  False
    #condition = lambda x:  if x<0  else
    _sum = 0
    condition = False
    for item in subTotals:
        if conditionNegative(item) :
            _sum -= item
        elif not conditionNegative(item):
            _sum += item
    return _sum

#def getPercentage():
#    pass

# Example (Vanilla):
# Income statement: Income vs Expenses

# the same function works (for positive & negative values )
# (for both Debits , & Credits: each under their own context  )

""" Differentiate between: the good: Income """

# incoming cashflow
# Vanillia Example:

# Income
names = ['wages & Tips', 'Income Interest ', 'Dividends', 'gifts recieved']
prices = [5300.0   , 100.54 , 142.63 , 132.43 ]

_total = iterateSubtotals(prices)

print("totalItems = ", _total)

#outgoing cashflow

# Expense
names = ['water', 'Electricity', 'carrier, monthly [pre-paid]', 'Fuel ']
prices2 = [- 85, -  250, - 49.99, - 1624.59]
print("prices2 = ", prices2)

#prices3 = prices.extend(prices2)
prices3 = prices + prices2  #itertools.chain(prices, prices2)

print("total Income/Loss = ", prices3)


total = iterateSubtotals(prices3)# priceTotal  -> 100

_sub = iterateSubtotals(prices2)# sub Total -> x

total2 = total + _sub 
x = _sub * 100 /total2

print("total = ", total2) # 4447.76
print("- Total(_sub)  = ",_sub) # 2009.58 #note: _sub` is almost half (of `total2` ) 
print("percent Sub  = x= ", x, " %")

p, x  = getPercentage(total, _sub)


print("percentSub = ", x)


# Add function that prints
# shared
def getDifference(LHS, RHS): # - 
    """for networth 
        totalAssets + totalLiabilities == totalEquities """
    return abs(LHS) - abs(RHS)

class IncomeStatement:
    """
    getProbability(  p_sub, p_total)
    getPercentage( p_sub, p_total)
    getRemainder(self, _total, _sub):
    """
    
    def getProbability(  p_sub, p_total):

        """get a probability, """
        x = p_sub / p_total 
        
        p = 1 - ( p_sub / p_total )
        
        return  x, p
        
    def getPercentage( p_sub, p_total):
        """assumes p_sub is a the probability of event(sub)
gets the percentage of sun (in relation to the sub (the expenses)

- assumes p_total is probability of event(total)
gets the percentage of sun (in relation to the sub (the expenses) "


"""

        # totalPercent = 1#00 
        x, p = getProbability(p_sub, p_total)

        x = x * 100 #p_sub / p_total # * 100
        
        p = p * 100 #1 - ( p_sub / p_total ) # * 100
        
        return  x, p
    
    def __init__(self):
        pass


    def getRemainder(self, _total, _sub):
        return _total - _sub
    
    def getPercentage( _totalCount, _subCount):
        """assumes _sub is 
gets the percentage of sun (in relation to the sub (the expenses) """
        totalPercent = 100 
        x = _subCount

        x = _sub * 100/ _total
        
        p = 1 - ( _sub * 100 / _total )
        
        return  x, p 
    
    def __init__(self):
        pass


   # def getRemainder(self,  _sub, _total): # same as getDifference(LHSS, RHS)
   #     return _total - _sub


    def printValue(self, val):
        #todo: variable name 
        print(f" {val}  = ", percentSub)


    def getpDiff(self, percentAdd, percentSub):
    
        # calculate the gap : diff  = %Add - %Sub
        diff = percentAdd - percentSub
        print("diff = +", diff, " %")
        return diff

    def getProbability(self):
        pass
    
    def getPercentGap(self, _total, _sub):
    
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



    def getGap2(self, percentAdd , percentSub ):
        """gets the gap between the Add and sub percentage """
        # 1. Diff: %Add - %Sub
        
        diff= percentAdd - percentSub
        return diff


    def getCollection():#self):
        return inspect.currentframe().f_back.f_locals.items()

# getvariableName(var) 

    def getvariableName( var, itemPrice,collectionKernel= getCollection()):
        """ gets the name of a variable
        - we need three variables: #var_name, var_val, callers_local_vars
        - with a condition: `var_val is var`

        sourrce: https://docs.python.org/3/library/inspect.html

        """
        condition  = itemPrice is var
        #use of `inpect function: currentframe(), `f_back.f_locals.items()`
        
        collection = [] # inspect.currentframe().f_back.f_locals.items()

        return [itemName for itemName, itemPrice in  collection if condition ]

#DEMO
incomeStmt = IncomeStatement()

#1. fill-in data (with input


#2.1vl0: Do Further computation

# remainder = _total - _sub
remainder = incomeStmt.getRemainder( _sub, _total)


print(' Total Net Income: \t  \t  {0} \n '.format(remainder))


percentAdd, percentSub = getPercentage( _sub, _total)
print("percentSub= ", percentSub, " %")


percentTotal = 100
percentAdd = percentTotal - percentSub
print("percentAdd= ", percentAdd, " %")

# calculate the gap 
diff = percentAdd - percentSub


#finally calculate the gap 
diff = getDifference(percentAdd, percentSub) # percentAdd - percentSub


print("diff = +", diff, " %") # 9%


_sum = 0
#zip names, prices
for n, p in zip( names , prices ):
    
    #display name & price
    print('Income \t Budget \n {0} | {1}'.format(n, p))
    #calculate the `subTotal`
    _sum += p
    print(' Subtotal: \t  \t  {0} \n '.format(_sum))

#calculate the `Total`
_total = _sum
print(' Total: \t  \t  {0} \n '.format(_total))

#Example: Income Statement:
##A person has the following bills, in a specific month

# A la Real-world example:

names = ['income','Mortgage/Rent', 'Home/Rental Insurance ', 'Electricity', 'Gas/Oil', 'Water/Sewer/Trash', 'Phone/Cellphone', 'Streaming/Cable', 'Stationary', 'cloudService', 'other']
prices = [4000 ,- 200.0 , - 100.00 , -50.0 ,-  40.0, - 20.0, - 20.0, - 25.0, -125.0, -249.99 , 0.0]

_subtotal = 0

# def x( names , prices  , total=1000):

#function 1: Display name & Price

#say , this is balance b/d (brought down) 
#_total = 1000

def isGainOrLoss(total):

    condition = conditionNegative(total)
    if condition:
        return "Loss"
    if not condition:
        return "Gain"

def PositiveOrNegative(total):
    condition = conditionNegative(total)
    if condition:
        return "-"
    if not condition:
        return "+"
    else: raise ValueError("Unexpected Error Occured please recheck value and try again later")

def printWPrecision(total,precisionDigits: int =2):
    """ credit: Rex Logan, source:https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points """
    stringDigit=repr(precisionDigits)
    return("{:.2f}".format( round(total, precisionDigits)))

def check_probability(x):
    """ a probability, to be valid ,should be above 0 and below 1"""

    condition = 0 <= x <= 1
    if not condition :
        return False
    elif  condition :
        return True
    else:
        raise ValeError


_subtotal=3170.01
"""#UncommentMe In the end
for itemName , itemPrice in zip( names , prices ):
    
    print('Income \t Budget \n {0} | {1}'.format(itemName, printWPrecision(itemPrice))) 
    _subtotal += itemPrice
    print(' Subtotal: \t  \t  {0} \n '.format(printWPrecision(_subtotal)))
"""
total = _subtotal
strRes = isGainOrLoss(total)
print("Net Monthly Income ", strRes, "of $ {0}{1}".format(PositiveOrNegative(total),total) )

# Example 2
#3 for 5
cocaCola= 2.49 #4.99
pepsi = 2.51
drinks = [cocaCola, pepsi]

expectedExpense = 7.5

# subTotal: is an event of 2 cokes + 1 pepsi
subTotal = 2* cocaCola + 1* pepsi # approx 7.5
print("subTotal =", subTotal) # actual 7.49
actualExpense = subTotal

diff =  expectedExpense - actualExpense
print("difference(expectation - reality) = ", round(float(diff),2) ) 

# probability (of Counts)

p_coke = cocaCola / subTotal

p_pepsi = pepsi / subTotal
check_probability(p_pepsi)
# check_probability(p_pepsi)
print(f"Is ProbabilityValid(Event(Pepsi)){check_probability(p_pepsi) }") 
print(f"Is ProbabilityValid(Event(2 Cokes)){check_probability(2*p_coke) } ") # =  {check_probability(2*p_coke)} ") 

#print( check_probability(2*p_coke) ) 

print("p(pepsi) = ", p_pepsi)

print("p(P_coke)= ",2*p_coke)
print( 2*p_coke +p_pepsi == 1 )

val = p_pepsi + 2*p_coke
print(f"total probaility { p_pepsi + 2*p_coke}")
#condition = # sum#(enumerate(val)) == 1
#if not condition:
#     False
#elif condition:
#    True
#else:
#    raise ValueError("please recheck input, then try again later!")
    



