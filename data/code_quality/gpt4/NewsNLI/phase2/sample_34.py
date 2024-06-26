explosives_kg_premise_min = 30
explosives_kg_premise_max = 35
explosives_kg_hypothesis_min = 30
explosives_kg_hypothesis_max = 35

# The hypothesis and the premise both give an estimated range for the amount of explosives in the car
if explosives_kg_hypothesis_min != explosives_kg_premise_min or explosives_kg_hypothesis_max != explosives_kg_premise_max:
    # Check if either the minimum or maximum estimate of explosives in the hypothesis contradicts the estimates in the premise
    label = "contradiction"
else:
    # If the minimum and maximum estimates in the hypothesis do not contradict the estimates in the premise, we can infer entailment
    label = "entailment"

print(label)
