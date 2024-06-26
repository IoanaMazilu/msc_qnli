profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit in the business at the end of the year mentioned in the premise
if profit_premise >= profit_hypothesis:
    # check if the estimate of 'profit_hypothesis' contradicts the profit in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit
    # any profit less than 'profit_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
