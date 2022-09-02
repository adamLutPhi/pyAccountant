# accountingLog

## 9-1-2022


### Added 
A `resetAccount`:  to reset the state of account, after each Debit or Credit, 
as each state the account assumes. The flags `Cr` & `Dr` are only temporary
*( that,when appled correctly, works fluently in a transaction)* 


#### Elaboration: 
it's a two-way system: 
- the account could be debited:
    set account to debit
    
    account is called 
    then, reset:
    It **resets its self state**,  ideally before returning to user


`resetAccount`
Made callable, to enforce the reset of accounts' transaction flags : `drTransaction`, `crTransaction`

##### Perspective

`Transaction 1` always is a success 
However, I am afraid to say so , about  the others.

the `resetAccount` would set things straight, by  returning the **debit flag** `drTransaction` , **credit flag** `crTransaction`or returning the `None` State - **the Original state of Being** , where nothingness exists
 
Thus, on a higher level, we have: 
 
 1. **stateful**: 
 - an Action of flow is happening
 -  can describe an `Account` as `Debit` or `Credit`
- 2 types of flow can be summarized
 2. **stateless**:
 
 Required to be , as states need to return to their original default state `None`
 
 **Note:**
     for the account to free `free flowing`
     it must transition, between `statefulness` , then retreats back int `statelessness`
 
- A `state` has: 
    1. Debit 
    2. Credit 

    it describes an action, that occurs.
        
- A `Non-state` has:
    3. None
    describes the stillness.
    

 1. Debit : whenever one requires to `debit` the account 
 this depends on the accounts type : 
 
 After each state ,  the account should be able to return to `None` 
 *(Where no action happens )*
 

### Added 
 #1.1. flowHandling 
 Returns a user-friendly string about the cash flow : `in-flow`, `out-flow`, or `No change` (i.e. n.c)
 
 # 
 1.2. calcFlow: serves as a better alternative of a return, for any account
 (after all accounting is about being accountable on cash-flows)
 calculates the cash flow:

 1. if increasing: returns a positive amount 
 2. if decreasing: returns a negative amount 
 3. if it's equal to 0: retunrs `No Change` (i.e. n.c)
 
 **Updated**
 Instead of Dr or Cr ( flags with a great level of confusion)
 I have extended Account properties to include:
 
 #Transaction flags
 Describes the flags of a current `transaction` , in a `stateful` manner 
 (i.e. in relation to the accounts current state : 
 1. is it Debiting mode i.e. `drTransaction`
 2. is it Crediting mode i.e. `crTransaction`
 3. or is it stateless , where no action is required i.e. `None`
 
 this kind of seperation removes confusing part of the current state of an account 
 
### Changed 
 
 `drTransaction` instead of `Dr`
 `crTransaction` instead of `Cr`
 
 Hence, this makes it clear that it implements the flags *(as a  part of a changeable account states)*
 
 whereas , for the **Account flags**:
 
1.  `drAcc`
2. ` crAcc `

Note: it only requires to be called but account objects

Those describe what a paticular `account` is (i.e. a DebitAccount or a CreditAccount) # TODO: ensure this feature is implemented, as well 
 Hence, helps in promoting an `account` (into a `DebitAccount` or a `CreditAccount` )
 
 
 # Those 4 flags in total are needed in order to properly let all accounts 
 function **dynamically & organically**
 Once logic has been set , an update would be the best, by that time.
 
 ## 9-2-2022
 
 ### Added 
 
 Static methods for 
 
 1. `Increment` 
 2. `decrement` 
 
 ### Changed 
 Decrement, fixed return, so that it exatly ,after subtraction, the total of account balances 
 (goes back to 0, successfulling )
 
 Increment might be prone to arithmetic errors, but none discovered, on my part
