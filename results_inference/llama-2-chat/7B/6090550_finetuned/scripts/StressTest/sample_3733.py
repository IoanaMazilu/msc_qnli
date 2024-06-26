travel_time_premise = 8
travel_time_hypothesis = 7

# the hypothesis refers to the travel time from A to B and back, which is also mentioned in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the travel time in the hypothesis contradicts the estimate of less than 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel time
    # any travel time less than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
