work_premise = 40
work_hypothesis = 40

# the premise and hypothesis refer to the same work
if work_hypothesis <= work_premise:
    # check if the estimate of 'work_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days,
    # any number of days greater than 'work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
