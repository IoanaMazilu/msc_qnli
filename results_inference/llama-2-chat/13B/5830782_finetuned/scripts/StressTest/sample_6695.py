amount_premise = 14000
amount_hypothesis = 14000

# the hypothesis refers to the amount after 8 months mentioned in the premise
if amount_hypothesis >= amount_premise:
    # check if the hypothesis value contradicts the estimate of less than 'amount_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact amount
    # any amount less than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
