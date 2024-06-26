hours_dan_premise = 6
hours_dan_hypothesis = 6
hours_annie_premise = 6
hours_annie_hypothesis = 6

# the hypothesis refers to the number of hours Dan works and Annie works, both mentioned in the premise
if hours_dan_hypothesis <= hours_dan_premise:
    # check if the estimate of 'hours_dan_hypothesis' contradicts the number of hours Dan works in the premise
    label = "contradiction"
elif hours_annie_hypothesis!= hours_annie_premise:
    # check if the number of hours Annie works in the hypothesis contradicts the number of hours Annie works reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
