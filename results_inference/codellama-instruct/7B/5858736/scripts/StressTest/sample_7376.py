# Define variables with representative names for the numerical entities in both inputs
orders_per_hour_premise = 40
hours_worked_premise = 16
total_orders_premise = orders_per_hour_premise * hours_worked_premise

# Extract all quantities as valid numbers (integers or floats)
orders_per_hour_hypothesis = 40
hours_worked_hypothesis = 16
total_orders_hypothesis = orders_per_hour_hypothesis * hours_worked_hypothesis

# Use brief comments to explain what comparison you do between the defined variables
if total_orders_hypothesis <= total_orders_premise:
    # Check if the estimate of 'total_orders_hypothesis' contradicts the total number of orders reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
