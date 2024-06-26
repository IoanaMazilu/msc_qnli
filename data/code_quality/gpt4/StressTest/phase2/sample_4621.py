road_time_premise = 1
road_time_hypothesis = 6

# the hypothesis refers to the time Steve spends on the roads, as mentioned in the premise
if road_time_hypothesis <= road_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'road_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time spent on the roads
    # any time greater than 'road_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
