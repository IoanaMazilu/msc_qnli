work_days_premise = 24
work_days_hypothesis = 64

# the hypothesis refers to the number of days Matt and Peter can do a piece of work, mentioned also in the premise
if work_days_premise > work_days_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of less than 'work_days_hypothesis' days
    label = "contradiction"
elif work_days_premise != work_days_hypothesis:
    # check if the premise value is different from the hypothesis one
    # any number of days less than 'work_days_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"
else:
    # if the premise value and the hypothesis estimate do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
