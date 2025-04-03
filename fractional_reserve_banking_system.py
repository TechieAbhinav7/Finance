# # Fractional Reserve Banking System

'''
# - Fractional Reserve Banking is a system where banks are required to keep only a fraction of their deposits as reserves and can loan out the remainder to borrowers.

- The key idea behind this model is that when a customer deposits money in the bank, the bank doesn't keep all of it. 
    Instead, the bank is required to keep a fraction of the deposit (called the reserve ratio) and can lend out the remaining portion (called the loan).

- The money lent out will eventually be deposited again into the banking system, leading to more loans and more deposits, creating a multiplier effect.
'''

# # How Model Reflects Fractional Reserve Banking

'''
1) Initial Deposit: You start with a certain deposit (e.g., 1000).
2) Reserve Ratio: The bank keeps a certain percentage of this deposit as reserves (e.g., 10%).
3) Loan Ratio: The bank loans out the remaining portion (e.g., 90%) to borrowers.
4) Money Creation: The loaned money gets spent by borrowers and deposited back into the bank, thus creating new deposits in the banking system.
5) Cyclic Process: This process repeats itself, with the new deposit (which is a loan from the previous cycle) being loaned out again, creating more deposits and loans. Each cycle reduces the amount available for lending by the reserve ratio.
'''

# # Example

'''
You deposit 1000 in the bank.
The bank keeps 10% (100) as reserves.
The remaining 90% (900) is loaned out.
The loaned money (900) will likely be spent and deposited again, becoming new deposits in the system.
This process repeats itself in a cycle, with the total deposits growing over time due to the money being re-deposited.
'''

# # Conclusion

'''
This model represents the **Fractional Reserve Banking** system, 
where banks are required to keep only a fraction of deposited money 
as reserves, and the remaining portion can be loaned out to borrowers. 
The money that is loaned out is spent and re-deposited into the banking system, 
creating new deposits. This process continues in a cyclic manner, 
with each new deposit being loaned out again, multiplying the total money 
in circulation. The reserve ratio determines how much of the deposit 
the bank must keep in reserves, while the rest can be used for lending.
'''
def simulate_frb():
    deposit = int(input("Please enter the amount: "))
    initial_deposit = deposit
    # deposit = initial_deposit
    loan_ratio = 90/100
    reserve_ratio = 10/100
    cycle = 0
    loan = deposit*loan_ratio
    reserves = deposit*reserve_ratio
    total_loans = 0
    total_reserves = 0
    total_deposits = deposit
    min_threshold = 1

    while reserves > min_threshold:
        total_loans += loan
        total_reserves += reserves
        loan = deposit*loan_ratio
        reserves = deposit*reserve_ratio
        new_deposits = loan
        deposit = new_deposits
        total_deposits += deposit
        cycle += 1

        print(f"Cycle: {cycle} :: Deposit: {deposit:.2f} :: Loan: {loan:.2f} :: Reserve: {reserves:.2f}")

        if reserves <= min_threshold:
            break
    


    print(f"\nIn total, there were total {cycle} cycle of lending and deposits.\n\n")
    print(f"\tThe initial deposit was {initial_deposit:.2f}.")
    # print(f"\tThe total deposits amounted to {total_deposits:.2f}.")
    print(f"\tThe total loans amounted to {total_loans:.2f}.")
    print(f"\tThe total reserves amounted to {total_reserves:.2f}.\n \n \n")

simulate_frb()