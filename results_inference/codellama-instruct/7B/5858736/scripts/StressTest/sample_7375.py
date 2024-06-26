# Define variables with representative names for the numerical entities in both inputs
hours_worked_premise = 36
hours_worked_hypothesis = 16
orders_per_hour_premise = 40
orders_per_hour_hypothesis = 40

# Extract all quantities as valid numbers
hours_worked_premise = int(hours_worked_premise)
hours_worked_hypothesis = int(hours_worked_hypothesis)
orders_per_hour_premise = float(orders_per_hour_premise)
orders_per_hour_hypothesis = float(orders_per_hour_hypothesis)

# Calculate the total hours worked and the total orders earned
total_hours_worked_premise = hours_worked_premise * 4
total_hours_worked_hypothesis = hours_worked_hypothesis * 4
total_orders_earned_premise = total_hours_worked_premise * orders_per_hour_premise
total_orders_earned_hypothesis = total_hours_worked_hypothesis * orders_per_hour_hypothesis

# Compare the total hours worked and the total orders earned
if total_hours_worked_hypothesis <= total_hours_worked_premise:
    # Check if the estimate of 'total_hours_worked_hypothesis' contradicts the total hours worked in the premise
    label = "contradiction"
elif total_orders_earned_hypothesis <= total_orders_earned_premise:
    # Check if the estimate of 'total_orders_earned_hypothesis' contradicts the total orders earned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
