# Define variables for the premise and hypothesis
sides_bc_premise = 3
sides_ca_premise = 4
sides_ab_premise = 5
sides_bc_hypothesis = 7
sides_ca_hypothesis = 4
sides_ab_hypothesis = 5

# Check if the hypothesis values contradict the premise
if sides_bc_hypothesis!= sides_bc_premise:
    label = "contradiction"
elif sides_ca_hypothesis!= sides_ca_premise:
    label = "contradiction"
elif sides_ab_hypothesis!= sides_ab_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
