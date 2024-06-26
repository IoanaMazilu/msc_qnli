traffic_cost_per_day_premise = 0.5
traffic_cost_per_day_hypothesis = 0.5
charge_off_time_premise = 12
charge_off_time_hypothesis = 52

# the hypothesis refers to the cost and the charge off time of the internet traffic mentioned in the premise
if traffic_cost_per_day_hypothesis != traffic_cost_per_day_premise:
    # check if the cost per day in the hypothesis contradicts the cost per day reported in the premise
    label = "contradiction"
elif charge_off_time_hypothesis >= charge_off_time_premise:
    # check if the 'charge_off_time_hypothesis' contradicts 'charge_off_time_premise' value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
