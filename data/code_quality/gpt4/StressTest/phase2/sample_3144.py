on_time_rate_premise = 50
on_time_rate_hypothesis = 30

# the hypothesis refers to the on-time departure rate mentioned in the premise
if on_time_rate_hypothesis >= on_time_rate_premise:
    # check if the 'on_time_rate_hypothesis' contradicts the on-time departure rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
