pay_per_hour_premise = 1
pay_per_hour_hypothesis = 1
hour_limit_premise = 10
hour_limit_hypothesis = 30

# the hypothesis refers to the pay per hour and the limit of hours worked, both mentioned in the premise
if pay_per_hour_hypothesis!= pay_per_hour_premise:
    # check if the pay per hour in the hypothesis contradicts the pay per hour reported in the premise
    label = "contradiction"
elif hour_limit_hypothesis < hour_limit_premise:
    # check if the limit of hours worked in the hypothesis contradicts the limit of hours worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
