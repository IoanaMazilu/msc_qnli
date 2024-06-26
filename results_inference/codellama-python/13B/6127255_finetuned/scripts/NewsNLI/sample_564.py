citizens_premise = 1005
loyalty_scheme_never_redeem_premise = 0.40
loyalty_scheme_never_redeem_hypothesis = 0.40

# the hypothesis mentions the percentage of passengers who never redeem loyalty miles, which is also mentioned in the premise
if loyalty_scheme_never_redeem_hypothesis!= loyalty_scheme_never_redeem_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
