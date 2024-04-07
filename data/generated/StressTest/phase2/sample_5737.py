# Premise: Matt and Peter can do together a piece of work in less than 70 days.
# Hypothesis: Matt and Peter can do together a piece of work in 20 days.
# Golden Label: neutral

work_time_premise = 70
work_time_hypothesis = 20

# the hypothesis talks about time taken to do a piece of work by Matt and Peter, also referenced in the premise
if work_time_hypothesis >= work_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken to do the work
    # any time less than 'work_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

