# Define variables for the numerical entities in the premise and hypothesis
days_premise = 10
efficiency_premise = 0.35

# Define variables for the numerical entities in the hypothesis
days_hypothesis = 10
efficiency_hypothesis = 0.25

# Check if the hypothesis value contradicts the premise
if days_hypothesis <= days_premise:
    label = "contradiction"
elif efficiency_hypothesis <= efficiency_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
