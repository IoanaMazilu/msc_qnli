oil_shortfall_premise = 1.5
oil_shortfall_hypothesis = 1.5

# the hypothesis and premise mention the shortfall in oil production needed to meet demand unless supply exceeds demand
if oil_shortfall_hypothesis!= oil_shortfall_premise:
    # check if the shortfall estimate in the hypothesis contradicts the shortfall estimate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
