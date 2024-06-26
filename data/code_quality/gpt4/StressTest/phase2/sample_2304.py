cleaning_time_premise = 4
cleaning_time_hypothesis = 7

# the hypothesis refers to the time Bruce and Anne spend cleaning their house, also mentioned in the premise
if cleaning_time_premise > cleaning_time_hypothesis:
    # check if the time 'cleaning_time_premise' contradicts the estimate of less than 'cleaning_time_hypothesis'
    label = "contradiction"
elif cleaning_time_premise < cleaning_time_hypothesis:
    # the premise gives an exact time for the cleaning
    # so we can infer from it that any time less than 'cleaning_time_hypothesis' is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value and the premise value are the same, we can infer entailment
    label = "entailment"

print(label)
