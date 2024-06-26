profit_share_premise = 1970
profit_share_hypothesis = 6970

# The hypothesis refers to Sameer's share in profit, also mentioned in the premise
if profit_share_hypothesis <= profit_share_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'profit_share_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the share in profit
    # Any share greater than 'profit_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
