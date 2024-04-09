commute_time_premise = 15
commute_time_hypothesis = 15

# the hypothesis talks about the time it takes Darcy to commute to work by walking, referenced also in the premise
if commute_time_hypothesis <= commute_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'commute_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the commute time, any value greater than 'commute_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
