fishing_time_premise = 40
fishing_time_hypothesis = 20

# the hypothesis refers to the fishing time mentioned in the premise
if fishing_time_premise < fishing_time_hypothesis:
    # check if the estimated 'fishing_time_hypothesis' contradicts the fishing time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
