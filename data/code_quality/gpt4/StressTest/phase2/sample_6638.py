work_days_premise = 30
work_days_hypothesis = 50

# the hypothesis talks about the time Ram, Krish and Bhim can complete a work, referenced also in the premise
if work_days_hypothesis < work_days_premise:
    # check if the hypothesis value contradicts the time 'work_days_premise' taken by Ram, Krish and Bhim to complete a work
    label = "contradiction"
elif work_days_hypothesis > work_days_premise:
    # any time greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and the premise value are equal, we can infer entailment
    label = "entailment"

print(label)
