# Define variables for the premise
pay_per_hour_premise = 1
pay_per_hour_hypothesis = 1
max_hours_premise = 35

# Define variables for the hypothesis
more_hours_hypothesis = max_hours_premise + 1

# The hypothesis refers to the number of hours worked per week, which is also mentioned in the premise
if pay_per_hour_hypothesis!= pay_per_hour_premise:
    # Check if the pay per hour in the hypothesis contradicts the pay per hour in the premise
    label = "contradiction"
elif more_hours_hypothesis > max_hours_premise:
    # Check if the number of more hours in the hypothesis contradicts the maximum number of hours in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
