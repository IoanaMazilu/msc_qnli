travel_premise = 8
travel_hypothesis = 7

# the hypothesis talks about the travel time by car and cycle, referenced also in the premise
if travel_hypothesis <= travel_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel time, any time less than 'travel_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
