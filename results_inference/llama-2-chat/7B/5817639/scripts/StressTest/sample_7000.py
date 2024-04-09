work_finish_premise = 60
work_finish_hypothesis = 20

# the hypothesis talks about the time it takes for Ramesh and Sushil to finish a work
if work_finish_hypothesis <= work_finish_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_finish_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it takes for Ramesh to finish a work
    # any time less than 'work_finish_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
