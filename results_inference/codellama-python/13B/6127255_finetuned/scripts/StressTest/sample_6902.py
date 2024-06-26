offer_premise = 30
offer_hypothesis = 80

# the hypothesis talks about the discount offer on a shirt, referenced also in the premise
if offer_hypothesis!= offer_premise:
    # check if the discount offer in the hypothesis contradicts the discount offer mentioned in the premise
    label = "contradiction"
else:
    # if the discount offers are the same, we can infer entailment
    label = "entailment"

print(label)
