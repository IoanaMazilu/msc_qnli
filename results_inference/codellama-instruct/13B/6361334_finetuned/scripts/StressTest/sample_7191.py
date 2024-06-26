premise_time = 12
hypothesis_time = 82

# the hypothesis refers to the time of departure of the train, which is also mentioned in the premise
if hypothesis_time >= premise_time:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact time of departure, but the hypothesis gives a less than value
    # any departure time less than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
