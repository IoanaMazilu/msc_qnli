# the hypothesis talks about the number of shifts and the average order value per hour, both referenced also in the premise
if hypothesis_shifts!= 4:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
elif hypothesis_avg_orders_per_hour!= 40:
    # check if the average order value per hour in the hypothesis contradicts the average order value per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
