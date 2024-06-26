time_premise = 6
time_hypothesis = 7

# the hypothesis talks about the time required by a train to cover the distance between Chennai and Jammu, referenced also in the premise
if time_hypothesis <= time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time greater than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
