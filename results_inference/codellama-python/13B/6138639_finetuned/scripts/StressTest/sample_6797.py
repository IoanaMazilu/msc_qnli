deposit_premise = 62500
deposit_hypothesis = 62500
interest_rate = 8

# the hypothesis refers to the amount deposited by Lucy and the interest rate mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the hypothesis value contradicts the estimate of less than 'deposit_premise'
    label = "contradiction"
else:
    # the premise gives an exact amount for the deposit
    # any amount less than 'deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
