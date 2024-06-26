# Define variables for the premise and hypothesis
likely_attack_premise = 0.14
likely_attack_hypothesis = 0.30

# Check if the hypothesis contradicts the premise
if likely_attack_hypothesis!= likely_attack_premise:
    # The hypothesis contradicts the premise, so the label is "contradiction"
    label = "contradiction"
else:
    # The hypothesis does not contradict the premise, so the label is "neutral"
    label = "neutral"

print(label)
