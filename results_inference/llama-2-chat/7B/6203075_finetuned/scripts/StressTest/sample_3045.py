work_hours_premise = 8
work_hours_hypothesis = 5

# the hypothesis refers to the number of work hours per day, which is also mentioned in the premise
if work_hours_hypothesis!= work_hours_premise:
    # check if the number of work hours in the hypothesis contradicts the number of work hours in the premise
    label = "contradiction"
else:
    # if the number of work hours in the hypothesis does not contradict the number of work hours in the premise, we can infer entailment
    label = "entailment"

print(label)
