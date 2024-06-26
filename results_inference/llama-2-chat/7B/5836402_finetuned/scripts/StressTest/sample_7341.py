profit_share_premise = 6970
profit_share_hypothesis = 1970

# the hypothesis refers to the profit share mentioned in the premise
if profit_share_hypothesis <= profit_share_premise:
    # check if the hypothesis value contradicts the estimate of more than 'profit_share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit share
    # any profit share greater than 'profit_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
