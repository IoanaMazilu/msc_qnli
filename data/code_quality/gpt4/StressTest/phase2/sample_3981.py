cost_per_day_premise = 0.5
cost_per_day_hypothesis = 0.5
charge_time_premise = 12
charge_time_hypothesis = 42

# the hypothesis refers to the cost per day and the charge off time for Adams's internet provider, mentioned in the premise
if cost_per_day_hypothesis != cost_per_day_premise:
    # check if the cost per day in the hypothesis contradicts the cost per day reported in the premise
    label = "contradiction"
elif charge_time_hypothesis >= charge_time_premise:
    # check if the charge off time in the hypothesis contradicts the charge off time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
