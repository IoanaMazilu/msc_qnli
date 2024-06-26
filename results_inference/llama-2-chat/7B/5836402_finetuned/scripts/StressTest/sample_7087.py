dan_work_hours_premise = 8
dan_work_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works, mentioned in the premise
if dan_work_hours_hypothesis >= dan_work_hours_premise:
    # check if the estimate of 'dan_work_hours_hypothesis' contradicts the number of hours Dan works in the premise
    label = "contradiction"
elif dan_work_hours_hypothesis < dan_work_hours_premise:
    # if the number of hours Dan works in the hypothesis is less than the number of hours in the premise, it is entailed
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
