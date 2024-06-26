# Define variables with representative names for the numerical entities in both inputs
jose_joined_premise = 2
jose_joined_hypothesis = 8
jose_investment_premise = Rs.
jose_investment_hypothesis = Rs.

# Extract all quantities as valid numbers (integers or floats)
jose_joined_premise = int(jose_joined_premise)
jose_joined_hypothesis = int(jose_joined_hypothesis)
jose_investment_premise = float(jose_investment_premise)
jose_investment_hypothesis = float(jose_investment_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if jose_joined_hypothesis <= jose_joined_premise:
    # Check if the estimate of 'jose_joined_hypothesis' contradicts the number of months between the two events
    label = "contradiction"
elif jose_investment_hypothesis!= jose_investment_premise:
    # Check if the estimate of 'jose_investment_hypothesis' contradicts the amount invested
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
