amount_premise = 3
amount_hypothesis = 7

# the hypothesis talks about the percentage of amount Dana gives back to her parents, referenced in the premise
if amount_hypothesis <= amount_premise:
    # check if the hypothesis value contradicts the estimate of 'amount_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the amount, and any amount greater than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
