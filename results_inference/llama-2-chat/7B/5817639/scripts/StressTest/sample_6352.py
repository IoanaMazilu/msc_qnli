profit_premise = 42000
profit_hypothesis = 22000

# the hypothesis talks about the profit of a business, referenced also in the premise
if profit_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the estimate of less than 'profit_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the profit, and the hypothesis provides an estimate that is less than the premise
    # any profit less than 'profit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)