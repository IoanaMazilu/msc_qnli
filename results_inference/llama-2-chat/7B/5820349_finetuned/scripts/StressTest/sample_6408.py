offer_premise = 20
offer_hypothesis = 80

# the hypothesis refers to the offer percentage for shirts mentioned in the premise
if offer_hypothesis < offer_premise:
    # check if the estimate of 'offer_hypothesis' contradicts the offer percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
