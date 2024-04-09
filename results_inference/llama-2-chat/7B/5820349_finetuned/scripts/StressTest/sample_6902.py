offer_premise = 30
offer_hypothesis = 80

# the hypothesis refers to the discount percentage offered on a shirt, which is also mentioned in the premise
if offer_hypothesis!= offer_premise:
    # check if the discount percentage in the hypothesis contradicts the discount percentage mentioned in the premise
    label = "contradiction"
else:
    # if the discount percentage in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
