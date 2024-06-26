average_fall_premise = 6
average_fall_hypothesis = 1

# the hypothesis talks about the number of seconds the average falls after Izzy finishes a sprint, referenced also in the premise
if average_fall_hypothesis > average_fall_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_fall_premise' seconds
    label = "contradiction"
elif average_fall_hypothesis < average_fall_premise:
    # the premise gives only an estimate for the number of seconds the average falls
    # any number of seconds less than 'average_fall_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
