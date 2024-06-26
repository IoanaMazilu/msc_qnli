cost_per_day_premise = 0.5
cost_per_day_hypothesis = 0.5
charge_off_time_premise = 12
charge_off_time_hypothesis = 32

# The hypothesis refers to the cost per day and charge off time for Salley's internet provider
if cost_per_day_hypothesis != cost_per_day_premise:
    # Check if the cost per day in the hypothesis contradicts the cost per day in the premise
    label = "contradiction"
elif charge_off_time_hypothesis != charge_off_time_premise:
    # Check if the charge off time in the hypothesis contradicts the charge off time in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
