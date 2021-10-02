def helping_families(money_required, total_houses, count):

    # base case
    if money_required < 0:
        return
    if money_required > 0 and total_houses <= 0:
        return
    if money_required == 0:
        count += 1
        return
    if total_houses <= 0:
        return
    
