amount_withdrawn_premise = 5000
amount_withdrawn_hypothesis = 2000

# the hypothesis value contradicts the estimate in the premise
if amount_withdrawn_hypothesis <= amount_withdrawn_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount withdrawn
    # any amount less than 'amount_withdrawn_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
