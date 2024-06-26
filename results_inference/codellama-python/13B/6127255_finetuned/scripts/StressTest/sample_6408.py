offer_premise = 20
offer_hypothesis = 80

# the hypothesis refers to the shop's offer mentioned in the premise
if offer_hypothesis <= offer_premise:
    # check if the hypothesis value contradicts the premise offer
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise offer, we can infer entailment
    label = "entailment"

print(label)
