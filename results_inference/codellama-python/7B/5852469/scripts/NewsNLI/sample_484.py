endorsement_deal_premise = 1
endorsement_deal_hypothesis = 1

# the hypothesis mentions the endorsement deal that Hernandez has already lost, which is also mentioned in the premise
if endorsement_deal_hypothesis!= endorsement_deal_premise:
    # check if the endorsement deal from the hypothesis contradicts the endorsement deal in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
