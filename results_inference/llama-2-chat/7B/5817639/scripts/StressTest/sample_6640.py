work_premise = 20
work_hypothesis = 40

# the hypothesis talks about the time it would take Bhim to complete the work, referenced also in the premise
if work_hypothesis <= work_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_premise' days
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it would take Bhim to complete the work
    # any time greater than 'work_premise' days is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
