amount_premise = 750
amount_hypothesis = 450

# the hypothesis refers to the amount sold, which is also mentioned in the premise
if amount_hypothesis >= amount_premise:
    # check if the hypothesis value contradicts the estimate of less than 'amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount
    # any amount less than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
