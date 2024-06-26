marie_account_premise = 248
marie_account_hypothesis = 148

# the hypothesis refers to the same amount of money as the premise
if marie_account_hypothesis <= marie_account_premise:
    # check if the estimate of'marie_account_hypothesis' contradicts the number of money in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money
    # any amount of money greater than'marie_account_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
