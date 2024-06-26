# Define the variables for the premise and hypothesis
ana_premise = 8
ana_hypothesis = 8

# The hypothesis refers to the time Ana goes before, which is also mentioned in the premise
if ana_hypothesis >= ana_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
elif ana_hypothesis < ana_premise:
    # If the hypothesis value is less than the premise, we can infer entailment
    label = "entailment"
# If the hypothesis value is equal to the premise, we cannot infer entailment or contradiction
else:
    label = "neutral"

print(label)