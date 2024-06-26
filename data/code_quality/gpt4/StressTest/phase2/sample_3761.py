work_days_premise = 12
work_days_hypothesis = 12

# the hypothesis refers to the number of days Mary can do a piece of work, mentioned in the premise
if work_days_hypothesis != work_days_premise:
    # check if the number of days in the hypothesis contradicts the exact number of work days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
