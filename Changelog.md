# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 07:01:04 2022

@author: Ahmad Lutfi
"""

# accountingLog

9-1-2022


#added 
A `resetAccount`:  to reset the state of account, after each Debit or Credit, 
as each state the account assumes. The flags `Cr` & `Dr` are only temporary
*( that,when appled correctly, works fluently in a transaction)* 

 
 

# How: 
it's a two-way system: 
- the account could be debited:
    set account to debit
    
    account is called 
    then, reset:
    It **resets its self state**,  ideally before returning to user


`resetAccount`


Transaction 1 always is a success 
however,  I am afraid to say so , about  the others.

reset would set things straight, by  returning the debit or credit into the None State - original state of being 
 
 Thus, on a higher level, we have: 
 
 1. stateful: 
 - an Action of flow is happening
 -  can describe an `Account` as `Debit` or `Credit`
- 2 types of flow can be summarized
 2. stateless:
 
 Required to be , as states need to return to their original default state `None`
 
 **Note:**
     for the account to free `free flowing`
     it must transition, between `statefulness` , then retreats back int `statelessness`
 
a state has: 
    1. Debit 
    2. Credit 

    it describes an action, that occurs.
        
a non-state:
    3. None
    describes the stillness.
    

 1. Debit : whenever one requires to `debit` the account 
 this depends on the accounts type : 
 
 after each state ,  the account should be able to return to `None` 
 where no action happens 
 
 #--------
 ## Added 
 #1.1. flowHandling 
 retu rns a strong about 
 
 # 
 1.2. calcFlow
 
 Updated 
 instead of Dr or Cr ( flags with a great level of confusion)
 I have extended Account properties to include:
 
 #Transaction flags
 #descrives the flags of a current transaction , in a `stateful` manner 
 
 # Changed 
 
 `drTransaction` instead of `Dr`
 `crTransaction` instead of `Cr`
 
 Hence, this makes it clear that it implements the flags *(as a  part of a changeable account states)*
 
 whereas , for the **Account flags**:
 
1.  `drAcc`
2. ` crAcc `

 Those describe what a paticular `account` is (i.e. a DebitAccount or a CreditAccount) # TODO: ensure this feature is implemented, as well 
 Hence, helps in promoting an `account` (into a `DebitAccount` or a `CreditAccount` )
 
 
 # Those 4 flags in total are needed in order to properly let all accounts 
 function **dynamically & organically**
 Once logic has been set , an update would be the best, by that time.
 
 #--------
 # 9-2-2022
 
 # Added 
 
 Static methods for 
 
 1. `Increment` 
 2. `decrement` 
 
 # Changed 
 Decrement, fixed return, so that it exatly ,after subtraction, the total of account balances 
 (goes back to 0, successfulling )
 
 Increment might be prone to arithmetic errors, but none discovered, on my part