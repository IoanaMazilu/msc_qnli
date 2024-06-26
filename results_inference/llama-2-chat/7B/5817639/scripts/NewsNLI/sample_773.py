import math

# Define variables for premise and hypothesis
turkey_trade_premise = 1
turkey_trade_hypothesis = 1

# Check if the hypothesis contradicts the premise
if turkey_trade_hypothesis!= turkey_trade_premise:
    # If the hypothesis value is different from the premise value, it contradicts
    label = "contradiction"
else:
    # If the hypothesis value is the same as the premise value, it entails
    label = "entailment"

# Print the label
print(label)
