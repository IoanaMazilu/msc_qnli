joining_time_premise = 2
joining_time_hypothesis = 8

# the hypothesis talks about the time Jose joined him, referenced also in the premise
if joining_time_hypothesis <= joining_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'joining_time_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an estimate for the joining time
    # any joining time less than 'joining_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
