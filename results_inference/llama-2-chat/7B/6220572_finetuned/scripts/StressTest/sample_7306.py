work_hours_premise = [2, 5, 5, 5]
work_hours_hypothesis = [9, 5, 5, 5]

# the hypothesis refers to the number of work hours per day on each day of the week, mentioned in the premise
if work_hours_premise[0] == work_hours_hypothesis[0]:
    # check if the estimate of 'work_hours_hypothesis[0]' contradicts the number of work hours reported in the premise
    label = "contradiction"
elif work_hours_premise[1]!= work_hours_hypothesis[1]:
    # check if the number of work hours on Monday, Wednesday and Friday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
elif work_hours_premise[2]!= work_hours_hypothesis[2]:
    # check if the number of work hours on Tuesday and Thursday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
