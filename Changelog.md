# accountingLog

## 9-1-2022


added `resetAccount` to reset the state of account, after each Debit or Credit 
as each state the account assumes, is only temporary 

how: 
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
 
 
 
