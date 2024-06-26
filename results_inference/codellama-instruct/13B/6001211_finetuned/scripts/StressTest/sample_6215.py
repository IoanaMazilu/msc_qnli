work_hours_premise = 10
work_hours_hypothesis = 70

# the hypothesis refers to the number of work hours per day mentioned in the premise
if work_hours_premise!= work_hours_hypothesis:
    # check if the number of work hours in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
