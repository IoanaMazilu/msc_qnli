raj_roshan_ratio_premise = 5 / 4
raj_roshan_ratio_hypothesis = 8 / 4

# The hypothesis refers to the money ratio between Raj and Roshan
if raj_roshan_ratio_hypothesis <= raj_roshan_ratio_premise:
    # Check if the ratio in the hypothesis contradicts the ratio stated in the premise
    label = "contradiction"
elif raj_roshan_ratio_hypothesis > raj_roshan_ratio_premise:
    # If the ratio in the hypothesis is greater than the ratio in the premise, it could be neutral
    label = "neutral"
else:
    # If the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
