profit_share_premise = 6970
profit_share_hypothesis = 1970

# the hypothesis refers to the profit share of Sameer mentioned in the premise
if profit_share_premise <= profit_share_hypothesis:
    # check if the estimate of 'profit_share_hypothesis' contradicts the profit share in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
