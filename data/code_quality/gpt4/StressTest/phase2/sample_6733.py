start_road_premise = 3
start_road_hypothesis = 2

# the hypothesis talks about the start of the route that Bill needs to take, which is also referenced in the premise
if start_road_hypothesis >= start_road_premise:
    # check if the hypothesis value contradicts the estimate of less than 'start_road_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the starting road
    # a starting road less than 'start_road_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
