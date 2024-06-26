joining_time_premise = 2
joining_time_hypothesis = 5

# the hypothesis refers to the time when Jose joined him, also mentioned in the premise
if joining_time_premise > joining_time_hypothesis:
    # check if the time in the premise contradicts the estimate of less than 'joining_time_hypothesis' in the hypothesis
    label = "contradiction"
else:
    # if the premise does not contradict the hypothesis, it can be inferred as entailment
    label = "entailment"

print(label)
