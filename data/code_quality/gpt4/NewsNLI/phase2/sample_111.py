bid_premise = 1000000 - 1
bid_hypothesis = 1000000

# the hypothesis refers to the top bid at press time, which is also mentioned in the premise
if bid_hypothesis != bid_premise:
    # check if the bid in the hypothesis contradicts the bid reported in the premise
    label = "contradiction"
else:
    # if the bid in the hypothesis does not contradict the bid in the premise, we can infer entailment
    label = "entailment"

print(label)
