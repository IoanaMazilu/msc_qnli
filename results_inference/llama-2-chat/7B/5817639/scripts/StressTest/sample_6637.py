work_completion_premise = 50
work_completion_hypothesis = 30

# the hypothesis talks about the time it takes to complete a work, referenced also in the premise
if work_completion_hypothesis <= work_completion_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_completion_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it takes to complete a work, but the hypothesis provides a more specific value
    # any time less than 'work_completion_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
