travel_time_premise = 7
travel_time_hypothesis = 1

# the hypothesis talks about the time taken for the journey, which is also mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the estimate of 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken,
    # any time taken less than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
