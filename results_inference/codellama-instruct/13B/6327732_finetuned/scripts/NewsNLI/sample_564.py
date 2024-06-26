poll_size_premise = 1005
poll_size_hypothesis = 1005
loyalty_scheme_premise = 0.4
loyalty_scheme_hypothesis = 0.4

# the hypothesis mentions the same percentage of passengers who never redeem loyalty miles as the premise
if loyalty_scheme_hypothesis!= loyalty_scheme_premise:
    # check if the percentage of passengers who never redeem loyalty miles from the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
