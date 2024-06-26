work_days_premise = 24
work_days_hypothesis = 14

# the hypothesis refers to the number of days Matt and Peter need to do a piece of work, mentioned also in the premise
if work_days_hypothesis != work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
