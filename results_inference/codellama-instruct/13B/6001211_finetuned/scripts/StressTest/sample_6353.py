profit_premise = 22000
profit_hypothesis = 22000

# the hypothesis refers to the profit mentioned in the premise
if profit_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact value for the profit
    # any profit greater than 'profit_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
