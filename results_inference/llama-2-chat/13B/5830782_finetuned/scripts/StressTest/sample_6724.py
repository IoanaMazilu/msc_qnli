amount_premise = 1600
amount_hypothesis = 3600
interest_rate = 6  # since it's the same in both premise and hypothesis, no need to compare

# the hypothesis refers to the amount from Anwar mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the hypothesis value contradicts the estimate of more than 'amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount
    # any amount greater than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
