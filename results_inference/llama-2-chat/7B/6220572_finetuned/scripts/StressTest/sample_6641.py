work_completion_premise = 40
work_completion_hypothesis = 40

# the hypothesis talks about the time needed to complete the same work, referenced also in the premise
if work_completion_hypothesis == work_completion_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_completion_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time needed to complete the work
    # any time greater than 'work_completion_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
