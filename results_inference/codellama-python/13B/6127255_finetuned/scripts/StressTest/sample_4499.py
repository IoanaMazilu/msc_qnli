cost_price_premise = 12
cost_price_hypothesis = 12

# the hypothesis refers to the same selling price mentioned in the premise
if cost_price_hypothesis <= cost_price_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the selling price
    # any selling price greater than 'cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
