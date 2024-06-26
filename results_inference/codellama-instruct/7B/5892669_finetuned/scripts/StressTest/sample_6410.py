offer_premise = 20
offer_hypothesis = 80

# the hypothesis refers to the discount offer on a shirt mentioned in the premise
if offer_hypothesis!= offer_premise:
    # check if the discount offer in the hypothesis contradicts the discount offer reported in the premise
    label = "contradiction"
else:
    # if the discount offer in the hypothesis does not contradict the discount offer in the premise, we can infer entailment
    label = "entailment"

print(label)
