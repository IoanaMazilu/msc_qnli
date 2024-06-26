x_dollars_per_hour_premise = 1
x_dollars_per_hour_hypothesis = 2

# the hypothesis refers to the pay per hour for the first and additional hours worked, mentioned also in the premise
if x_dollars_per_hour_hypothesis!= x_dollars_per_hour_premise:
    # check if the pay per hour in the hypothesis contradicts the pay per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
