work_time_premise = 10
work_time_hypothesis = 20

# the hypothesis refers to Sakshi's time to complete a piece of work, which is also mentioned in the premise
if work_time_hypothesis <= work_time_premise:
    # check if the hypothesis value contradicts the premise that Sakshi needs more than 'work_time_premise' days to complete the work
    label = "contradiction"
else:
    # the premise gives only an estimate for the minimum time needed by Sakshi to complete the work
    # any time greater than 'work_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
