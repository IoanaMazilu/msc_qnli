# The premise and hypothesis are the same, but with different ratios
ratio_premise = 3/2
ratio_hypothesis = 2/2

# The premise states a specific ratio of car and AC prices
if ratio_premise <= ratio_hypothesis:
    # If the ratio in the premise is less than or equal to the ratio in the hypothesis, it is an entailment
    label = "entailment"
elif ratio_premise > ratio_hypothesis:
    # If the ratio in the premise is greater than the ratio in the hypothesis, it is a contradiction
    label = "contradiction"
else:
    # If the ratios are the same, it is a neutral case
    label = "neutral"

print(label)
