cleaning_time_premise = 6
cleaning_time_hypothesis = 1

# the hypothesis refers to the cleaning time of the house, which is also mentioned in the premise
if cleaning_time_premise >= cleaning_time_hypothesis:
    # check if the estimate of 'cleaning_time_hypothesis' contradicts the cleaning time in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
