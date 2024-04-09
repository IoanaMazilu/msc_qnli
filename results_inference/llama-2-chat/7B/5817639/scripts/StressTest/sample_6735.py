work_days_premise = 12
work_days_hypothesis = 22

# the hypothesis talks about the time it would take Rohit and Rohan to complete a work, referenced also in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it would take Rohit and Rohan to complete a work
    # any time less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
