commute_time_premise = 15
commute_time_hypothesis = 55

# the hypothesis refers to the number of minutes Darcy spends to commute to work by walking and the train
if commute_time_hypothesis >= commute_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'commute_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of minutes Darcy spends to commute to work
    # any number of minutes less than 'commute_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
