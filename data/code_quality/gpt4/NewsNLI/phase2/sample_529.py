offer_premise = 100
offer_hypothesis = 100

# the hypothesis mentions the value offered by the lottery commission, which is also mentioned in the premise
if offer_hypothesis != offer_premise:
    # check if the value offered in the hypothesis contradicts the value offered in the premise
    label = "contradiction"
else:
    # if the value offered in the hypothesis does not contradict the value offered in the premise, we can infer entailment
    label = "entailment"

print(label)
