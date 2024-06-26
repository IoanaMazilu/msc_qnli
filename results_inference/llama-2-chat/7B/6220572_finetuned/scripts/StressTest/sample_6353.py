profit_premise = 22000
profit_hypothesis = 22000

# the hypothesis refers to the profit mentioned in the premise
if profit_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the profit in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit
    # any profit greater than 'profit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
