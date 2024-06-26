cost_per_day_premise = 0.5
cost_per_day_hypothesis = 0.5
charge_off_time_premise = 12
charge_off_time_hypothesis = 32

# the hypothesis refers to the cost per day and charge off time of Lally's internet provider, mentioned also in the premise
if cost_per_day_premise != cost_per_day_hypothesis:
    # check if the cost per day in the hypothesis contradicts the cost per day reported in the premise
    label = "contradiction"
elif charge_off_time_hypothesis != charge_off_time_premise:
    # check if the charge off time in the hypothesis contradicts the charge off time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
