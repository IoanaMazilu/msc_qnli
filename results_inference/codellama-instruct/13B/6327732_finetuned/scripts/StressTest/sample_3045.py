hours_per_day_premise = [8, 6, 6]
hours_per_day_hypothesis = [5, 6, 6]

# the hypothesis refers to the number of hours worked per day on specific days, mentioned in the premise
if hours_per_day_hypothesis[0] <= hours_per_day_premise[0]:
    # check if the estimate of 'hours_per_day_hypothesis[0]' contradicts the number of hours worked on Monday in the premise
    label = "contradiction"
elif hours_per_day_hypothesis[1]!= hours_per_day_premise[1]:
    # check if the number of hours worked on Tuesday in the hypothesis contradicts the number of hours worked on Tuesday reported in the premise
    label = "contradiction"
elif hours_per_day_hypothesis[2]!= hours_per_day_premise[2]:
    # check if the number of hours worked on Thursday in the hypothesis contradicts the number of hours worked on Thursday reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
