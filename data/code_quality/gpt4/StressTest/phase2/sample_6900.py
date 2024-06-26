offer_premise = 30
offer_hypothesis = 70

# The hypothesis refers to the shop's offer mentioned in the premise
if offer_hypothesis <= offer_premise:
    # Check if the offer percentage in the hypothesis contradicts the offer percentage in the premise
    label = "contradiction"
else:
    # If the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
