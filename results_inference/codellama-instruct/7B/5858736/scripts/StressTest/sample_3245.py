# Define variables for the premise and hypothesis
consumable_spending_premise = 0.6
clothes_transport_spending_premise = 0.5

# Define variables for the hypothesis
consumable_spending_hypothesis = 0.4
clothes_transport_spending_hypothesis = 0.5

# Check if the hypothesis values contradict the premise
if consumable_spending_hypothesis >= consumable_spending_premise:
    label = "contradiction"
elif clothes_transport_spending_hypothesis!= clothes_transport_spending_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
