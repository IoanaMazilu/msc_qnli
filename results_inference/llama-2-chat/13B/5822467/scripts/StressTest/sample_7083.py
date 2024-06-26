annie_hours_premise = 10
annie_hours_hypothesis = 20

# the hypothesis refers to the number of hours Annie takes to do the job, mentioned in the premise
if annie_hours_premise <= annie_hours_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'annie_hours_premise'
    label = "contradiction"
elif annie_hours_hypothesis < annie_hours_premise:
    # check if the hypothesis value is less than the estimate of 'annie_hours_premise'
    label = "entailment"
else:
    # the premise gives only an estimate for the number of hours Annie takes to do the job
    # any number of hours less than 'annie_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
