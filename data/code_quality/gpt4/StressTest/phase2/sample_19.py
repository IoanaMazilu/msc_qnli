work_hours_premise = 70
work_hours_hypothesis = 10

# the hypothesis refers to the working hours mentioned in the premise
if work_hours_hypothesis >= work_hours_premise:
    # check if the 'work_hours_hypothesis' contradicts the number of working hours in the premise
    label = "contradiction"
elif work_hours_hypothesis < work_hours_premise:
    # check if the 'work_hours_hypothesis' can be inferred from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
