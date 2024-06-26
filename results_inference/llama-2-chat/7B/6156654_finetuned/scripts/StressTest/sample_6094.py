# Define the premise and hypothesis
premise = 8
hypothesis = 9

# The hypothesis refers to a specific number greater than 8, which is also mentioned in the premise
if hypothesis <= premise:
    # If the hypothesis value contradicts the premise, the relation is neutral
    label = "neutral"
elif hypothesis > premise:
    # If the hypothesis value is greater than the premise, it entails the premise
    label = "entailment"
else:
    # If the hypothesis value is equal to the premise, it contradicts the premise
    label = "contradiction"

print(label)
