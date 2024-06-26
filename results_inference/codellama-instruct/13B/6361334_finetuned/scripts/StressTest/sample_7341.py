profit_premise = 6970
profit_hypothesis = 1970

# the hypothesis refers to the share of Sameer in the profit, which is not mentioned in the premise
if profit_hypothesis <= profit_premise:
    # check if the estimate of 'profit_hypothesis' contradicts the profit in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit
    # any profit greater than 'profit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
