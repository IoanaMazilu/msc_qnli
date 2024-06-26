travel_time_premise = 7
travel_time_hypothesis = 8

# the hypothesis refers to the travel time from A to B and back mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the travel time in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel time
    # any travel time less than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
