work_days_premise = 20
work_days_hypothesis = 25

# the hypothesis talks about the time it takes for Ramesh and Sushil to finish a work
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the estimate of 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it takes Ramesh to finish a work
    # any time greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
