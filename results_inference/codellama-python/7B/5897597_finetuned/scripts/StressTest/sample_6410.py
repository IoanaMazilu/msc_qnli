offer_premise = 20
offer_hypothesis = 80

# the hypothesis refers to the discount offer mentioned in the premise
if offer_premise!= offer_hypothesis:
    # check if the discount offer in the hypothesis contradicts the discount offer in the premise
    label = "contradiction"
else:
    # if the discount offers in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
