work_days_mary_premise = 11
work_days_mary_hypothesis = 11

# the hypothesis refers to the number of days Mary can do a piece of work, mentioned in the premise
if work_days_mary_hypothesis <= work_days_mary_premise:
    # check if the estimate of 'work_days_mary_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
