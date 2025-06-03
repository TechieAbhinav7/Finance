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
