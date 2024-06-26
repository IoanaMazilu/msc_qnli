offer_premise = 30
offer_hypothesis = 80

# the hypothesis refers to the discount offer on a shirt mentioned in the premise
if offer_hypothesis!= offer_premise:
    # check if the discount offer in the hypothesis contradicts the discount offer reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
