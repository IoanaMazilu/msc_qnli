travel_time_premise = 7
travel_time_hypothesis = 8

# the hypothesis talks about the travel time from A to B and back, referenced also in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the travel time, which is consistent with the hypothesis
    # but the hypothesis value cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
