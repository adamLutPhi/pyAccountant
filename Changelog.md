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
 
 Required to be , as states need to return to their Original, & default state: `None`
 
 **Note:**
     for the account to free `free flowing`
     it must transition, between `statefulness` , then retreats back int `statelessness`
 
- A `state` has: 
    1. Debit 
    2. Credit 

    it describes an **action**, that occurs.
        
- A `Non-state` has:
    3. None
    
  describes the stillness, the non-action part *(of any action)*   

 1. Debit : whenever one requires to `debit` the account 
 this depends on the accounts type: 
 
 After each state ,  the account should be able to return to `None` 
 *(Where no action happens )*
 

### Added 

#### 1.1. flowHandling 
 Returns a user-friendly string about the cash flow : `in-flow`, `out-flow`, or `No change` (i.e. n.c)
 
  
#### 1.2. calcFlow 
-  serves as a better alternative of  return, 
- for any account(after all accounting is about being accountable on cash-flows)
- **How:** calculates the cash flow:

 1. if **increasing:** returns a *positive amount* 
 2. if **decreasing:** returns a *negative amount*
 3. if it's **equal to 0:** retunrs `No Change` (or *n.c*)
 
### Updated
 Instead of Dr or Cr ( the **bool flags** presents a great level of **Confusion**)
 I have extended Account properties to include:
 
#### Transaction flags
    1. `crTransaction`
    2. `drTransaction`
    
 they are flags Describing  of a current `transaction`, 
 in a `stateful` manner (i.e. in relation to the accounts current state: 
 1. is it **Debiting mode** i.e. `drTransaction`
 2. is it **Crediting mode** i.e. `crTransaction`
 3. or is it **stateless** , where no action is required i.e. `None`
 **[add Image here](http:www.pictureUrl.com)**
 
 this kind of *seperation* removes the confusing part of the current *state of an account*
 
 
### Changed 
 
 `drTransaction` instead of `Dr`
 `crTransaction` instead of `Cr`
 
 Hence, this makes it clear that it implements the flags *(as a  part of a changeable account states)*
 
 whereas , for the **Account flags**:
 
1.  `drAcc`
2. ` crAcc `

Note: the above is only **complementary** (but, by no means, **not necessary**)
Note: it only requires to be called but account objects

Those describe what a paticular `account` is (i.e. a DebitAccount or a CreditAccount) # TODO: ensure this feature is implemented, as well 
Hence, helps in promoting an `account` (into a `DebitAccount` or a `CreditAccount` )
 
 
 # Those 4 flags in total are needed in order to properly let all accounts 
 function **dynamically & organically**
 Once logic has been set , an update would be the best, by that time.
 
 
# 9-2-2022
 
## Added 
 
 Static methods for 
 
 1. `Increment`  an account, by an **amount**
 2. `decrement` an account, by an **amount**
 
## Updated
 
 `decrement`:  fixed its **return**, so that it's *precise* ,after subtraction, 
 Upon checking, the total of account balances **goes back to 0, successfully, as expected
 
 
 Increment might be prone to arithmetic errors, but none discovered, on my part
 
## Changed 

- `CreditAccount`: its `__init__`'s  parameters: so that it takes `name` & `total`
 instead of `args` & `kwargs` which it was taking 
 that is a copy/paste error, defined )

- `creditAcc.decrement` 
 
 Observing `CreditAccount`, it has not overrided it's `super`'s `account.decrement`
 this shows that account's `decrement` is the sole decrementation function, 
 that is properly functioning
 
 
## Updated
 
Added a `cash.total` assignment, so that it would **Auto-Update** the `Account.total`, 
in general , in the following manner:  
   
   
     cash.total = decrement(cash.total, 100) 
     bank.total = decrement(bank.total, 100)
     
     
As the static `decrement` returns the new `cash.total`, the assignment helps in
Updating cash's (& bank's) total

Updating the `account.total` was the missing link 
from now on, it should be reflected upon transactions


A gain, I am being reminded about the `flows of energy`: 
By a `Cash flow`, **it is the Bread & Butter of Accounting **
 

## 9-3-2022



### Added 
- **badDebt** 
whenever a debt is **spoiled**, and the one responsible is unable to pay back 
the sum amount, either partially, or in full.

### Updated  

- updating the general 5 required transactions, of the Great Expectations, 
in their **bare-bone form** suitable for beginners, as the code author.
it boils down to **5 main transactions **
 Mr.Pip's Debt  payment, in full, 
 Mr. Herbert's debt, going bad, while `barnettInn` records is as a `lossAccount` 
 (which is a  Credit Account), under the SOCI Account-Recording object 
 (describing the **Income & loss** Account )
 
- However, Mr. `pip` is able to pay back the `100` shillings for his dear friend 
in full, to `barnettInn` . the later would then record is written down as an **Income** 

Hence, at the end of an accounting period **( a month, season, year)**
the company, **Barnett Inn's** or simply put, `barnettInn`
would be able to track every **loss incurred**  & **income gained**, in their day-to-day
operations , as expected 



#### additional words 
 
 One would act their part of persona, which one wishes to become 
 
 Thus we act as if we have already reached the end of spectrum, 
 `e.g.` if we're at point `A`, but we want to reach point `B`
 Thus, we should act as we're already arrived at that point `B`, and act accordingly 
 Say, what changes would the programmer write, given knowledge learned, & skill earned.
 
 Maybe that' How code would resolve itself, author asks ( I'd get hints to do this (or that) )
 thus, there is a specific type of effort, by Adding, or subtracting `the line of code  that saves` the `repo`,
 as a whole, rendering it functioning. That for sure does exist, but is of a *rare kind*
 
  
  
## 9-4-2022

### Added 

`serviceRendered ` a CreditAccount Object, to model the service rendered 
it can be product purchased `purchases`


## 9-4-2022

## Updated 
`RevenueAccount` which is a `+ Capital[Cr]` or a  `CreditAccount`
`ExpenditureAccount` which is a `- Capital[Cr] = [Dr]` a `DebitAccount`
