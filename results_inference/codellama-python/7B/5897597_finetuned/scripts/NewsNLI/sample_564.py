loyalty_scheme_non_redeemers_premise = 0.4
loyalty_scheme_non_redeemers_hypothesis = 0.4

# the hypothesis mentions the percentage of passengers who never redeem loyalty miles, which is also referenced in the premise
if loyalty_scheme_non_redeemers_hypothesis!= loyalty_scheme_non_redeemers_premise:
    # check if the percentage of passengers who never redeem loyalty miles in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
