amount_premise = 7450
amount_hypothesis = 3450

# the hypothesis refers to the amount of money from Anwar, which is also discussed in the premise
if amount_hypothesis >= amount_premise:
    # check if the hypothesis value contradicts the estimate of less than 'amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount
    # any amount of money less than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
