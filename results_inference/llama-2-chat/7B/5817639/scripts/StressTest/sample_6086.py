work_days_premise = 20
work_days_hypothesis = 30

# check if the hypothesis value contradicts the estimate of 'work_days_premise'
if work_days_hypothesis > work_days_premise:
    label = "contradiction"
elif work_days_hypothesis == work_days_premise:
    # the hypothesis and premise values match, so we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the number of work days,
    # so any number of work days greater than 'work_days_premise' is consistent with the premise,
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
