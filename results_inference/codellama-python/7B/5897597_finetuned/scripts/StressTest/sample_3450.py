joining_time_premise = 2
joining_time_hypothesis = 8

# the hypothesis refers to the time Jose joined, which is also mentioned in the premise
if joining_time_premise > joining_time_hypothesis:
    # check if the time in the premise contradicts the estimate of less than 'joining_time_hypothesis'
    label = "contradiction"
elif joining_time_premise < joining_time_hypothesis:
    # if the time in the premise is less than 'joining_time_hypothesis', it can be explicitly entailed from the hypothesis
    label = "entailment"
else:
    # if the time in the premise is equal to 'joining_time_hypothesis', it is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)
