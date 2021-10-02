def atm():
    withdrawal_amount = int(input())
    initial_balance = float(input())
    if withdrawal_amount <= initial_balance + 0.50 and withdrawal_amount % 5 == 0:
        return initial_balance - (withdrawal_amount + 0.50)
    else:
        return initial_balance

    
print(atm())
