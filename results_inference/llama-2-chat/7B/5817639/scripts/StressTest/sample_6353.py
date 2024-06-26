profit_premise = 22000
profit_hypothesis = 25000

# the hypothesis talks about the profit of a business, which is also referred to in the premise
if profit_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the estimate of the profit in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit, any profit greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
