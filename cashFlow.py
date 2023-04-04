from enum import Enum



    
class CashFlow:

    
    def __init__(self):
        pass


    def __init__(self, year=2022):
        pass
        
    #def add():
    #    pass

#TODO: partial Entry : depends upon it
def iterateSubtotals(subTotals, printFunction=None):
        _sum = 0
        for item in subTotals:
            
            _sum += item
        
        return _sum

operatingActivitiesNames = ["Earnings", "Depreciation", "Accounts receivable",
                            "Inventory", "Current Assets ", "Accounts Payable"]
operatingActivities = [248, 239, -108, 244, -18, -107]


investingActivitiesName = ["property, plant, Equipment PPE", "other long-term assets"]
investingActivities = [-205, 20]

financingActivities = [-50, 1, -121, 34, -16]


operatingSubtotal = iterateSubtotals(operatingActivities)

investingSubtotal = iterateSubtotals(investingActivities)

financingSubtotal = iterateSubtotals(financingActivities)


print("operatingSubtotal = ",operatingSubtotal)
print("investingSubtotal = ",investingSubtotal)
print("financingSubtotal = ", financingSubtotal)

total = operatingSubtotal + investingSubtotal + financingSubtotal

print("total  = ",total)
