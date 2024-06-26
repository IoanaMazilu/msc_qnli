start_road_premise = 2
start_road_hypothesis = 3

# the hypothesis talks about the starting road number, also referenced in the premise
if start_road_hypothesis > start_road_premise:
    # check if the hypothesis value contradicts the premise's start road number
    label = "contradiction"
else:
    # the premise gives only a precise value for the starting road number
    # a starting road number less than or equal to 'start_road_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
