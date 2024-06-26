# the hypothesis refers to the number of passengers and airports mentioned in the premise
if hypothesis_premise == hypothesis_hypothesis:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
