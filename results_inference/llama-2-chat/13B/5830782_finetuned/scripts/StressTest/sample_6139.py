travel_time_premise = 4
travel_time_hypothesis = 7

# the hypothesis talks about the duration of Kiran's travel, which is also mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of travel
    # any duration greater than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
