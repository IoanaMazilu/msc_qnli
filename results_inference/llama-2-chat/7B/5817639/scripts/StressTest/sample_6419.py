# Define variables for the premise and hypothesis
gang_premise = 3
gang_hypothesis = 7

# Check if the hypothesis value contradicts the premise value
if gang_hypothesis <= gang_premise:
    label = "contradiction"
else:
    # The premise value is less than or equal to the hypothesis value, so we can infer entailment
    label = "entailment"

print(label)
