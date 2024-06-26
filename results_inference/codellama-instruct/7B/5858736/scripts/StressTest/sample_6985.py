# Define variables with representative names for the numerical entities in both inputs
total_pens_purchased_premise = 22
total_pens_purchased_hypothesis = 12
total_cost_premise = 42.00
total_cost_hypothesis = 42.00

# Extract all quantities as valid numbers (integers or floats)
total_pens_purchased_premise = int(total_pens_purchased_premise)
total_pens_purchased_hypothesis = int(total_pens_purchased_hypothesis)
total_cost_premise = float(total_cost_premise)
total_cost_hypothesis = float(total_cost_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if total_cost_hypothesis <= total_cost_premise:
    # Check if the estimate of 'total_cost_hypothesis' contradicts the total cost mentioned in the premise
    label = "contradiction"
elif total_pens_purchased_hypothesis!= total_pens_purchased_premise:
    # Check if the number of pens purchased in the hypothesis contradicts the number of pens purchased reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
