# The hypothesis refers to the ratio of sheep and horses at the farm, which is also mentioned in the premise
if hypothesis_sheep_horses_ratio!= premise_sheep_horses_ratio + 1:
    # Check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif hypothesis_sheep_horses_ratio > premise_sheep_horses_ratio + 7:
    # Check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # If the ratios do not contradict, we can infer entailment
    label = "entailment"

print(label)
