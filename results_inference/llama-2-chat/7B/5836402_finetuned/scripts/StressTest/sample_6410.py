offer_premise = 20
offer_hypothesis = 80

# the hypothesis refers to the offer for shirts, which is also mentioned in the premise
if offer_hypothesis!= offer_premise:
    # check if the offer in the hypothesis contradicts the offer in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
